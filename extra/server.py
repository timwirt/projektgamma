# Run with
#   uvicorn server:server --port 8000 --reload

try:
  import serverlogik
except ImportError as e:
  print(f"Importing the shared library 'serverlogik' did not work.")
  print(f"Is (a link to) the shared library 'serverlogik.____.so' in the same directory as this python script?")
  print(f"The import caused the following exception '{e}'")
  print(f"Exiting")
  exit(1)

try:
  import fastapi_restful.tasks
except ImportError as e:
  print(f"Importing the shared library 'fastapi_restful.tasks' did not work.")
  print(f"Is the library 'fastapi_restful' installed?")
  print(f"Install it with: 'pip install fastapi_restful'")
  print(f"The import caused the following exception '{e}'")
  print(f"Exiting")
  exit(1)

import os
import json
import sched
import time
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn  
import threading
from fastapi_restful.tasks import repeat_every
from serverlogik import Serverlogik

# Read server.json on server start
f = open('server.json')
server_infos = json.load(f)
f.close()

# Konto- list
konto_list = server_infos['konto_list']

# Gueter- list
gueter_list = server_infos['gueter']

# Serverlogik
sl = Serverlogik()

# Object to config the webservice
server = FastAPI()

# Add path to main '/'
@server.get("/")
async def main():
    return server_infos

# Add path to login '/login/{name}/{pwd}'
@server.get("/login/{name}/{pwd}")
async def login(name:str, pwd:str):
    if (name in konto_list):
        if(pwd == server_infos['konten'][name]['pwd']):
            return True
        
    return False

# Add path to signin '/signin/{name}/{pwd}/{pwd_test}'
@server.get("/signin/{name}/{pwd}/{pwd_test}")
async def signin(name:str, pwd:str, pwd_test:str):
    if (not(name in konto_list)):
        if(pwd == pwd_test):
            # add konto
            server_infos['konten'][name] = create_konto(name, pwd)
            server_infos['konto_list'].append(name)
            
            # save json
            update_server_json()

            # update main view
            main()
            return True
        
    return False

# Add path to get_stocks '/stocks'
@server.get("/stocks")
async def stocks():
    return server_infos['gueter']

# Add path to '/deposit/{name}/{value}'
@server.get("/deposit/{name}/{value}")
async def deposit(name:str, value:float):
    server_infos['konten'][name]['coins'] = server_infos['konten'][name]['coins'] + value
    update_server_json()

# Add path to '/withdraw/{name}/{value}'
@server.get("/withdraw/{name}/{value}")
async def withdraw(name:str, value:float):
    coins = server_infos['konten'][name]['coins']
    if coins > 0 and value <= coins:
        server_infos['konten'][name]['coins'] = coins - value
    update_server_json()

# Add path to '/buy/{name}/{stock}'
@server.get("/buy/{name}/{stock}")
async def buy(name:str, stock:str):
    server_infos['konten'][name]['konto_gueter'][stock] = server_infos['konten'][name]['konto_gueter'][stock] + 1
    server_infos['konten'][name]['coins'] = server_infos['konten'][name]['coins'] - server_infos['gueter'][stock][19]

# Add path to '/sell/{name}/{stock}'
@server.get("/sell/{name}/{stock}")
async def sell(name:str, stock:str):
    server_infos['konten'][name]['konto_gueter'][stock] = server_infos['konten'][name]['konto_gueter'][stock] - 1
    server_infos['konten'][name]['coins'] = server_infos['konten'][name]['coins'] + server_infos['gueter'][stock][19]

'''Helper methods'''
def create_konto(name:str, pwd:str):
    # return Konto- structure
    return {
        "name": name,
        "pwd": pwd,
        "coins" : 0.0,
        "konto_gueter": {
            "Klausurzulassung": 0,
            "Note": 0,
            "Klopapier": 0,
            "Nudeln": 0,
            "Konserven": 0,
            "Klausurbestechungsgeld": 0,
            "Bachelor B.Sc.": 0,
            "Bachelor B.A.": 0,
            "Bachelor B.Eng.": 0,
            "Mensaessen": 0,
            "Master": 0,
            "Docktor": 0
        }
    }

def update_server_json():
    with open('server.json', "r+") as jsonFile:
        json.dump(server_infos, jsonFile)
    jsonFile.close()

@server.on_event("startup")
@repeat_every(seconds=5)
def update_values():
    global gueter_list

    gueter_list = sl.new_values(gueter_list)
    server_infos['gueter'] = gueter_list

    update_server_json()
