import cv2

from matplotlib import pyplot as plt
img = cv2.imread("Figure2.jpg")
laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
sobelImg= cv2.add(sobelx, sobely)
schx= cv2.Scharr(img, cv2.CV_64F, 1, 0)
schy= cv2.Scharr(img, cv2.CV_64F, 0, 1)
plt.subplot(2,3,1),plt.imshow(img,cmap="gray"),plt.title("OriginallImage")
plt.subplot(2,3,2),plt.imshow(laplacian,cmap="gray"),plt.title("laplacian Image")
plt.subplot(2,3,3),plt.imshow(sobelx,cmap="gray"),plt.title("sobelx Image")
plt.subplot(2,3,4),plt.imshow(sobely,cmap="gray"),plt.title("sobely Image")
plt.subplot(2,3,5),plt.imshow(schx,cmap="gray"),plt.title("schx Image")
plt.subplot(2,3,6),plt.imshow(schy,cmap="gray"),plt.title("schy Image")

plt.imshow()
