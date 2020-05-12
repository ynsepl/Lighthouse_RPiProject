import RPi.GPIO as GPIO
import time

rel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(rel,GPIO.OUT, initial=GPIO.HIGH)

while True:
    hours = time.strftime("%H")
    seconds = time.strftime("%S")
    if int(hours) == 10 :
        if int(seconds) == 5:
            GPIO.output(rel, GPIO.LOW)
            time.sleep(5)
            GPIO.output(rel, GPIO.HIGH)