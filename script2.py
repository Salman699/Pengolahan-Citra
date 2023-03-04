import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

imggambar= cv2.imread("a_noise_tiga.jpg",-1)

height, width = imggambar.shape[:2]
qheight, qwidth = height / 4, width / 3
T = np.float32([[1, 0, qwidth], [0, 1, qheight]])
img_translation = cv2.warpAffine(imggambar, T, (width, height))
tampil_hor=np.concatenate((imggambar,img_translation),axis=1)
cv2.imshow('hasil',tampil_hor)
cv2.waitKey(0)
cv2.destroyAllWindows