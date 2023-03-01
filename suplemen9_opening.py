import cv2
import numpy as np
from matplotlib import pyplot as plt

imggambara=cv2.imread("circle4.jpg",0)
imggambar=cv2.cvtColor(imggambara,cv2.THRESH_BINARY)
kernel = np.ones((10,10),np.uint8)
imgopening=cv2.morphologyEx(imggambar,cv2.MORPH_OPEN,kernel)
# kernel = np.ones((5,5),np.uint8)
# imgmg=cv2.morphologyEx(imgopening,cv2.MORPH_GRADIENT,kernel)

# tampil_hor=np.concatenate((imggambar,imgopening),axis=0)

cv2.putText(imgopening,"Salman Tubagus Alfarzizi - 2215102006 - MM1",(100,175),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),1)


tampil_hor=np.concatenate((imggambar,imgopening),axis=0)
cv2.imshow('hasil akhir',tampil_hor)

# cv2.imshow("contoh opening",imgopening)

cv2.waitKey(0)
cv2.destroyAllWindows



# kernel = np.ones((7,7),np.uint8)
# imgclosing=cv2.morphologyEx(imggambar,cv2.MORPH_CLOSE,kernel)
# cv2.imshow("contoh closing",imgclosing)
