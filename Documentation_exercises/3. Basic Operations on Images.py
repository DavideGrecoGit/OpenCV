import numpy as np
import cv2 as cv

img = cv.imread('image.jpg')

px = img[100,100]
print(px)

# accessing only blue pixel
blue = img[100,100,0]
print( blue )

# modify a single pixel 
# slow and discouraged.
img[100,100] = [255,255,255]
print( img[100,100] )

# Alternative: .item function
# accessing red value
img.item(10,10,2)

# modifying red value
img.itemset((10,10,2),255)
img.item(10,10,2)

# print properties

print( img.shape )

# number of pixels
print( img.size )

# type of the image
print( img.dtype )

# copy and pasting image regions
to_copy = img[120:200, 530:690]
img[273:353, 100:260] = to_copy

#cv.imshow("Display window", img)
#k = cv.waitKey(0)

#Split and merge channels
b,g,r = cv.split(img)
img = cv.merge((b,g,r))

#or
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

#setting all red pixels to 0
img[:,:,2] = 0

# adding a border
from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv.imread('image.jpg')

border_size = 100

replicate = cv.copyMakeBorder(img1,border_size,border_size,border_size,border_size,cv.BORDER_REPLICATE)
#Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
reflect = cv.copyMakeBorder(img1,border_size,border_size,border_size,border_size,cv.BORDER_REFLECT)
#Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
reflect101 = cv.copyMakeBorder(img1,border_size,border_size,border_size,border_size,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,border_size,border_size,border_size,border_size,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,border_size,border_size,border_size,border_size,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()