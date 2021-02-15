import RPi.GPIO as GPIO
# import pyrebase
import time
# import automode

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def lights(room_data):
    # db = firebase.database()
    room_data=room_data.pop("mode")

    pins=[1, 2, 3, 4, 5, 6]
    raspi={}
    d=[]
    for device in room_data :
        i=0
        # raspi[device.key()] =device.val() 
        d.append([device,pins[i],room_data.get(device)])
        i=i+1
    for device in d:
        GPIO.setup(d[1], GPIO.OUT) 
        if(d[2]== 'true'):
            GPIO.output(d[1], 0)
        else:
            GPIO.output(d[1], 1)
        time.sleep(0.1)
    # d.append([2])
    # d.append([3])
    # d.append([4])
    # d.append([5])
    # d.append([6])
    # for i, j in d.items():
    #     GPIO.setup(j[1], GPIO.OUT) 

    #     if(j[0]== 1):

    #         GPIO.output(j[1], 0)
    #     else:
    #         GPIO.output(j[1], 1)
    #     time.sleep(0.1)


