#!/usr/bin/python df
import serial
import string, time
import time


#ser =serial.Serial('/dev/ttyACM0', 9600)
ser = serial.Serial('/dev/ttyACM0', 9600)
output = int(ser.readline())
print("hasil terbaca: ",output)
