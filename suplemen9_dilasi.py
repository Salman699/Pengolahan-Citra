import cv2
import numpy as np
from matplotlib import pyplot as plt

imggambar = cv2.imread("a_balls3.jpg",0)
kernel = np.ones((1,1),np.uint8)
kernel2 = np.ones((15,15),np.uint8)

imgCanny = cv2.Canny(imggambar,10,150)
imgdilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgdilation2 = cv2.dilate(imgCanny,kernel2,iterations=1)
imgdilation3= ~imgdilation2

tampil_hor=np.concatenate((imggambar,imgdilation2),axis=0)
# tampil_hor=np.concatenate((imggambar,mg),axis=0)

cv2.imshow('hasil akhir',tampil_hor)

# cv2.imshow("dilate Image 5",imgdilation2)
cv2.waitKey(0)
cv2.destroyAllWindows