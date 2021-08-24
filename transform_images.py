import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')

while True:
    success, image = cap.read()

    new_image = cv2.resize(image, (300, 500))
    new_image = cv2.GaussianBlur(new_image, (9, 9), 0)
    new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    new_image = cv2.Canny(new_image, 100, 100)
    kernel = np.ones((5, 5), np.uint8)
    new_image = cv2.dilate(new_image, kernel, iterations=1)
    new_image = cv2.erode(new_image, kernel, iterations=1)
    cv2.imshow('Profile image', image)
    cv2.imshow('Profile image', new_image[0:100, 0:150])

    cv2.imshow('Result', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
