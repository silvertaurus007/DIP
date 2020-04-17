import numpy as np
import cv2

img = cv2.imread('Fig09.tif')
img = cv2.resize(img,(500,500))
kernel = np.ones((6,6),np.uint8)
kernel1 = np.ones((2,2),np.uint8)
img_1 = cv2.imread('Fig09_7.tif')
img_1 = cv2.resize(img_1,(500,500))

img_erosion = cv2.erode(img,kernel,iterations=1)
img_dilation= cv2.dilate(img,kernel,iterations=1)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

improved_img = cv2.morphologyEx(img_1, cv2.MORPH_CLOSE, kernel1)

cv2.imshow('img',img)

cv2.imshow('Erosion',img_erosion)
cv2.imwrite('Erosion.jpg',img_erosion)

cv2.imshow('Dilation',img_dilation)
cv2.imwrite('Dilation.jpg',img_dilation)

cv2.imshow('opening',opening)
cv2.imwrite('Opening.jpg',opening)

cv2.imshow('closing',closing)
cv2.imwrite('closing.jpg',closing)

cv2.imshow('improved',improved_img)
cv2.imwrite('improved.jpg',improved_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
