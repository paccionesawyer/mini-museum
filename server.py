#Server code for ME 30 Project 4
#Olif Hordofa
#Dec 08, 2020

import RPi.GPIO as GPIO
from flask import Flask
import time

app = Flask(__name__)

#assign pins to be used
P_A1 = 11 
P_A2 = 12
P_B1 = 13
P_B2 = 15
delay = 0.01 # time to settle

#setup the pins into output
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_A1, GPIO.OUT)
    GPIO.setup(P_A2, GPIO.OUT)
    GPIO.setup(P_B1, GPIO.OUT)
    GPIO.setup(P_B2, GPIO.OUT)

#move the motor clockwise
def forwardStep():
    setStepper(1, 0, 1, 0)
    setStepper(0, 1, 1, 0)
    setStepper(0, 1, 0, 1)
    setStepper(1, 0, 0, 1)

#move the motor counterclockwise
def backwardStep():
    setStepper(1, 0, 0, 1)
    setStepper(0, 1, 0, 1)
    setStepper(0, 1, 1, 0)
    setStepper(1, 0, 1, 0)

#controls excitation to fire up
def setStepper(in1, in2, in3, in4):
    GPIO.output(P_A1, in1)
    GPIO.output(P_A2, in2)
    GPIO.output(P_B1, in3)
    GPIO.output(P_B2, in4)
    time.sleep(delay)

setup()

#keyword "scream" comes in from the client (mic)
@app.route('/scream')
def scream():

    for i in range(67):
        forwardStep()

    time.sleep(5)

    for i in range(68):
        backwardStep()

    return "Hope it was fun!"

#keyword "mona" comes in from the client (mic)
@app.route('/mona')
def monalisa():

    for i in range(68):
        backwardStep()
    time.sleep(5)
    for i in range(67):
        forwardStep()
   
    return "Hope it was fun!"

GPIO.cleanup()