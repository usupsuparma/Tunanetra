#!/usr/bin/python

import serial, string, time

output = (" ")
ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)

while True:
    try:
        print("----")
        while output != (""):
            output = ser.readline()
            print(output)
        output = (" ")
    except KeyboardInterrupt:
        print("keluar dari program")
