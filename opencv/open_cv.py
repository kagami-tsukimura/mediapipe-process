import cv2

image = cv2.imread("./images/icon.png")
cv2.imshow("", image)

cv2.waitKey()
cv2.destroyAllWindows()
