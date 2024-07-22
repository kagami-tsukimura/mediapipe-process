import cv2

img = cv2.imread("./images/icon.png")
cv2.circle(img, (100, 100), 10, (0, 0, 255), -1)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

imgs = {"img": img, "img_gray": img_gray, "img_hsv": img_hsv, "img_rgb": img_rgb}

# 生の画像データ取得
w, h, c = img.shape
print(f"width: {w}, height: {h}, channels: {c}")
print(img[100, 100])


for name, img in imgs.items():
    cv2.putText(
        img,
        name,
        (w // 3 * 1, h // 7 * 6),
        cv2.FONT_HERSHEY_DUPLEX,
        1,
        (255, 0, 0),
        2,
    )
    cv2.imshow("", img)

    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite(f"./images/output_{name}.png", img)
