import sys
# add paths to matrix python modules
sys.path.append('rpi-rgb-led-matrix/bindings/python/rgbmatrix')
sys.path.append('rpi-rgb-led-matrix/bindings/python/samples')

from PIL import Image
from PIL import ImageDraw
from samplebase import SampleBase
from rgbmatrix import graphics, RGBMatrixOptions, RGBMatrix
import time

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

    red = graphics.Color(255, 0, 0)
    green = graphics.Color(0, 255, 0)
    blue = graphics.Color(0, 0, 255)

    COLORS = {
        "red": [255, 0, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255]
    }

    for x in range(0, matrix.width):
        for y in range(0, matrix.height):
            matrix.SetPixel(x, y, 0, 0, 0)

    image = Image.open("./dont enter.jpg")
    # Make image fit our screen.
    image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

    matrix.SetImage(image.convert('RGB'))

    try:
        print("Press CTRL-C to stop.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)