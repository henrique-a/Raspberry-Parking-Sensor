import RPi.GPIO as GPIO 
import time 
import threading as th

class Buzzer(th.Thread):

    def __init__(self, pin, freq, level):
        self.level = level
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(pin, GPIO.OUT) 
        self.pwm = GPIO.PWM(pin,freq)
        th.Thread.__init__(self)
        self._stop_event = th.Event()

    def stop(self):
        self._stop_event.set()
        
    def is_stopped(self):
        return self._stop_event.is_set()
        
    def run(self):
        while(not self.is_stopped()):
            self.buzz(100, self.duration, 90)
                
    def buzz(self, pitch, duration, DC):
        self.pwm.ChangeFrequency(pitch)
        self.pwm.start(DC)
        time.sleep(duration)
        self.pwm.stop()
        time.sleep(1)

def main():
    b = Buzzer(18, 100,0)
    b.run()
    #buzz(100, 5, 90, b)
    
if __name__ == '__main__':
    main()