#!/usr/bin/python

import serial, string, time
import time
import RPi.GPIO as GPIO

output = (" ")
ser = serial.Serial('/dev/ttyACM0', 9600)

try:
    while True:
        print("----")
        while output != (""):
            output =int(ser.readline())
            print(output)
            output = (" ")
except KeyboardInterrupt:
    print("keluar dari program euy")
    # gunakan ctrl + c
    GPIO.cleanup()
