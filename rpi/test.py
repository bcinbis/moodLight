import RPi.GPIO as GPIO
import time

count = 0

def button_callback(channel):
    time.sleep(.5)
    global count
    while(GPIO.input(19) == GPIO.HIGH):
        pass
    count += 1
    print("pressed "+str(count))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(19, GPIO.RISING, callback=button_callback)

message = input('enter: ')

GPIO.cleanup()
from PIL import Image
from PIL import ImageDraw
from numpy import asarray

image = Image.open("./do_not_enter.jpg")
image.thumbnail((32, 32), Image.ANTIALIAS)
image.convert('RGB').show()

numpydata = asarray(image)

# <class 'numpy.ndarray'> 
print(type(numpydata)) 
  
#  shape 
print(numpydata) 
