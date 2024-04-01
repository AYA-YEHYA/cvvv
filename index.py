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