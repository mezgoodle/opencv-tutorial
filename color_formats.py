import cv2

image = cv2.imread('images/profile.jpg')

image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)

cv2.imshow('Result', image)
cv2.waitKey(0)

