import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

imggambar= cv2.imread("a_balls3.jpg",-1)

imgCropped = imggambar[0:150,150:500]
cv2.imshow("citra original",imggambar)
cv2.imshow("citra hasil crop",imgCropped)
cv2.waitKey(0)
cv2.destroyAllWindows