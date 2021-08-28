import cv2
import numpy as np

image = np.zeros((350, 350), dtype='uint8')

circle = cv2.circle(image.copy(), (0, 0), 80, 255, -1)
square = cv2.rectangle(image.copy(), (25, 25), (250, 350), 255, -1)

cv2.imshow('Result', circle)
cv2.waitKey(0)
