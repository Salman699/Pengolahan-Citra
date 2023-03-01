import cv2
import numpy as np
from matplotlib import pyplot as plt

imggambar = cv2.imread("a_balls3.jpg",0)
kernel = np.ones((5,5),np.uint8)
kernel2 = np.ones((1,1),np.uint8)


imgCanny = cv2.Canny(imggambar,10,150)
imgdilation5 = cv2.dilate(imgCanny,kernel,iterations=1)
imgErode = cv2.erode(imgdilation5,kernel2,iterations=1)

tampil_hor=np.concatenate((imgCanny,imgErode),axis=1)
cv2.imshow('hasil akhir',tampil_hor)

# cv2.imshow("erosion Image",imgErode)
cv2.waitKey(0)
cv2.destroyAllWindows