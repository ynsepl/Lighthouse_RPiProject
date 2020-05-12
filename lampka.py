import RPi.GPIO as GPIO
import time
import keyboard


rel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(rel,GPIO.OUT, initial=GPIO.HIGH)

#Automatic start
while True:
    hours = time.strftime("%H")
    seconds = time.strftime("%S")
    if int(hours) == 10 :
        if int(seconds) == 5:
            GPIO.output(rel, GPIO.LOW)
            time.sleep(5)
            GPIO.output(rel, GPIO.HIGH)
while True:
    try:  
        if keyboard.is_pressed('s'):  
            GPIO.output(rel, GPIO.LOW)
            pass
        
        elif keyboard.is_pressed("space"):
            GPIO.output(rel, GPIO.HIGH)
            pass
