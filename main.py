import hcsr04
import screen
from datetime import datetime
import time 
import numpy as np

def main():
    
    sensor = hcsr04.HCSR04(4,19)
    nokia = screen.Screen()
    f = 255*np.ones(12)
    nokia.print_nokia(f)

    while(True):
        dist = sensor.distance_cm()
        #now = datetime.now()
        #clock = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        if dist != -1:
            distance = str(dist) + " cm" 
            nokia.write_text(distance)
        if 150 < dist:
            f[0] = 255
            f[3] = 255
            f[6] = 255
            f[9] = 255
            nokia.print_nokia(f)
        if 75 < dist <= 150:
            f[0] = 0
            f[3] = 255
            f[6] = 255
            f[9] = 255
            nokia.print_nokia(f)
        if 50 < dist <= 75:
            f[0] = 0
            f[3] = 0
            f[6] = 255
            f[9] = 255
            nokia.print_nokia(f)
        if 25 < dist <= 50:
            f[0] = 0
            f[3] = 0
            f[6] = 0
            f[9] = 255
            nokia.print_nokia(f)
        if 0 < dist < 25:
            f[0] = 0
            f[3] = 0
            f[6] = 0
            f[9] = 0
            nokia.print_nokia(f)

main()
