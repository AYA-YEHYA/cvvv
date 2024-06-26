# import cv2
# import numpy as np
# from scipy import ndimage
# kernel_3x3 = np.array([[-1, -1, -1],
# [-1, 8, -1],
# [-1, -1, -1]])

# img=cv2.imread("Figure1")
# k3=ndimage.convlove(img,kernel_3x3)
 
# blured=cv2.GaussianBlur(img,(7,7),0)
# g_hbf=img-blured

# cv2.imshow('originalImage',img)
# cv2.imshow('3x3',k3)
# cv2.imshow('blureImage',blured)
# cv2.imshow('g_hbf',g_hbf)

# cv2.waitKey()
# cv2.destroyAllWindows()


# import cv2
# import numpy as np

# image = cv2.imread('Figure1.jpg', cv2.IMREAD_GRAYSCALE)

# kernel = np.array([[0, -1, 0],
#                    [-1, 4, -1],
#                    [0, -1, 0]])

# edges = cv2.filter2D(image, -1, kernel)

# cv2.imshow('Original Image', image)
# cv2.imshow('Edges', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np 
pipes=cv2.imread('img1.jpg')
gray_img = cv2.cvtColor(pipes,cv2.COLOR_BGR2GRAY)
gray_img = cv2.medianBlur(gray_img , 5)
cricles = cv2.HoughCircles(gray_img,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minDist=0,minRadius=0)
cricles =np.uint16(np.around(cricles))
for i in cricles[0,:]:
    cv2.circle(pipes,(i[0],i[1],2,(0,255,0),2))
    cv2.circle(pipes,(i[0],i[1],2,(0,0,255),3))
cv2.imwrite('img1.jpg',pipes)   
cv2.imshow("HoughCricles",pipes)
cv2.waitKey()   
cv2.destroyAllWindows()
