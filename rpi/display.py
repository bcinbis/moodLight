'''
File that handles all operations dealing with the LED-matrix
'''
# Standard imports
import os
import sys
import time
import string
import fnmatch

# Add paths to matrix python modules
sys.path.append('rpi-rgb-led-matrix/bindings/python/rgbmatrix')
sys.path.append('rpi-rgb-led-matrix/bindings/python/samples')

# RPI and led matrix imports
from PIL import Image
from PIL import ImageDraw
from rgbmatrix import graphics
from samplebase import SampleBase
from rgbmatrix import graphics, RGBMatrixOptions, RGBMatrix


class Display:
    '''
    Description: Basic superclass that contains the general startup procedures for the LED matrix
    '''
    def __init__(self):
        
        # Configuration for the matrix
        options = RGBMatrixOptions()
        options.rows = 32
        options.cols = 32
        options.chain_length = 1
        options.parallel = 1
        options.gpio_slowdown = 5
        options.hardware_mapping = 'adafruit-hat' 

        # Enter in the hardware configurations
        self.matrix = RGBMatrix(options = options)

        # Specifications for Font style of text
        self.font = graphics.Font()
        self.font.LoadFont("rpi-rgb-led-matrix/fonts/7x13.bdf")


class codeDisplay(Display):
    '''
    This Display is used when the program is initially started. It is where the user can enter their 3-digit
    code for the gathering they are attending.
    '''
    def __init__(self):
        super().__init__()

        # Variables used to display the possible code that the user has displayed
        self.chars = ['_']
        self.chars += list(string.ascii_lowercase)
        self.str = ''
        self.STR = ''
        self.done = False
        red = graphics.Color(255,0,0)
        graphics.DrawText(self.matrix, self.font, 2, 10, red, "Code")

    # Update led matrix with current selection of letters
    def printStr(self):
        self.matrix.Clear()
        red = graphics.Color(255,0,0)
        green = graphics.Color(0,255,0)
        graphics.DrawText(self.matrix, self.font, 2, 10, red, "Code")
        graphics.DrawText(self.matrix, self.font, 2, 20, green, self.str)

    # Where index is updated through button presses in main,
    # This allows for cycling through all of the alphabet
    def sendIndex(self, index):
        self.str =  self.STR + self.chars[index]
        self.printStr()

    # Signifies that the enter button has been pressed
    def enter(self):
        self.STR = self.str
        if len(self.STR) == 3:
            self.done = True
        

class imgDisplay(Display):
    '''
    This Display is used after a user joined the gathering and the client has downloaded all of the pictures
    that the event has. Now the user can cycle through which picture they would like to display at any time
    '''
    def __init__(self):
        super().__init__()

        # Load all image names 
        self.image  = ''
        self.index = 0
        self.files = []
        for f in os.listdir("img"):
            if fnmatch.fnmatch(f, '*.jpg'):
                self.files.append(f)
        self.len = len(self.files)

    # Print the current selected image to the LED matrix
    def printImage(self):
        self.matrix.Clear()
        self.image = Image.open('./img/'+self.files[self.index])
        self.image.thumbnail((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
        self.matrix.SetImage(self.image.convert('RGB'))

    # Update which image is selected, occurs after button presses
    def sendIndex(self, ind):
        self.index = ind
        self.printImage()

