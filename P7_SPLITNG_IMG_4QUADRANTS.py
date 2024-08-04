import cv2
image = cv2.imread("image.jpg")
(h, w) = image.shape[:2]

cX, cY = (w // 2), (h // 2)

topLeft = image[0:cY, 0:cX]
topRight = image[0:cY, cX:w]
bottomLeft = image[cY:h, 0:cX]
bottomRight = image[cY:h, cX:w]

cv2.imshow("Top left corner", topLeft)
cv2.imshow("Top right corner", topRight)
cv2.imshow("Bottom left corner", bottomLeft)
cv2.imshow("Bottom right corner", bottomRight)

cv2.imshow("original Image", image)
cv2.waitKey(0)