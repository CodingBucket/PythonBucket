# This program detects face and eye using Open CV

# pip install opencv-python

import cv2

# Haar Classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Read image
image = cv2.imread('new-year.jpg')
faces = face_cascade.detectMultiScale(image, 1.3, 5)

print('Faces found: ', len(faces))
print('The image height, width, and channel: ', image.shape)
print('The coordinates of each face detected: ', faces)

# Loop over all coordinates faces and draw rectangles
for (x,y,w,h) in faces:
    # Draw face detection
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
    # Draw eye detection
    roi_face = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_face, 1.3, 5)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_face, (ex,ey), (ex+ew, ey+eh), (255, 0, 0), 2)

# Show image
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindow()