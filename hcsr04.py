from os import path
import time

gpio_root = '/sys/class/gpio'
gpiopath = lambda pin: path.join(gpio_root, 'gpio{0}'.format(pin))

class Pin():
    
    def __init__(self, number, direction):
        
        self.number = number
        
        if not path.isdir(gpiopath(number)):
            f = open(path.join(gpio_root, 'export'), 'w')
            f.write(str(number))
            f.flush()
            f.close()
            
        if path.exists(path.join(gpiopath(self.number), 'direction')):
            f = open(path.join(gpiopath(number), 'direction'), 'w')
            f.write(direction)
            f.flush()
            f.close()

    def write(self, v):
        if path.exists(path.join(gpiopath(self.number), 'value')):
            f = open(path.join(gpiopath(self.number), 'value'), 'w')
            f.write(str(v))
            f.flush()
            f.close()

    def read(self):
        f = open(path.join(gpiopath(self.number), 'value'), 'r')
        f.seek(0)
        value = f.read().strip()
        f.close()
        return value

class HCSR04():

    def __init__(self, trigger_pin, echo_pin, echo_timeout=0.02332):
        """
        trigger_pin: Pino de saída que manda os pulsos
        echo_pin: Pino de leitura para medir a distância.
        echo_timeout_us: Timeout em microsegundos para ler o valor do pino echo. 
        """
        self.echo_timeout = echo_timeout
        # Init trigger pin (out)
        self.trigger = Pin(trigger_pin, "out")
        self.trigger.write(0)

        # Init echo pin (in)
        self.echo = Pin(echo_pin, "in")

    def send_pulse(self):
        """
        Manda o trigger enviar um pulso e manda o echo ler.
        Então calculamos o tempo em microsegundos entre o momento que o pulso é
        enviado e momento que o echo ler o pulso.
        """
        self.trigger.write(0)
        time.sleep(1)
        self.trigger.write(1)
        time.sleep(0.00001)
        self.trigger.write(0)

        echo_end = 0
        echo_init = 0
        loop_init = time.time()
        while(self.echo.read() == '0'):
            #echo_init = time.time()
            if time.time() - loop_init > 0.1:
                break
            pass
        echo_init = time.time()


        while(self.echo.read() == '1'):
            #echo_end = time.time()
            pass
        echo_end = time.time()
        print("Inicio: " + str(echo_init))
        print("Fim: " + str(echo_end))
        delay = echo_end - echo_init
        print("Delay: " + str(delay))
        if delay <= self.echo_timeout:
            return delay
        else:
            return -1

    def distance_mm(self):
        """
        Retorna a distância em milímetros.
        """
        delay = self.send_pulse()
        if delay is -1:
            return -1
        else:        
            mm = delay * 171500
            return round(mm, 2)
        # To calculate the distance we get the pulse_time and divide it by 2 
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.34320 mm/us that is 1mm each 2.91us
        # pulse_time // 2 // 2.91 -> pulse_time // 5.82 -> pulse_time * 100 // 582 
        
    def distance_cm(self):
        """
        Retorna a distância em centmétros
        """
        delay = self.send_pulse()
        if delay is -1:
            return -1
        else:
            cm = delay * 17150
            return round(cm, 2)
        # To calculate the distance we get the pulse_time and divide it by 2 
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.034320 cm/us that is 1cm each 29.1us


        

def main():
    sensor = HCSR04(4, 19)
    while(True):
        print(sensor.distance_cm())
        time.sleep(0.1)

if __name__ == '__main__':
    main()
