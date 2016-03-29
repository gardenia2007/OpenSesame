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

while True:
    s = socket.socket()
    s.connect((server_ip, server_port))

    data = s.recv(1)
    localtime = time.asctime( time.localtime(time.time()) )
    print localtime, "recv:", data
    if data == 'b':
        print localtime, "Open the door!"

        GPIO.output(switch1, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(switch1, GPIO.LOW)

        time.sleep(0.5) 

        GPIO.output(switch2, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(switch2, GPIO.LOW)

        time.sleep(0.5)

        GPIO.output(switch2, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(switch2, GPIO.LOW)

        time.sleep(0.5)

        GPIO.output(switch2, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(switch2, GPIO.LOW)
    s.close()
    time.sleep(1)



