# Projekt Gamma

## Bibliothek für den Server bauen
Um das Projekt zu bauen, soll einer der folgenden Befehlsketten im Projektverzeichnis ausgeführt werden.
In Linux Mint verwendet man
```
cmake -S . -B build && cmake --build build
```
Auf den Rechnern der CIP Pools ist der Aufruf leider ein wenig länger
```
export PROJ_PATH=`pwd` && cmake -S $PROJ_PATH -B $PROJ_PATH/build && cmake --build $PROJ_PATH/build
```
Falls das Projekt so nicht baut, liegen entweder Implementierungsfehler vor oder es fehlen externe Softwarepakete.

## Server starten
Der Server benötogt folgende Pakete, die mit `pip install <package>` installiert werden können:

- fastapi_restful

Der Server liegt im Verzeichnis `./projektbeta/extra`. Danach kann der Server mit 
```
uvicorn server:server --port 8000 --reload
```

gestartet werden.

## Client starten
Der Client benötogt folgende Pakete, die mit `pip install <package>` installiert werden können:

- matplotlib

Der Client liegt im Verzeichnis `./projektbeta/extra`. Danach kann der Client mit 
```
python3 client.py
```
gestartet werden.

## Qt-Probleme
Falls beim Bauen von QT-Anwendungen eine Klasse nicht gefunden wird, kann das an nicht eingebundenen Headern oder einer unvollständigen CMakekonfiguration liegen.
Hier kann ein Blick in die [Qt6-Dokumentation](https://doc.qt.io/) der fehlenden Klasse helfen.
Anschließend müssen die Header eingebunden werden, das `CMakeLists` angepasst werden und die oben genannte `cmake`-Befehlskette erneut aufgerufen werden.
