import cv2
import numpy as numpy
from matplotlib import pyplot as plt

img=cv2.imread('gambar1B.png',0)
edges=cv2.Canny(img,100,200)


plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Original image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('Edge Image'),plt.xticks([]),plt.yticks([])
cv2.putText(img,"Salman Tubagus Alfarizi-2215102006-MM1",(100,175),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,225,225),1)

tampil_hor=np.concatenate((imggambar,imgopening),axis=0)
cv2.imshow('hasil akhir',tampil_hor)
plt.show()