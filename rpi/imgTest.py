import os
import glob

class imgDisplay():
    def __init__(self):
        #super().__init__()

        #load all images
        print('helo')
        files = [f for f in os.listdir("C:\Users\2019m\Desktop\petals\rpi") if os.path.isfile(f)]
        for f in files:
            print(f)

if __name__ == "__main__":
    x = imgDisplay()