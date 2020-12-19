import os
import glob
import fnmatch

class imgDisplay():
    def __init__(self):
        #super().__init__()

        files = [f for f in os.listdir("img")]
        for f in files:
            if fnmatch.fnmatch(f, '*.jpg'):
                print(f)

if __name__ == "__main__":
    x = imgDisplay()