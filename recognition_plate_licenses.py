import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as plt

image = cv2.imread('images/license.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(image_filter, 30, 200)

contours = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:8]

position = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    number_of_edges = 4
    if len(approx) == number_of_edges:
        position = approx
        break

print(position)

plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.show()
