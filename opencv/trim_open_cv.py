import cv2

img = cv2.imread("./images/icon.png")

h, w, c = img.shape
print(f"image[h: {h}, w: {w}, c: {c}]")

trim_img = img[100:300, 50:200]
print(f"trim_image[h: {h}, w: {w}, c: {c}]")
cv2.imshow("", trim_img)

cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite("./images/trim_icon.png", trim_img)
