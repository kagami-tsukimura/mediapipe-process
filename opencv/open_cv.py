import cv2
import matplotlib.pyplot as plt

image = cv2.imread("./images/icon.png")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
