import cv2

print(cv2.__version__)

cvImage = cv2.imread("lock.jpg")
gray_image = cv2.cvtColor(cvImage, cv2.COLOR_BGR2GRAY)
cv2.imshow("Over the Clouds", cvImage)
cv2.imshow("Over the Clouds - gray", gray_image)
cv2.waitKey(0)

cv2.destroyAllWindows()