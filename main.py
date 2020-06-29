import sys
sys.path.append('latch_sdk_python')
import config.latch
import latch
import json
from time import sleep
import RPi.GPIO as GPIO

#Setup GPIOP
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.HIGH)

def doorButton():
    GPIO.output(17, GPIO.LOW)
    sleep(0.5)
    GPIO.output(17, GPIO.HIGH)

def openDoor():
    doorButton()
    sleep(50)
    doorButton()

api = latch.Latch(config.latch.appId, config.latch.secret)
with open('config/accounts.txt', 'r') as f:
    accountIds = [s.replace('\n', '') for s in f.readlines()]
while True:
    for id in accountIds:
        response = api.status(id)
        if response == None:
            print("Connection error")
            continue
        responseData = response.get_data()
        status = responseData['operations'][config.latch.appId]['status']
        if status == "on":
            print("Opening door...")
            openDoor()

