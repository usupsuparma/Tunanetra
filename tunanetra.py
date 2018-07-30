import time
import RPi.GPIO as GPIO
import serial, string, time



# main program

output = (" ")
ser = serial.Serial('/dev/ttyACM0', 9600)


try:
    while True:
        output =str(int(ser.readline()))
        if output != " ":            
            if output <= 50:
                print(output)
                print("jarak bahaya")
            elif output >= 50:
                print("jarak aman")
        else:
            print("data jarak tidak ada")

except KeyboardInterrupt:
    # gunakan ctrl + c
    GPIO.cleanup()
    break()
