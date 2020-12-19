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