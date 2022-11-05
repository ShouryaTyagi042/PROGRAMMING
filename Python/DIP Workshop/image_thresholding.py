import cv2

# THRESHOLD VALUE FUNCTION


def threshold(img, threshold_value):
    for i in range(len(img)):
        for j in range(len(img[0])):
            if (img[i][j] > threshold_value):
                img[i][j] = 255
            else:
                img[i][j] = 0


img_path = "Python/DIP Workshop/images/book_page.jpg"
img = cv2.imread(img_path)
# cv2.imshow("img", img)

# CONVERTING IMAGE TO GRAYSCALE
gray_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("grayscale", gray_scale_img)

# THRESHOLD FUNCTION
thresh_val, thresh_img = cv2.threshold(
    gray_scale_img, 200, 255, cv2.THRESH_OTSU)
cv2.imshow("thresh", thresh_img)

# USING DEFINED FUNCTION
# threshold(gray_scale_img, 127)
# cv2.imshow("threshold", gray_scale_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
