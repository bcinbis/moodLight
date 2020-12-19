from display import Display
from client import Client
import client
import RPi.GPIO as GPIO
import time

LENGTH = 27
oldIndex = 0
newIndex = 0
enter = False
#button19 is for scrolling
#button18 is for enter

def button19_callback(channel):
    time.sleep(.5)
    print('button19')
    global newIndex
    global LENGTH
    while(GPIO.input(19) == GPIO.HIGH):
        pass
    newIndex += 1
    if newIndex == LENGTH:
        newIndex = 0

def button18_callback(channel):
    time.sleep(.5)
    print('button18')
    global enter
    while(GPIO.input(18) == GPIO.HIGH):
        pass
    enter = True
    newIndex = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(19, GPIO.RISING, callback=button19_callback, bouncetime=400)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(18, GPIO.RISING, callback=button18_callback, bouncetime=400)



def joinParty(code):
    pass




if __name__ == '__main__':
    disp = Display()
    while not disp.done:
        if enter:
            disp.enter()
            enter = False
        if oldIndex != newIndex:
            disp.sendIndex(newIndex)
            oldIndex = newIndex
    code = disp.STR
    cli = Client(code)