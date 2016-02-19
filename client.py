# -*- coding: utf-8 -*-

import os
import socket

import RPi.GPIO as GPIO
import time

from setting import *

switch1 = 16
switch2 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(switch1, GPIO.OUT)
GPIO.setup(switch2, GPIO.OUT)

s = socket.socket()
s.connect((server_ip, server_port))

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

