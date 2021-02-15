# import RPi.GPIO as GPIO
# import pyrebase
# import time
# import automode

# # config = {
# #     "apiKey": "AIzaSyCgZED8uqNacFRqXcEV7a2jQL2WApeWTu4",
# #         "authDomain": "coding-faction.firebaseapp.com",
# #             "databaseURL": "https://coding-faction.firebaseio.com/",
# #                 "storageBucket": "coding-faction.appspot.com"
# # }
# # firebase = pyrebase.initialize_app(config)
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

def lights(room_data):
    # db = firebase.database()
    room_data=room_data.pop("mode")

    pins=[1, 2, 3, 4, 5, 6]
    raspi={}
    d=[]
    for device in room_data :
        i=1
        raspi[device.key()] =device.val() 
        d.append([[device.key(),device.val()],i])
        i=i+1
    # d.append([2])
    # d.append([3])
    # d.append([4])
    # d.append([5])
    # d.append([6])
    for i, j in d.items():
        GPIO.setup(j[1], GPIO.OUT) 

        if(j[0]== 1):

            GPIO.output(j[1], 0)
        else:
            GPIO.output(j[1], 1)
        time.sleep(0.1)

#     # pins=[1, 2, 3, 4, 5, 6]
#     # while(True):
#     #     # switch = db.child("Tests").get()
#     #     d={}
#     #     for user in switch.each() :
#     #         d[user.key()] =user.val()
#     #     d['Bulb1'].append(1)
#     #     d['Bulb2'].append(2)
#     #     d['Bulb3'].append(3)
#     #     d['Bulb4'].append(4)
#     #     d['Bulb5'].append(5)
#     #     d['Bulb6'].append(6)
#     #     for i, j in d.items():
#     #         GPIO.setup(j[1], GPIO.OUT) 

#     #         if(j[0]== 1):

#     #             GPIO.output(j[1], 0)
#     #         else:
#     #             GPIO.output(j[1], 1)
#     #         time.sleep(0.1)

