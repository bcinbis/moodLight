# Local imports from our files
from display import codeDisplay, imgDisplay
from client import Client
import client

# RPI pins import
import RPi.GPIO as GPIO

# Standard imports
import time
import fnmatch
import os
import sys

# Variables for codeDisplay
LENGTH = 27
oldIndex = 0
newIndex = 0
enter = False
# Button19 is for scrolling
# Button18 is an enter key

# Variables for imgDisplay
nIndex = 0
oIndex = 0
imgNum = 0
esc = False
# Both buttons move through the different images
# Hold either button for 4 seconds to leave the party

# Flag to signify switch from codeD to imgD
flag = True


def button19_callback(channel):
    global flag
    '''
    IF statement: Callback for button 19 during codeDisplay
    Action: increases index (cycling back to 0 when max length is reached), index is sent (via main) 
    to the led matrix where it controlls which ascii character (a to z) is currently selected
    '''
    if flag: 
        time.sleep(.5)
        print('button19')
        global newIndex
        global LENGTH

        # Button Debounceing
        while(GPIO.input(19) == GPIO.HIGH):
            pass
        
        # Adjust index
        newIndex += 1
        if newIndex == LENGTH:
            newIndex = 0

    else:
        '''
        Else Satement: Callback during imgDisplay
        Action 1: changes index, which is sent to imgDisplay (via main) which changes the image currently displayed on led matrix
        Action 2: Hold down the button for more than 4 seconds and this will begin the ending sequence of the program
        '''
        global nIndex
        global imgNum
        global esc
        time.sleep(.5)

        # Track amount of time that button is held
        start = time.perf_counter()
        while(GPIO.input(19) == GPIO.HIGH):
            pass
        stop = time.perf_counter()

        # Checks to see if button was held for more than 4 seconds
        if (stop - start) > 4:
            esc = True
            return

        # Adjust Index
        nIndex += 1
        if nIndex == imgNum:
            nIndex = 0
    

def button18_callback(channel):
    global flag
    '''
    IF Statement: Callback for button 18 during codeDisplay
    Action: Works as an enter button. When it is pressed, it sends an enter code to the codeDisplay instance
    (via main) to signify that the ascii selected is part of the code the user is trying to enter
    '''
    if flag:    
        time.sleep(.5)
        print('button18')
        global enter
        global newIndex

        # Button Debouncing
        while(GPIO.input(18) == GPIO.HIGH):
            pass

        # Enter was pressed
        enter = True
        newIndex = 0

    
    else:
        '''
        Else Satement: Callback during imgDisplay
        Action 1: changes index, which is sent to imgDisplay (via main) which changes the image currently displayed on led matrix
        Action 2: Hold down the button for more than 4 seconds and this will begin the ending sequence of the program
        '''
        global nIndex
        global imgNum
        global esc
        time.sleep(.5)
        
        # Track amount of time that button is held
        start = time.perf_counter()
        while(GPIO.input(19) == GPIO.HIGH):
            pass
        stop = time.perf_counter()

        # Checks to see if button was held for more than 4 seconds
        if (stop - start) > 4:
            esc = True
            return
        
        # Adjust index
        nIndex -= 1
        if nIndex == -1:
            nIndex = imgNum -1

# Setting up interrupts for the buttons
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(19, GPIO.RISING, callback=button19_callback, bouncetime=400)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(18, GPIO.RISING, callback=button18_callback, bouncetime=400)


def cleanup():
    '''
    Ensures that user only has images from their respective gathering
    Action: This removes previous files from a past social gathering
    '''
    files = []
    for f in os.listdir("img"):
        if fnmatch.fnmatch(f, '*.jpg'):
            files.append(f)
    for f in files:
            os.remove('./img/'+f)



if __name__ == '__main__':
    SERVER = '35.239.118.105:4200'

    # Free up any storage 
    cleanup()

    # Enter your code for the gathering you are attending
    disp = codeDisplay()
    while not disp.done:
        if enter:
            disp.enter()
            enter = False
        if oldIndex != newIndex:
            disp.sendIndex(newIndex)
            oldIndex = newIndex
    code = disp.STR # code is retrieved here
    flag = False # adjust button callbacks to deal with seacond display
    
    # Insert all client code
    client = Client(SERVER)
    urls = client.getImageUrls(code)
    client.downloadImages(urls)

    # User can begin cycling through and choosing which image to display
    disp = imgDisplay()
    imgNum = disp.len
    while not esc:
        if oIndex != nIndex:
            disp.sendIndex(nIndex)
            oIndex = nIndex
    
    # Ending/shutdown sequence
    del disp
    time.sleep(2)
    sys.exit(0)