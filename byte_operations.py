import cv2
import numpy as np

photo = cv2.imread('images/profile.jpg')
image = np.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(image.copy(), (200, 300), 120, 255, -1)
square = cv2.rectangle(image.copy(), (25, 25), (250, 350), 255, -1)

image = cv2.bitwise_and(photo, photo, mask=circle)
# image = cv2.bitwise_or(circle, square)
# image = cv2.bitwise_xor(circle, square)
# image = cv2.bitwise_not(circle)

cv2.imshow('Result', image)
cv2.waitKey(0)
