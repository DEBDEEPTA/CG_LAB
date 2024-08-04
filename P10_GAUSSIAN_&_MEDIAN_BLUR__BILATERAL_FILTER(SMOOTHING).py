import cv2
img = cv2.imread("image.jpg") # READING THE IMAGE
g_blur = cv2.GaussianBlur(img,(5,5),0)
m_blur = cv2.medianBlur(img,5)
m_bl_filter = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("ORIGINAl IMAGE",img)
cv2.imshow("GAUSSIAN BLUR",g_blur)
cv2.imshow("MEDIAN BLUR",m_blur)
cv2.imshow("IMAGE SMOOTHING",m_bl_filter)
cv2.waitKey()
cv2.destroyAllWindows()
