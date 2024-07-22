import cv2

img = cv2.imread("./images/icon.png")
w, h, c = img.shape
print(f"width: {w}, height: {h}, channels: {c}")
print(img[0, 10])
cv2.putText(
    img,
    "Penguin",
    (w // 3 * 1, h // 7 * 6),
    cv2.FONT_HERSHEY_DUPLEX,
    1,
    (255, 0, 0),
    2,
)
cv2.imshow("", img)

cv2.waitKey()
cv2.destroyAllWindows()
