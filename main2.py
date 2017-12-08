
import buzzer
import hcsr04
import screen
from datetime import datetime
import time 
import numpy as np
import threading as th
import multiprocessing as mp


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
			p= buzzer.init_buzzer(12,100)
			print('ta aqui 1')
			bThread=th.Thread(target =buzzer.buzz, args =(100,5,90)) # Cria a thread e depois coloca-a numa lista de threads ativas
			bThread.start() # inicia 
			f[0] =255
			f[3] = 255
			f[6] = 255
			f[9] = 255
			nokia.print_bars(f)
		if 75 < dist1 <= 150:
			p= init_buzzer(12,100)
			print('ta aqui 2')
			bThread=th.Thread(target = buzz, args =(100,5,90)) # Cria a thread e depois coloca-a numa lista de threads ativas
			bThread.start() # inicia 
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
			p= init_buzzer(12,100)
			print('ta aqui 3')
			bThread=th.Thread(target = buzz, args =(100,5,90)) # Cria a thread e depois coloca-a numa lista de threads ativas
			bThread.start() # inicia 
			f[0] = 0
			f[3] = 0
			f[6] = 0
			f[9] = 0
			nokia.print_bars(f)
		#distance = str(min(dists)) + " cm	"
		print('vai comecar')
		distance= str(dist1)+ "cm"
		position = (20,10)
		nokia.write_text(distance, position)
		print('agora vai')
print("start")
main()
