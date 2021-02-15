import RPi.GPIO as GPIO
from lights import lights
import pyrebase
import automode
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Listens to stream
def stream_handler(message):
    # print("changed")
    # print(message["event"])
    # print(message["path"]) 
    print(message["data"])
    return (message["data"])

def Database():
    config = {
        "apiKey": "AIzaSyCgZED8uqNacFRqXcEV7a2jQL2WApeWTu4",
        "authDomain": "coding-faction.firebaseapp.com",
        "databaseURL": "https://coding-faction.firebaseio.com/",
        "storageBucket": "coding-faction.appspot.com"
    }
    firebase = pyrebase.initialize_app(config)
    db=firebase.database()
    # x=db.child("Classes").child("Ground Floor").child("G1").get()
    # print(x.val())
    my_stream =db.child("Classes").child("Ground Floor").child("G1").stream(stream_handler)
    return (my_stream)

# Main Function
def Main():
    # Check time 


    #check database
    room_data=Database()
    autoMode=room_data["mode"]
    if(autoMode==True):
        lights(room_data)

# Runs main function
Main()
    


