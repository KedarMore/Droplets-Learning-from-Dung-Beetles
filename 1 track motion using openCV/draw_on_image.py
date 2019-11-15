import cv2
import numpy as np

##########################################################################################
image = cv2.imread('0.jpg')

r = 200.0 / image.shape[1]
dim = (200, int(image.shape[0] * r))

# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

        # define range of white color in HSV
        # change it according to your need !
lower_white = np.array([50,0,0], dtype=np.uint8)
upper_white = np.array([179,255,255], dtype=np.uint8)

        # Threshold the HSV image to get only white colors
mask = cv2.inRange(hsv, lower_white, upper_white)
        # Bitwise-AND mask and original image
res = cv2.bitwise_and(resized,resized, mask= mask)

#cv2.imshow('frame',resized)
#cv2.imshow('mask',mask)
#cv2.imshow('res',res)
##########################################################################################

#img = cv2.imread('Untitled.jpg',cv2.IMREAD_GRAYSCALE)
_,img = cv2.threshold(mask,127,255,cv2.THRESH_OTSU)
h, w = img.shape[:2]

contours0, hierarchy = cv2.findContours( img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
moments  = [cv2.moments(cnt) for cnt in contours0]
# Nota Bene: I rounded the centroids to integer.
centroids = [( int(round(m['m10']/m['m00'])),int(round(m['m01']/m['m00'])) ) for m in moments]

print ('cv2 version:', cv2.__version__)
print ('centroids:', centroids)

for c in centroids:
    # I draw a black little empty circle in the centroid position
    cv2.circle(img,c,5,(0,0,0),-1)

cv2.imshow('image', img)
0xFF & cv2.waitKey()
cv2.destroyAllWindows()
