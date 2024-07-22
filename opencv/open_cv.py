import cv2

image = cv2.imread("./images/icon.png")
w, h, _ = image.shape
cv2.putText(
    image,
    "Penguin",
    (w // 3 * 1, h // 7 * 6),
    cv2.FONT_HERSHEY_DUPLEX,
    1,
    (255, 0, 0),
    2,
)
cv2.imshow("", image)

cv2.waitKey()
cv2.destroyAllWindows()
