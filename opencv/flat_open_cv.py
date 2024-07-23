import os

import cv2
import numpy as np


def call_noise(height, width):
    """
    Generates random noise coordinates based on the given height and width.

    Parameters:
    height (int): The height of the image.
    width (int): The width of the image.

    Returns:
    tuple: Two arrays containing random noise coordinates.
    """

    nx = np.random.randint(0, width - 1, 1500)
    ny = np.random.randint(0, height - 1, 1500)

    return nx, ny


img = cv2.imread("./images/icon.png")

height, width, _ = img.shape
noise_img = img.copy()

white = (255, 255, 255)
black = (0, 0, 0)

# ごま塩ノイズ
nx, ny = call_noise(height, width)
noise_img[ny, nx] = white
nx, ny = call_noise(height, width)
noise_img[ny, nx] = black

# 平坦化
# 平均化フィルタ
flatten_img = cv2.blur(noise_img, (5, 5))

images = {"origin": img, "noise": noise_img, "flatten": flatten_img}


output_dir = "./images/outputs"
os.makedirs(output_dir, exist_ok=True)

for name, image in images.items():
    h, w, _ = image.shape
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


imgs = cv2.hconcat(list(images.values()))
cv2.imshow("", imgs)

cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite(f"{output_dir}/output_all_icon.png", imgs)
