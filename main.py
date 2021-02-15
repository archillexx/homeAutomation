import RPi.GPIO as GPIO
from lights import lights
import pyrebase
# import automode
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Listens to stream
def stream_handler(message):
    # print("changed")
    # print(message["event"])
    # print(message["path"]) 
    print(message["data"])
    checkMode(message["data"])

def checkMode(room_data):
    autoMode=room_data["mode"]
    if(autoMode==True):
        lights(room_data)


# Main Function
def Main():
    print("RUNNING")
    config = {
        "apiKey": "AIzaSyCgZED8uqNacFRqXcEV7a2jQL2WApeWTu4",
        "authDomain": "coding-faction.firebaseapp.com",
        "databaseURL": "https://coding-faction.firebaseio.com/",
        "storageBucket": "coding-faction.appspot.com"
    }
    firebase = pyrebase.initialize_app(config)
    db=firebase.database()
    db.child("Classes").child("Ground Floor").child("G1").stream(stream_handler)
    # Check time 

# Runs main function
Main()
    


