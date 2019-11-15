
import cv2
import numpy as np

image = cv2.imread('real_image.jpeg')

r = 200.0 / image.shape[1]
dim = (200, int(image.shape[0] * r))
 
# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

        # define range of white color in HSV
        # change it according to your need !
lower_white = np.array([0,0,0], dtype=np.uint8)
upper_white = np.array([179,40,255], dtype=np.uint8)

        # Threshold the HSV image to get only white colors
mask = cv2.inRange(hsv, lower_white, upper_white)
        # Bitwise-AND mask and original image
res = cv2.bitwise_and(resized,resized, mask= mask)

cv2.imshow('frame',resized)
cv2.imshow('mask',mask)
cv2.imshow('res',res)




