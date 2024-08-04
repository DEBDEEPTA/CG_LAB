import cv2
import numpy as np

# Define the dimensions of the canvas
w = 500     # CANVAS WIDTH
h = 500     # CANVAS HEIGHT

# Create a blank canvas
canvas = np.ones((h, w, 3), dtype=np.uint8) * 255
#                                           * 255 TO SET BACKGROUND WHITE
# DEFINE A SQUARE OBJECT
obj_points = np.array([[100, 100], [200, 100], [200, 200], [100, 200]], dtype=np.int32)

# TRANSFORMATION MATRICES(3 MATRICES)
TM = np.float32([[1, 0, 100], [0, 1, 50]])       # TRANSLATION MATRIK
RM = cv2.getRotationMatrix2D((150, 150), 45, 1)  # ROTATION MATRIX
SM = np.float32([[1.5, 0, 0], [0, 1.5, 0]])      # SCALING MATRIX

# DEFINING TRANSFORMATIONS ( 3 TYPES)
#             1) TRANSLATE
#             2) ROTATE
#             3) SCALE
translated_obj = np.array(
    [
        np.dot(TM, [x, y, 1])
        [:2]
        for x, y in obj_points
    ], dtype=np.int32)

rotated_obj = np.array(
    [
        np.dot(RM, [x, y, 1])
        [:2]
        for x, y in translated_obj
    ], dtype=np.int32)
scaled_obj = np.array(
    [
        np.dot(SM, [x, y, 1])
        [:2]
        for x, y in rotated_obj
    ], dtype=np.int32)


# Draw the objects on the canvas
cv2.polylines(canvas, [obj_points], True, (0, 0, 0), 2)
cv2.polylines(canvas, [translated_obj], True, (0, 255, 0), 2)
cv2.polylines(canvas, [rotated_obj], True, (255, 0, 0), 2)
cv2.polylines(canvas, [scaled_obj], True, (0, 0, 255), 2)
# Display the canvas
cv2.imshow("2D Transformations", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

