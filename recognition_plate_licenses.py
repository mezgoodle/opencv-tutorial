import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as plt

image = cv2.imread('images/license.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(image_filter, 30, 200)

plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.show()
