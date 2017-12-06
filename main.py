import hcsr04
import shapes

sensor=hcsr04.HCSR04(4,19)
dist=sensor.distance_cm()
