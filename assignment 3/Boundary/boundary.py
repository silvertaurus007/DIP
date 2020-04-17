import cv2
import numpy as np

img = cv2.imread('Fig09_16.tif')
img = cv2.resize(img,(500,500))

kernel = np.ones((4,4),np.uint8)

img0 = cv2.erode(img,kernel,iterations=1)
img1 = cv2.subtract(img,img0)

cv2.imshow('boundary',img1)
cv2.imwrite('boundary.jpg',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()


    
