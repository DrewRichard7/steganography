from matplotlib import image as mpimg
from matplotlib import pyplot as plt
import numpy as np


message = 'a' # type message (must be string for the thing to encode correctly )
pictureFN = 'Emily.png'


binmsg = bin(int.from_bytes(message.encode(), 'big')) # makes it into a binary
binmsgar = np.array(binmsg)
binmsglst = np.ndarray.tolist(binmsgar)
#binmsglst = binmsglst.astype(np.float)

image = mpimg.imread(pictureFN) # read in an image file using matplotlib
# plt.imshow(image)
# plt.show()
image = image*255 # read in png file from folder
position = 1,1,2
binaryindex = 2

#print(type(image))  # look at the RGB values and get in terms of 0-255 range
#print(image[position])
#print(type(binmsgar))
#print(type(np.float(binmsglst[binaryindex])))
#print(np.float(binmsglst[binaryindex]))


if image[position] % 2 == 0:
    image[position] = 0
else:
    image[position] = 1
    
#print(image[position].item())
#print(type(image[position].item()))

if np.float(binmsglst[binaryindex]) == image[position].item():
    print('first is the same')
else:
    print('not the same')

