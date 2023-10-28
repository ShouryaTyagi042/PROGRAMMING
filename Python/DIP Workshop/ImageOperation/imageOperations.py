import numpy as np
import cv2

# Accessing the image properties
# print(img.shape)
# print(img.size)
# print(img.dtype)


img = cv2.imread("Python/DIP Workshop/ImageOperation/RedColor.png")

# Accessing the pixel

cv2.imshow("original", img)
px = img[100, 100]
print(px)

# # Modifying the pixel
# img[100, 100] = [255, 0, 0]
# updatedPx = img[100, 100]
# print(updatedPx)
# img[0:200, 0:400] = [255, 0, 0]
# cv2.imshow("Updated", img)


# loading the image

# Setting the font and font color
# font = cv2.FONT_HERSHEY_SIMPLEX
# white = (255, 255, 255)
# cv2.putText(img, "Red Color Image",
#             (100, 100), font, 4, white, 4)
# cv2.imshow("updated", img)
# (name_image, text,coordinates for the text,
# font_type, font_scale,color,thickness)aq


# # Cropping the image
# croppedImage = img[0:600, 0:600]
# cv2.imshow("Cropped Image", croppedImage)


cv2.waitKey(0)
cv2.destroyAllWindows()
