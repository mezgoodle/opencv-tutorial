import cv2

# How to show image
image = cv2.imread('images/profile.jpg')
cv2.imshow('Profile image', image)

cv2.waitKey(0)

# How to show video
cap = cv2.VideoCapture('videos/path_to_video.mp4')

while True:
    success, image = cap.read()
    cv2.imshow('Result', image)

    if cv2.waitKey(1) and ord('q') == 0xFF:
        break
