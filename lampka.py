import RPi.GPIO as GPIO
import time
import datetime

rel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(rel,GPIO.OUT, initial=GPIO.HIGH)
while True:
    czas = datetime.datetime.now()
    if czas.minute == 17 :
        GPIO.output(rel, GPIO.LOW)
        time.sleep(5)
        GPIO.output(rel, GPIO.HIGH)
        time.sleep(55)