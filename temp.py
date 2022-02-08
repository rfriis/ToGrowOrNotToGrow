#!/usr/bin/python3

import time
from black import err
import pyrebase
import time
import board
import adafruit_dht  # temp sensor library

# firebase connection
config = {
    "apiKey": "AIzaSyCxpY5MD4saji785VBMgEqQOuO9ZnieulY",
    "authDomain": "cmp400-269dd.firebaseapp.com",
    "databaseURL": "https://cmp400-269dd-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "cmp400-269dd",
    "storageBucket": "cmp400-269dd.appspot.com",
    "messagingSenderId": "547369903506",
    "appId": "1:547369903506:web:769a29a5faccb92fa8cd4b",
    "measurementId": "G-L7B0KP9CYW",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# attempt to establish connection with sensor
# if connection made, send True to firebase, else send False
tempSensor = None

while True:
    tempConnection = False
    try:
        tempSensor = adafruit_dht.DHT22(board.D4)
        if tempSensor:
            tempConnection = True
    except Exception as error:
        print(error.args[0])

    # send connection variable to firebase
    data = {"tempConnection": tempConnection}
    db.child("Connections").set(data)
