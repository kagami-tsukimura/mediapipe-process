import os

import cv2

img = cv2.imread("./images/icon.png")

h, w, c = img.shape
print(f"image[h: {h}, w: {w}, c: {c}]")

# trim
trim_img = img[100:300, 50:200]
trim_h, trim_w, trim_c = trim_img.shape
print(f"trim_image[h: {trim_h}, w: {trim_w}, c: {trim_c}]")

# resize
dsize = (200, 200)
resize_image = cv2.resize(img, dsize)

resize_h, resize_w, resize_c = resize_image.shape
print(f"resize_image[h: {resize_h}, w: {resize_w}, c: {resize_c}]")

images = {
    "origin": img,
    "trim": trim_img,
    "resize": resize_image,
}

output_dir = "./images/outputs"
os.makedirs(output_dir, exist_ok=True)

for name, image in images.items():
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

    cv2.imwrite(f"{output_dir}/output_{name}_icon.png", image)
