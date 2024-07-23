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
noise = img.copy()

white = (255, 255, 255)
black = (0, 0, 0)

# ごま塩ノイズ
nx, ny = call_noise(height, width)
noise[ny, nx] = white
nx, ny = call_noise(height, width)
noise[ny, nx] = black


cv2.imshow("", noise)
cv2.waitKey()
cv2.destroyAllWindows()
