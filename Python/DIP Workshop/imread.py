import cv2
import numpy as np
img_path = "Python/DIP Workshop/images/sherlock_kid.png"
img = cv2.imread(img_path)
img_shape = img.shape
cv2.imshow("Image", img)
print(img)

# image is in bgr format in opencv


# GRAY IMAGE
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("GrayImage", img_gray)
# print(img_gray.shape)

# HSV IMAGE
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow("HSVimage", img_hsv)

# RESISZE IMAGE
img_resized = cv2.resize(img, (500, 500))
# cv2.imshow("ResizedImage", img_resized)

# CROPPING IMAGE
img_cropped = img[0:400, 350:760]
# cv2.imshow("CroppedImage", img_cropped)

# WHITE IMAGE
white_image = np.full(img_shape, 255, dtype=np.uint8)
print(white_image)
# cv2.imshow("white", white_image)

# NEGATIVE IMAGE
img_negative = np.subtract(white_image, img)
# cv2.imshow("negative", img_negative)

# RED IMAGE TASK


# cv2.imwrite("Python/DIP Workshop/images/sherlock_hsv.png", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
