import cv2
import numpy as np

# How to show image
image = cv2.imread('images/profile.jpg')
new_image = cv2.resize(image, (300, 500))
new_image = cv2.GaussianBlur(new_image, (9, 9), 0)
new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
new_image = cv2.Canny(new_image, 200, 200)
kernel = np.ones((5, 5), np.uint8)
new_image = cv2.dilate(new_image, kernel, iterations=1)
new_image = cv2.erode(new_image, kernel, iterations=1)
cv2.imshow('Profile image', image)
cv2.imshow('Profile image', new_image[0:100, 0:150])

# print(image.shape)

cv2.waitKey(0)

# How to show video
cap = cv2.VideoCapture('videos/path_to_video.mp4')
cap.set(3, 500)
cap.set(4, 300)
cap2 = cv2.VideoCapture(0)  # Show video from camera

while True:
    success, image = cap.read()
    cv2.imshow('Result', image)

    if cv2.waitKey(1) and ord('q') == 0xFF:
        break

# Create image from matrix
photo = np.zeros((450, 450, 3), dtype='uint8')
# RGB = BGR
photo[:] = 255, 0, 0
# Create rectangle
cv2.rectangle(photo, (0, 0), (100, 100), (119, 201, 105), thickness=cv2.FILLED)
# Create line
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (119, 201, 105), thickness=3)
cv2.imshow('Photo', photo)
cv2.waitKey(0)

