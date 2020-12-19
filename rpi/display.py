import os
import sys
import string
import fnmatch
# add paths to matrix python modules
sys.path.append('rpi-rgb-led-matrix/bindings/python/rgbmatrix')
sys.path.append('rpi-rgb-led-matrix/bindings/python/samples')

from PIL import Image
from PIL import ImageDraw
from rgbmatrix import graphics
from samplebase import SampleBase
from rgbmatrix import graphics, RGBMatrixOptions, RGBMatrix
import time

class Display:
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


class codeDisplay(Display):
    def __init__(self):
        super().__init__()
        #initializing code entering procedures
        #self.pos = 0
        self.chars = ['_']
        self.chars += list(string.ascii_lowercase)
        self.str = ''
        self.STR = ''
        self.done = False

    def printStr(self):
        self.matrix.Clear()
        green = graphics.Color(0,255,0)
        graphics.DrawText(self.matrix, self.font, 2, 10, green, self.str)

    def sendIndex(self, index):
        self.str =  self.STR + self.chars[index]
        self.printStr()

    def enter(self):
        self.STR = self.str
        if len(self.STR) == 3:
            self.done = True
        #self.pos +=1
        
class imgDisplay(Display):
    def __init__(self):
        super().__init__()

        #load all image names
        self.image  = ''
        self.index = 0
        self.files = []
        for f in os.listdir("testImg"):
            if fnmatch.fnmatch(f, '*.jpg'):
                self.files.append(f)
        self.len = len(self.files)

    def printImage(self):
        self.image = Image.open('./testImg/'+self.files[self.index])
        self.image.thumbnail((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
        self.matrix.SetImage(self.image.convert('RGB'))

    def sendIndex(self, ind):
        self.index = ind
        self.printImage()

    def __del__(self):
        for f in self.files:
            os.remove('./testImg/'+f)







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