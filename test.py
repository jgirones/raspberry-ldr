import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 23

GPIO.setup(pin, GPIO.IN)

time.sleep(0.25)

light = GPIO.input(pin)
print light
    
