import os

import cv2

img = cv2.imread("./images/icon.png")

st_point = (80, 100)
end_point = (150, 30)
color = (0, 0, 255)
thickness = 2
line_type = cv2.LINE_8
shift = 0

# 描画
# 線
cv2.line(img, st_point, end_point, color, thickness, line_type, shift)

# 正方形
cv2.rectangle(img, st_point, end_point, color, thickness, line_type, shift)

# 矢印
arrow_end_point = (30, 150)
tipLength = 0.1
cv2.arrowedLine(
    img, st_point, arrow_end_point, color, thickness, line_type, shift, tipLength
)

# 円
center = (80, 100)
radius = 10
circle_color = (255, 255, 0)
cv2.circle(img, center, radius, circle_color, thickness, line_type, shift)

# 楕円
ellipse_center = (300, 220)
axes = (60, 50)
angle = 0
ellipse_color = (255, 0, 0)
box = (ellipse_center, axes, angle)
ellipse_thickness = -1
cv2.ellipse(img, box, ellipse_color, ellipse_thickness, line_type)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

imgs = {"origin": img, "img_gray": img_gray, "img_hsv": img_hsv, "img_rgb": img_rgb}

# 生の画像データ取得
w, h, c = img.shape
print(f"width: {w}, height: {h}, channels: {c}")
print(img[100, 100])


output_dir = "./images/outputs"
os.makedirs(output_dir, exist_ok=True)

for name, img in imgs.items():
    cv2.putText(
        img,
        name,
        (w // 3 * 1, h // 7 * 6),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2,
        cv2.LINE_AA,
    )
    cv2.imshow("", img)

    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite(f"{output_dir}/output_{name}.png", img)
