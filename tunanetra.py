import time
import RPi.GPIO as GPIO
import serial, string, time



# main program

output = (" ")
ser = serial.Serial('/dev/ttyACM0', 9600)


try:
    while True:
        output =str(int(ser.readline()))
        print("data jarak: ", output)
        if output > 50:
            print(output)
            print("jarak aman")
        elif output < 50:
            print("jarak bahaya")
        else:
            print("data jarak tidak ada")

except KeyboardInterrupt:
    # gunakan ctrl + c
    GPIO.cleanup()
