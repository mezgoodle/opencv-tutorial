import cv2

image = cv2.imread('images/profile.jpg')
cv2.imshow('Profile image', image)

cv2.waitKey(0)
