#!/usr/bin/python df

import string, time
import serial
import time


output = (" ")
ser =serial.Serial('/dev/ttyACM0', 9600)

while True:
    try:
        output = int(ser.readline())
        print("hasil terbaca: ",output)
    except KeyboardInterrupt as e:
        print("Exit Program")
        print("============")
        break
