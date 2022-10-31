#Muhammed Hukumdar 02210201501
import cv2
import numpy as np

img = cv2.imread("ucak.jpg",0)
cv2.imshow("not inverter",img)

h=img.shape[0]
w=img.shape[1]
img2 = np.zeros([h,w], dtype = np.uint8)

for i in range(h):
    for j in range(w):
        img2[i,j] = 255 - img[i,j]

cv2.imshow("inveter", img2)
cv2.waitKey()