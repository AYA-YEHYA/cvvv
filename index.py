import cv2
import numpy as np
from scipy import ndimage
kernel_3x3 = np.array([[-1, -1, -1],
[-1, 8, -1],
[-1, -1, -1]])

img=cv2.imread("Figure1")
k3=ndimage.convlove(img,kernel_3x3)
 
blured=cv2.GaussianBlur(img,(7,7),0)
g_hbf=img-blured

cv2.imshow('originalImage',img)
cv2.imshow('3x3',k3)
cv2.imshow('blureImage',blured)
cv2.imshow('g_hbf',g_hbf)

cv2.waitKey()
cv2.destroyAllWindows()