import cv2

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
