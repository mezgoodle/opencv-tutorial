import cv2
import numpy as np

image = cv2.imread('images/profile.jpg')

image = cv2.flip(image, 1)
cv2.imshow('Result', image)

cv2.waitKey(0)
