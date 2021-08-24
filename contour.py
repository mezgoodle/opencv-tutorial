import cv2
import numpy as np

# How to show image
image = cv2.imread('images/profile.jpg')
new_image = np.zeros(image.shape, dtype='uint8')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (9, 9), 0)

image = cv2.Canny(image, 100, 140)

con, hir = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# print(con)

cv2.drawContours(new_image, con, -1, (230, 111, 148), 1)

cv2.imshow('Profile image', new_image)
cv2.waitKey(0)
