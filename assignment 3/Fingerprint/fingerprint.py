import cv2
import numpy as np

img=cv2.imread('fingerprint.tif')
#img = cv2.resize(img,(500,500))

kernel = np.ones((5,5),np.uint8)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

cv2.imshow('result',close)
cv2.imwrite('improved.jpg',close)

cv2.waitKey(0)
cv2.destroyAllWindows()
