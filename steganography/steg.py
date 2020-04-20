import binascii as askey # ascii library // didnt actually use this 
from matplotlib import image as mpimg
from matplotlib import pyplot as plt


message = 'type message here' # type message (must be string for the thing to encode correctly )



print(bin(int.from_bytes(message.encode(), 'big'))) # makes it into a 

# read in an image file using matplotlib
image = mpimg.imread('Emily.png')
print(image) # look at the RGB values 
# plt.imshow(image)
# plt.show()
