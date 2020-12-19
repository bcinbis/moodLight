from display import codeDisplay, imgDisplay
from client import Client
import client
import RPi.GPIO as GPIO
import time
import fnmatch
import os

#variables for codeDisplay
LENGTH = 27
oldIndex = 0
newIndex = 0
enter = False
#button19 is for scrolling
#button18 is for enter

#variables for imgDisplay
nIndex = 0
oIndex = 0
imgNum = 0
esc = False
#both buttons move through the different images
#hold either button for 4 seconds to leave the party


#flag to signify switch from codeD to imgD
flag = True



def button19_callback(channel):
    global flag
    if flag: 
        time.sleep(.5)
        print('button19')
        global newIndex
        global LENGTH

        while(GPIO.input(19) == GPIO.HIGH):
            pass
        newIndex += 1

        if newIndex == LENGTH:
            newIndex = 0

    else:
        global nIndex
        global imgNum
        global esc

        start = time.perf_counter()
        while(GPIO.input(19) == GPIO.HIGH):
            pass
        stop = time.perf_counter()

        if (stop - start) > 4:
            esc = True
            return

        nIndex += 1
        if nIndex == imgNum:
            nIndex = 0
    

def button18_callback(channel):
    global flag
    if flag:    
        time.sleep(.5)
        print('button18')
        global enter
        global newIndex

        while(GPIO.input(18) == GPIO.HIGH):
            pass

        enter = True
        newIndex = 0

    else:
        global nIndex
        global imgNum
        global esc

        start = time.perf_counter()
        while(GPIO.input(19) == GPIO.HIGH):
            pass
        stop = time.perf_counter()

        if (stop - start) > 4:
            esc = True
            return
        
        nIndex -= 1
        if nIndex == -1:
            nIndex = imgNum -1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(19, GPIO.RISING, callback=button19_callback, bouncetime=400)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(18, GPIO.RISING, callback=button18_callback, bouncetime=400)



if __name__ == '__main__':
    # #joining a social gathering
    # disp = codeDisplay()
    # while not disp.done:
    #     if enter:
    #         disp.enter()
    #         enter = False
    #     if oldIndex != newIndex:
    #         disp.sendIndex(newIndex)
    #         oldIndex = newIndex
    # code = disp.STR
    flag = False
    # cli = Client(code)
    # #instert all client code

    #changing the displayed image
    disp = imgDisplay()
    imgNum = disp.len
    while not esc:
        if oIndex != nIndex:
            disp.sendIndex(nIndex)
            oIndex = nIndex
    time.sleep(2)
    del disp
    files = []
    for f in os.listdir("testImg"):
        if fnmatch.fnmatch(f, '*.jpg'):
            files.append(f)
    for f in files:
            os.remove('./testImg/'+f)
    time.sleep(2)
    sys.exit(0)