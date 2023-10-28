# import required libraries
import cv2
import numpy as np

# read input image
img = cv2.imread('Python/DIP Workshop/ImageOperation/MaskImage.jpg')
cv2.imshow("Original Image", img)
# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# define range of yellow color in HSV
lower_yellow = np.array([15, 50, 180])
upper_yellow = np.array([40, 255, 255])
# Create a mask. Threshold the HSV image to get only yellow colors
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
# Bitwise-AND mask and original image
result = cv2.bitwise_and(img, img, mask=mask)
# display the mask and masked image
cv2.imshow('Mask', mask)
cv2.imshow('Masked Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()