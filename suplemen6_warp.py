import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread("a_balls3.jpg")
print(img.shape)

width,height = 200,350
pts1 = np.float32([[111,400],[287,500],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[352,440]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imghasil = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("asli",img)
cv2.imshow("hasil",imghasil)

cv2.waitKey(0)
cv2.destroyAllWindows
