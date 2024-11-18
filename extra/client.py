# pyside6-uic mainwindow.ui > ui_mainwindow.py
# Run with:
#   python3 client.py

import time
import sys
import requests
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QStackedWidget, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QTimer

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from UIPythonFiles.ui_anmelden import Ui_Anmelden
from UIPythonFiles.ui_registrieren import Ui_Registrieren
from UIPythonFiles.ui_stockx import Ui_StockX
from UIPythonFiles.ui_ein_auszahlen import Ui_Ein_Auszahlen

import numpy as np

plt.rcParams['figure.figsize'] = (16, 11)

import time
starttime = time.time()

host = "http://127.0.0.1:8000"

# The MainWindow-UI class to be opened by the client-application
class Ui(QtWidgets.QMainWindow):
    # The constructor loads all windows
    def __init__(self):
        super().__init__()
        self.amount = 0
        self.withdraw = True
        self.hostx_open = False
        self.user_name = ""
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.Anmelden()
        self.Registrieren()
        self.StockX()
        self.Ein_auszahlen()
        self.setCentralWidget(self.stacked_widget)
        self.setWindowTitle("Anmelden")
        self.resize(300,400)

        self.timer = QTimer()
        self.timer.setInterval(5000)
        
        # Connect the timeout signal to a custom function
        self.timer.timeout.connect(self.run_updateGui)

        # Starts the scheduler
        self.timer.start()

    def run_updateGui(self):
        if(self.stacked_widget.currentIndex() == 2):# Stockx-GUI
            # update view
            self.goto_page(self.ein_auszahlen_widget, False)
            self.goto_page(self.stockx_widget)

    # The Ein_asuzahlen method loads the Ui_Anmelden-GUI
    def Anmelden(self):
        self.anmelde_widget = QtWidgets.QMainWindow()
        Ui_Anmelden().setupUi(self.anmelde_widget)
        self.stacked_widget.addWidget(self.anmelde_widget)
        self.to_regestrieren_button = self.anmelde_widget.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.to_regestrieren_button.clicked.connect(lambda : self.goto_page(self.regestrier_widget))
        self.anmelden_button = self.anmelde_widget.findChild(QtWidgets.QPushButton, 'pushButton')
        self.anmelden_button.clicked.connect(lambda : self.handleAnmelden())

    # The Ein_asuzahlen method loads the Ui_Registrieren-GUI
    def Registrieren(self):
        self.regestrier_widget = QtWidgets.QMainWindow()
        Ui_Registrieren().setupUi(self.regestrier_widget)
        self.stacked_widget.addWidget(self.regestrier_widget)
        self.to_anmelden_button = self.regestrier_widget.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.to_anmelden_button.clicked.connect(lambda : self.goto_page(self.anmelde_widget))
        self.registrieren_button = self.regestrier_widget.findChild(QtWidgets.QPushButton, 'pushButton')
        self.registrieren_button.clicked.connect(lambda : self.handleRegistrieren())

    # The Ein_asuzahlen method loads the Ui_StockX-GUI
    def StockX(self):
        self.stockx_widget = QtWidgets.QMainWindow()
        Ui_StockX().setupUi(self.stockx_widget)
        self.stacked_widget.addWidget(self.stockx_widget)
        self.einzahlen_button = self.stockx_widget.findChild(QtWidgets.QPushButton, 'pushButton')
        self.einzahlen_button.clicked.connect(lambda : self.handleEinzahlenAuszahlen(False))
        self.auszahlen_button = self.stockx_widget.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.auszahlen_button.clicked.connect(lambda : self.handleEinzahlenAuszahlen(True))
        self.abmelden_button = self.stockx_widget.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.abmelden_button.clicked.connect(lambda : self.handleAbmelden())

    # The Ein_asuzahlen method loads the Ui_Ein_Auszahlen-GUI
    def Ein_auszahlen(self):
        self.ein_auszahlen_widget = QtWidgets.QMainWindow()
        Ui_Ein_Auszahlen().setupUi(self.ein_auszahlen_widget)
        self.stacked_widget.addWidget(self.ein_auszahlen_widget)
        self.ein_auszahlen_fertig_button = self.ein_auszahlen_widget.findChild(QtWidgets.QPushButton, 'pushButton')
        self.ein_auszahlen_fertig_button.clicked.connect(lambda : self.handleEinAusZahlen())
        self.ein_auszahlen_zurueck_button = self.ein_auszahlen_widget.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.ein_auszahlen_zurueck_button.clicked.connect(lambda : self.goto_page(self.stockx_widget))
        self.ein_auszahlen_widget.findChild(QtWidgets.QRadioButton, 'radioButton').clicked.connect(lambda : self.setAmount(0))
        self.ein_auszahlen_widget.findChild(QtWidgets.QRadioButton, 'radioButton_2').clicked.connect(lambda : self.setAmount(100))
        self.ein_auszahlen_widget.findChild(QtWidgets.QRadioButton, 'radioButton_3').clicked.connect(lambda : self.setAmount(250))
        self.ein_auszahlen_widget.findChild(QtWidgets.QRadioButton, 'radioButton_4').clicked.connect(lambda : self.setAmount(500))
    
    # The setAmount method saves the value to withdraw or deposit in this class
    def setAmount(self, number:int):
        self.amount = number
    
    # The handleWithdrawDeposit methods loads a boolean and changes the site to depositing-gui or withdrawing-gui
    def handleEinzahlenAuszahlen(self, withdraw_:bool):
        self.withdraw = withdraw_
        self.goto_page(self.ein_auszahlen_widget)

    # The handleWithdrawDeposit method deposits or withdraws money saved in the current class
    def handleEinAusZahlen(self):
        if self.withdraw:
            # the actual Withdrawing
            requests.get(f"{host}/withdraw/{self.user_name}/{self.amount}")
        else:
            # the actual Depositing
            requests.get(f"{host}/deposit/{self.user_name}/{self.amount}")
        
        # changes the gui_window to the stockx-gui
        self.goto_page(self.stockx_widget)

    # The handleLogin method logs in an existing user
    def handleAnmelden(self):
        # resets the input_fields to be empty
        name = self.anmelde_widget.findChild(QtWidgets.QLineEdit, 'lineEdit').text()
        self.anmelde_widget.findChild(QtWidgets.QLineEdit, 'lineEdit').setText("")
        password = self.anmelde_widget.findChild(QtWidgets.QLineEdit, 'lineEdit_2').text()
        self.anmelde_widget.findChild(QtWidgets.QLineEdit, 'lineEdit_2').setText("")
        
        # determins wether the input is valid
        if(name == "" or password == ""):
            print("Neither the Username nor the Password is allowed to be blanc!")
            return

        # the actual logging in
        try:
            response = requests.get(f"{host}/login/{name}/{password}").json()
        except Exception as e:
            print("An Error accured: " + e.args)
        
        if(response):
            print("You logged in as: " + name)
            self.setName(name)
            self.goto_page(self.stockx_widget)
        else:
            print("You couldn't login!")
    
    # The handleSignin method registers a new user
    def handleRegistrieren(self):
        # resets the input_fields to be empty
        name = self.regestrier_widget.findChild(QtWidgets.QLineEdit, 'lineEdit').text()
        self.regestrier_widget.findChild(QtWidgets.QLineEdit, 'lineEdit').setText("")
        password = self.regestrier_widget.findChild(QtWidgets.QLineEdit, 'lineEdit_2').text()
        self.regestrier_widget.findChild(QtWidgets.QLineEdit, 'lineEdit_2').setText("")
        password_test = self.regestrier_widget.findChild(QtWidgets.QLineEdit, 'lineEdit_3').text()
        self.regestrier_widget.findChild(QtWidgets.QLineEdit, 'lineEdit_3').setText("")

        # determins wether the input is valid
        if(name == "" or password == ""):
            print("Neither the Username nor the Password is allowed to be blanc!")
            return

        # the actual signing in
        try:
            response = requests.get(f"{host}/signin/{name}/{password}/{password_test}").json()
        except Exception as e:
            print("An Error accured: " + e.args)
        
        if(response):
            print("You created an account with the name: " + name)
            self.setName(name)
            self.goto_page(self.stockx_widget)
        else:
            print("You couldn't create the account!")
    
    # The handleLogout method logs out the currently logged in user
    def handleAbmelden(self):
        print("You logged out!")
        self.goto_page(self.anmelde_widget)
    
    # The goto_page method takes a loaded_widget_page and opens it on the MainWindow
    # It also resizes the window and updates the WindowTitle
    def goto_page(self, widget:QMainWindow, resize:bool=True):
        self.setWindowTitle(widget.windowTitle())
        index = self.stacked_widget.indexOf(widget)
        self.hostx_open = False
        if index == 0 and resize:
            self.resize(300,400)
        elif index == 1 and resize:
            self.resize(300,400)
        elif index == 2:
            self.updateCoins(self.user_name)
            self.updateGueter(self.user_name)

            self.hostx_open = True
            if resize:
                self.resize(1600,800)
        elif index == 3 and resize:
            self.resize(500,500)
            
        if index >= 0:
            self.stacked_widget.setCurrentIndex(index)
    
    # The setName method updates the used name to the username of the just logged in user
    def setName(self, name:str):
        self.user_name = name
        name_label = self.stockx_widget.findChild(QtWidgets.QLabel, 'label_3')
        name_label.setText(name)

    # The updateCoins method updates the coins in the stockx-gui and ein_auszahlen-gui
    def updateCoins(self, name:str):
        response = requests.get(f"{host}/").json()
        coins = "{:.2f}".format(response['konten'][name]['coins'])
        name_label = self.stockx_widget.findChild(QtWidgets.QLabel, 'label_2')
        name_label.setText(coins + "\u00a7")
        coinsLabel = self.ein_auszahlen_widget.findChild(QtWidgets.QLabel, 'label_2')
        coinsLabel.setText(coins + "\u00a7")

    # The buy method gets a username and a stockname and buys one stock if possible
    def kaufen(self, name:str, stock:str):
        response = requests.get(f"{host}/").json()
        # tests if buying is possible (because of own coins)
        coins = response['konten'][name]['coins']
        price = response['gueter'][stock][19]
        if coins < price:
            print("You can't buy: " + stock + " because you don't have enough money!")
            return
        print("You bought a stock of: " + stock)
        requests.get(f"{host}/buy/{name}/{stock}").json()
        # update view
        self.goto_page(self.ein_auszahlen_widget, False)
        self.goto_page(self.stockx_widget)
    
    # The sell method gets a username and a stockname and sells one stock if possible
    def verkaufen(self, name:str, stock):
        response = requests.get(f"{host}/").json()
        # tests if sell is possible (because of amount owned)
        amount = response['konten'][name]['konto_gueter'][stock]
        if amount == 0:
            print("You can't sell: " + stock + " because you don't own any!")
            return
        print("You sold a stock of: " + stock)
        requests.get(f"{host}/sell/{name}/{stock}").json()
        # update view
        self.goto_page(self.ein_auszahlen_widget, False)
        self.goto_page(self.stockx_widget)

    # The create_button_click_handler method gets a key and returns the 'kaufen'-method
    def create_button_click_handler(self, key:str):
        return (lambda: self.kaufen(self.user_name, key))
    # The create_button_click_handler_verkaufen method gets a key and returns the 'verkaufen'-method
    def create_button_click_handler_verkaufen(self, key:str):
        return (lambda: self.verkaufen(self.user_name, key))

    # The updateGueter method updates the List<Gueter> in the gui
    def updateGueter(self, name:str):
        response = requests.get(f"{host}/").json()
        gueter = dict(response['gueter'])

        tableWidget = QtWidgets.QTableWidget(self.stockx_widget.findChild(QtWidgets.QTableWidget, 'tableWidget'))
        tableWidget.setFixedSize(1600, 600)
        tableWidget.setRowCount(12)  # Zeilen
        tableWidget.setColumnCount(7)  # Spalten

        tableWidget.setHorizontalHeaderLabels(['Stock', 'Einzelpreis', 'Wertentwicklung', 'Kaufen', 'Verkaufen', 'Meine Güter', 'Wert meiner Gueter'])

        for i in range(12):
            tableWidget.setRowHeight(i, 120)
        for i in range(7):
            tableWidget.setColumnWidth(i, 150)

        tableWidget.setColumnWidth(0, 200)
        tableWidget.setColumnWidth(2, 500)

        # Name der Gueter
        count = 0
        for key in gueter:
            # Gueter-Name
            item = QtWidgets.QTableWidgetItem()
            item.setText(key)
            tableWidget.setItem(count, 0, item)
            # Einzelpreis
            item = QtWidgets.QTableWidgetItem()
            gueterPreis = gueter[key][19]
            item.setText("{:.2f}".format(gueterPreis))
            tableWidget.setItem(count, 1, item)

            # Gueter-Graph
            plt.clf()
            plt.cla()
            gut = gueter[key]
            kurs = np.zeros(20)
            i = 0
            for price in gut:
                kurs[i] = price
                i = i + 1
            fig, ax = plt.subplots()
            ax.plot(kurs)
            
            # Remove unwanted axes
            ax.set_xticks([])
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.yaxis.tick_left()

            # Create a FigureCanvas instance
            canvas = FigureCanvas(fig)
            # Disable the background to make it transparent
            canvas.setStyleSheet("background-color: transparent;")
            # Set the item as the cell widget
            tableWidget.setCellWidget(count, 2, canvas)
            plt.close()

            # Kaufen
            button = QtWidgets.QPushButton(tableWidget)
            button.setText("1x Kaufen")
            button.clicked.connect(self.create_button_click_handler(key))
            tableWidget.setCellWidget(count, 3, button)
            plt.close()

            # Verkaufen
            button = QtWidgets.QPushButton(tableWidget)
            button.setText("1x Verkaufen")
            button.clicked.connect(self.create_button_click_handler_verkaufen(key))
            tableWidget.setCellWidget(count, 4, button)

            # Gueter-Count
            item = QtWidgets.QTableWidgetItem()
            objCount = str(response['konten'][name]['konto_gueter'][key])
            item.setText(objCount)
            tableWidget.setItem(count, 5, item)

            # Wert der Gueter
            item = QtWidgets.QTableWidgetItem()
            objCount = response['konten'][name]['konto_gueter'][key]
            gueterPreis = gueter[key][19]
            value = objCount*gueterPreis
            item.setText("{:.2f}".format(value))
            tableWidget.setItem(count, 6, item)

            count = count + 1
        
# The application gets executed and the window-gui gets opened
if __name__ == "__main__":
  app = QtWidgets.QApplication([])

  window = Ui()
  window.show()

  sys.exit(app.exec())