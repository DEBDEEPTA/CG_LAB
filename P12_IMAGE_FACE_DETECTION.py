import cv2
# Load the cascade classifier (PRETRAINED MODEL FOR FACE DETECTION)
# download haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read the input image
img = cv2.imread("face_test.png")

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Save the output image
cv2.imwrite("output.jpg", img)



