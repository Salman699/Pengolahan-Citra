import cv2

img=cv2.imread('a_balls3.jpg')

#now detect canny edge

canny=cv2.Canny(img, 200, 250)

cv2.imshow("original",img)
cv2.imshow("canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()