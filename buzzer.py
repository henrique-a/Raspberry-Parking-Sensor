import RPi.GPIO as GPIO 
import time 

def init_buzzer(pin,freq):
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(12, GPIO.OUT) 
    buzzer = GPIO.PWM(12,100)
    return buzzer

def buzz(pitch, duration,DC,p):
	p.ChangeFrequency(pitch)
	p.start(DC)
   	time.sleep(duration)
    	p.stop()
    	time.sleep(1)
