import cv2
import numpy as np

img = cv2.imread("./images/icon.png")

height, width, _ = img.shape
noise = img.copy()

white = (255, 255, 255)
black = (0, 0, 0)

nx = np.random.randint(0, width - 1, (height, width))
ny = np.random.randint(0, height - 1, (height, width))

# ごま塩ノイズ
for i in range(height):
    for j in range(width):
        noise[i, j] = white if (nx[i, j] + ny[i, j]) < 255 else black


cv2.imshow("", noise)
cv2.waitKey()
cv2.destroyAllWindows()
