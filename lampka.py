import RPi.GPIO as GPIO
import time

rel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(rel,GPIO.OUT, initial=GPIO.HIGH)

while True:
    czas = time.strftime("%S")
    if int(czas) == 5 :
        GPIO.output(rel, GPIO.LOW)
        time.sleep(5)
        GPIO.output(rel, GPIO.HIGH)