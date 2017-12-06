import hcsr04
import screen
from datetime import datetime
import time 
import numpy as np

def main():
    
    sensor1 = hcsr04.HCSR04(4,19)
    sensor2 = hcsr04.HCSR04(16,26)
    nokia = screen.Screen()
    f = 255*np.ones(12)
    nokia.print_bars(f)

    while(True):
        dists = []
        dist1 = sensor1.distance_cm()
        now = datetime.now()
        clock = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        position = (20,0)
        nokia.write_text(clock, position)
        
        if dist1 != -1:
            dists.append(dist1)
            
        if 150 < dist1:
            f[0] = 255
            f[3] = 255
            f[6] = 255
            f[9] = 255
            nokia.print_bars(f)
        if 75 < dist1 <= 150:
            f[0] = 0
            f[3] = 255
            f[6] = 255
            f[9] = 255
            nokia.print_bars(f)
        if 50 < dist1 <= 75:
            f[0] = 0
            f[3] = 0
            f[6] = 255
            f[9] = 255
            nokia.print_bars(f)
        if 25 < dist1 <= 50:
            f[0] = 0
            f[3] = 0
            f[6] = 0
            f[9] = 255
            nokia.print_bars(f)
        if 0 < dist1 < 25:
            f[0] = 0
            f[3] = 0
            f[6] = 0
            f[9] = 0
            nokia.print_bars(f)

        dist2 = sensor2.distance_cm()
        if 150 < dist2:
            f[1] = 255
            f[4] = 255
            f[7] = 255
            f[10] = 255
            nokia.print_bars(f)
        if 75 < dist2 <= 150:
            f[1] = 0
            f[4] = 255
            f[7] = 255
            f[10] = 255
            nokia.print_bars(f)
        if 50 < dist2 <= 75:
            f[1] = 0
            f[4] = 0
            f[7] = 255
            f[10] = 255
            nokia.print_bars(f)
        if 25 < dist2 <= 50:
            f[1] = 0
            f[4] = 0
            f[7] = 0
            f[10] = 255
            nokia.print_bars(f)
        if 0 < dist2 < 25:
            f[1] = 0
            f[4] = 0
            f[7] = 0
            f[10] = 0
            nokia.print_bars(f)

        if dist2 != -1:
            dists.append(dist2)
            
        distance = str(min(dists)) + " cm"
        position = (20,10)
        nokia.write_text(distance, position)
        

main()
