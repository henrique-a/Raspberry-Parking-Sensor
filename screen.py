# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import time,numpy as np

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Screen:
        
        def __init__(self):
                SPI_PORT = 0
                SPI_DEVICE = 0
                SCLK = 4
                DIN = 17
                DC = 23
                RST = 24
                CS = 8
                # Hardware SPI usage:
                self.disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

                # Software SPI usage (defaults to bit-bang SPI interface):
                #disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)
                
                # Load default font.
                # Alternatively load a TTF font.
                # Some nice fonts to try: http://www.dafont.com/bitmap.php
                # self.font = ImageFont.truetype('arial.ttf', 8)

                self.font = ImageFont.load_default()
                
                # Initialize library.
                self.disp.begin(contrast=30)

                # Clear display.
                #disp.clear()
                self.disp.display()

                # Create blank image for drawing.
                # Make sure to create image with mode '1' for 1-bit color.
                self.image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

                # Get drawing object to draw on image.
                self.draw = ImageDraw.Draw(self.image)

                # Draw a white filled box to clear the image.
                self.draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

                f = 255*np.ones(12)
                self.print_bars(f)
        

        def print_bars(self, f):
                
                # Inicializa os retângulos de indicação
                # Ultima linha
                self.draw.rectangle((1,42,27,47), outline = 0, fill=int(f[0]))
                self.draw.rectangle((29,42,55,47), outline = 0, fill=int(f[1]))
                self.draw.rectangle((57,42,83,47), outline = 0, fill=int(f[2]))
                # Penultima linha
                self.draw.rectangle((3,35,25,40), outline = 0, fill=int(f[3]))
                self.draw.rectangle((31,35,53,40), outline = 0, fill=int(f[4]))
                self.draw.rectangle((59,35,81,40), outline = 0, fill=int(f[5]))
                #Antepenúltima Linha
                self.draw.rectangle((5,28,23,33), outline = 0, fill=int(f[6]))
                self.draw.rectangle((33,28,51,33), outline = 0, fill=int(f[7]))
                self.draw.rectangle((61,28,79,33), outline = 0, fill=int(f[8]))
                #Primeira linha
                self.draw.rectangle((7,21,21,26), outline = 0, fill=int(f[9]))
                self.draw.rectangle((35,21,49,26), outline = 0, fill=int(f[10]))
                self.draw.rectangle((63,21,77,26), outline = 0, fill=int(f[11]))

                
                # Display image.
                self.disp.image(self.image)
                self.disp.display()

                #print('Press Ctrl-C to quit.')
                #while True:
                #time.sleep(1.0)

        
        # Write some text.
        def write_text(self, message, position):
                self.draw.rectangle((0,0,83,18), outline=255, fill=255)
                self.draw.text(position, message, font=self.font)


def main():	
        f=np.zeros(12)
        print(str(f[0]))
        init_nokia(f)
        f[0]=255
        init_nokia(f)

if __name__ == '__main':
        main()
