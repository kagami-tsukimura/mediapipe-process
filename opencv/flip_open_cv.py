import cv2

img = cv2.imread("./images/icon.png")

# 時計回りに90度回転
clock_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# 反時計回りに90度回転
counter_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# 180度回転
reverse_img = cv2.rotate(img, cv2.ROTATE_180)

imgs = {
    "origin": img,
    "clock": clock_img,
    "counter": counter_img,
    "reverse": reverse_img,
}

for name, image in imgs.items():
    h, w, c = image.shape
    cv2.putText(
        image,
        name,
        (w // 3 * 1, h // 7 * 6),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2,
        cv2.LINE_AA,
    )
    cv2.imshow("", image)

    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite(f"./images/outputs/output_{name}_icon.png", image)
