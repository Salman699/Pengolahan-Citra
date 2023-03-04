import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

imggambar= cv2.imread("a_balls3.jpg",-1)

cv2.imshow("Original image", imggambar)
scale_percent = 50
width = int(imggambar.shape[1] * scale_percent / 100)
height = int(imggambar.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(imggambar, dim, interpolation = cv2.INTER_AREA)
print (resized)
print('Original Dimensions : ',imggambar.shape)
print('Resized Dimensions : ',resized.shape)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()