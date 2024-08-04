        # 1. READ ORIGINIAL_IMAGE
        # 2. CONVERT - ORIGINAL_IMG -->GRAY_SCALE-->BINARY_IMG
        # 3. DRAWING CONTOUR ON THE ORIGINAL IMAGE
import cv2
#Read the image and convert it to grayscale
image = cv2.imread('image.jpg')

# ORIGINAL_IMG -->GRAY_SCALE-->BINARY_IMG
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                               # ORIGINAL_IMG -->GRAY_SCALE
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) # GRAY_SCALE-->BINARY_IMG

#Now detect the contours
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# draw contours on the original image
image_copy = image.copy()    # APPLYING CONTOUR ON A COPY OF ORIGINAL IMAGE
image_copy = cv2.drawContours(image_copy, contours, -1, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

#Visualizing the results
cv2.imshow('ORIGINAL IMAGE', image)
cv2.imshow('CONTOURED IMAGE', image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()






