import binascii as askey # ascii library // didnt actually use this 
from matplotlib import image as mpimg
from matplotlib import pyplot as plt


message = 'type message here' # type message (must be string for the thing to encode correctly )
pictureFN = 'Emily.png'


# print(bin(int.from_bytes(message.encode(), 'big'))) # makes it into a 

# read in an image file using matplotlib
image = mpimg.imread(pictureFN)
# plt.imshow(image)
# plt.show()

image = image*255  # read in png file from folder
# print(image)  # look at the RGB values and get in terms of 0-255 range


firstpixel = image[1,1]
print(firstpixel)
