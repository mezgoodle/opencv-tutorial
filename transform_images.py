import cv2
import numpy as np

image = cv2.imread('images/profile.jpg')


# image = cv2.flip(image, 1)

def rotate(image, angle: int):
    height, width = image.shape[:2]
    point = (width // 2, height // 2)

    matrix = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(image, matrix, (width, height))


image = rotate(image, 90)


def transform(image, x, y):
    height, width = image.shape[:2]
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(image, matrix, (width, height))


image = transform(image, 30, 200)
cv2.imshow('Result', image)

cv2.waitKey(0)
