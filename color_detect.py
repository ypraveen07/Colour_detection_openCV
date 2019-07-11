import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]


print(len(flags))

print(flags[40])

import matplotlib.pyplot as plt
import numpy as np

nemo = cv2.imread("C:\\Users\\Praveen Kumar\\Desktop\\DSP-certificate-1.jpg")
plt.imshow(nemo)
plt.show()


nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
plt.imshow(nemo)
plt.show()


hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)

light_orange = (0, 0, 200)
dark_orange = (145, 55, 255)


mask = cv2.inRange(hsv_nemo, light_orange, dark_orange)
result = cv2.bitwise_and(nemo, nemo, mask=mask)

plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result)
plt.show()
