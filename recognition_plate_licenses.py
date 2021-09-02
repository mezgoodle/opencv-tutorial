import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as plt

image = cv2.imread('images/license.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
