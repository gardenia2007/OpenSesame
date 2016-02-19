# -*- coding: utf-8 -*-

import os
import socket

import RPi.GPIO as GPIO
import time

switch1 = 16
switch2 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(switch1, GPIO.OUT)
GPIO.setup(switch2, GPIO.OUT)

s = socket.socket()
s.connect(('120.27.52.70', 20000))

while True:
    data = s.recv(1)

    if data == 'b':
        print "Open the door!"
        GPIO.output(switch1, GPIO.HIGH)
        GPIO.output(switch2, GPIO.LOW)
        time.sleep(1)
    
        GPIO.output(switch1, GPIO.LOW)
        GPIO.output(switch2, GPIO.HIGH)
        time.sleep(1)

s.close()

