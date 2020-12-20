import os
import glob
import fnmatch

class imgDisplay():
    def __init__(self):
        #super().__init__()

        files = []
        for f in os.listdir("img"):
            if fnmatch.fnmatch(f, '*.jpg'):
                files.append(f)

if __name__ == "__main__":
    x = imgDisplay()