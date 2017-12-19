import RPi.GPIO as GPIO 
import time 

def init_buzzer(pin, freq):
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(pin, GPIO.OUT) 
    buzzer = GPIO.PWM(pin, 100)
    return buzzer

def buzz(pin, duration, DC):
    bz = GPIO.PWM(pin, 100)
    bz.start(DC)
    time.sleep(0.5)
    bz.stop()
    time.sleep(duration)