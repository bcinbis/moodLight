import sys
import string
# add paths to matrix python modules
sys.path.append('rpi-rgb-led-matrix/bindings/python/rgbmatrix')
sys.path.append('rpi-rgb-led-matrix/bindings/python/samples')

from PIL import Image
from PIL import ImageDraw
from rgbmatrix import graphics
from samplebase import SampleBase
from rgbmatrix import graphics, RGBMatrixOptions, RGBMatrix
import time

class Display():
    def __init__(self):
        # Configuration for the matrix
        options = RGBMatrixOptions()
        options.rows = 32
        options.cols = 32
        options.chain_length = 1
        options.parallel = 1
        options.gpio_slowdown = 5
        options.hardware_mapping = 'adafruit-hat' 

        self.matrix = RGBMatrix(options = options)

        self.font = graphics.Font()
        self.font.LoadFont("rpi-rgb-led-matrix/fonts/7x13.bdf")


        #initializing code entering procedures
        #self.pos = 0
        self.chars = [' ']
        self.chars += list(string.ascii_lowercase)
        self.str = ''
        self.STR = ''
        self.done = False


    def printStr(self):
        green = graphics.Color(0,255,0)
        graphics.DrawText(self.matrix, font, 2, 10, green, self.str)

    def sendIndex(self, index):
        self.str =  self.STR + self.chars[index]
        self.printStr()

    def enter(self):
        self.STR = self.str
        if len(self.STR) == 3:
            self.done = True
        #self.pos +=1
        






# Main function
if __name__ == "__main__":
    # Configuration for the matrix
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 32
    options.chain_length = 1
    options.parallel = 1
    options.gpio_slowdown = 5
    options.hardware_mapping = 'adafruit-hat'

    matrix = RGBMatrix(options = options)

    font = graphics.Font()
    font.LoadFont("rpi-rgb-led-matrix/fonts/7x13.bdf")

    COLORS = {
        "red": [255, 0, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255]
    }

    image = Image.open("./img/green light.jpg")
    # Make image fit our screen.
    image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

    matrix.SetImage(image.convert('RGB'))

    try:
        print("Press CTRL-C to stop.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)