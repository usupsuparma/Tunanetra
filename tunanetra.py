import time
import RPi.GPIO as GPIO


def measure():
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    start = time.time()

    while GPIO.input(echo == 0):
        start = time.time()

    while GPIO.input(echo == 1):
        stop = time.time()
    elepsed = stop - start
    distance = (elepsed * 34300)/2
    return distance
def measure_average():
    #this
    distance1 = measure()
    time.sleep(0.1)
    distance2 = measure()
    time.sleep(0.1)
    distance3 = measure()
    time.sleep(0.1)
    distance = distance1 + distance2 + distance3
    distance = distance/3
    return distance


# main program


# GPIO
GPIO.setmode(GPIO.BCM)


# GPIO yang digunakan
trig = 23
echo = 24

print("ultrasonik measuring")

# set pin output and input
GPIO.setup(trig, GPIO.OUT) # triger
GPIO.setup(echo, GPIO.IN) # echo

GPIO.output(trig , False)

try:
    while True:
        distance = measure_average()
        print("jarak adalah: %.1f "% distance)
        time.sleep(1)
except KeyboardInterrupt:
    # gunakan ctrl + c
    GPIO.cleanup()
