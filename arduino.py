#!/usr/bin/python

import serial, string, time

output = " "
ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)




try:
    while True:
        print ("----")
        while output != (" "):
            output = ser.readline()
            print("hasil: ",output)
        output = " "

except KeyboardInterrupt:
    # gunakan ctrl + c
    GPIO.cleanup()
