import cv2
import numpy

#Loading image from memory
image = cv2.imread('image.jpg')

#Dfining matrices
matrix_translate = numpy.float32([[1,0,100],[0,1,100]])                # MATRIX FOR TRANSLATION
##############################
height, width = image.shape[:2]
matrix_rotate = cv2.getRotationMatrix2D((width/2,height/2), 10, 1)     # MATRIX FOR ROTATION

#Applying the matrices to the image
img_translated = cv2.warpAffine(image, matrix_translate, (image.shape[1]+100,image.shape[0]+100))  # TRANSLATION
img_rotation = cv2.warpAffine(image, matrix_rotate, (width, height))                               # ROTATION
##################################
img_scaling = cv2.resize(image, None, fx=0.5,fy=0.5, interpolation=cv2.INTER_LINEAR)               # SCALING

#Showing the image
cv2.imshow('IMAGE TRANSLATION', img_translated)
cv2.imshow("IMAGE ROTATION",img_rotation)
cv2.imshow("IMAGE SCALING",img_scaling)
cv2.waitKey()

