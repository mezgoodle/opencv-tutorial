import cv2

image = cv2.imread('images/profile.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('faces.xml')

results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

for (x, y, width, height) in results:
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 0, 255), thickness=2)

cv2.imshow('Result', image)
cv2.waitKey(0)

