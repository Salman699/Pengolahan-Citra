import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

imggambar= cv2.imread("a_balls3.jpg",-1)

imgmedian = cv2.medianBlur(imggambar,9)
tampil_hor=np.concatenate((imggambar,imgmedian),axis=0)
cv2.imshow('hasil',tampil_hor)
cv2.waitKey(0)
cv2.destroyAllWindows