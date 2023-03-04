import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

imggambar= cv2.imread("a_balls3.jpg",-1)

cv2.imshow("Original image", imggambar)
imgresize= cv2.resize(imggambar,(200,500))
cv2.imshow("citra hasil",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows