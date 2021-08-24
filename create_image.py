import numpy as np
import cv2

# Create image from matrix
photo = np.zeros((450, 450, 3), dtype='uint8')
# RGB = BGR
photo[:] = 255, 0, 0
# Create rectangle
cv2.rectangle(photo, (0, 0), (100, 100), (119, 201, 105), thickness=cv2.FILLED)
# Create line
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (119, 201, 105), thickness=3)
# Create circle
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (119, 201, 105), thickness=2)
# Create text
cv2.putText(photo, 'Mezidia', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1., (255, 0, 0), 4)
cv2.imshow('Photo', photo)
cv2.waitKey(0)
