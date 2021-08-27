import cv2

image = cv2.imread('images/profile.jpg')

image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)

image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)

b, g, r = cv2.split(image)

cv2.imshow('Result', b)
cv2.waitKey(0)

