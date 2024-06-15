import cv2
import numpy as np


img2 = cv2.imread("skkbg.jpg")
img2 = cv2.resize(img2,dsize=(640,360))
img1 = cv2.imread("epicsaxguy.jpg")
img1 = cv2.resize(img1,dsize=(320,180))

h1,w1 = img1.shape[:2]
h2,w2 = img2.shape[:2]
x = (w2-w1)//2
y = h2-h1
w = x+ w1
h = y+ h1

hsv_kro = img1[:10,:10,:]
offset = 10



hsv_human = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
hsv_krodd = cv2.cvtColor(hsv_kro,cv2.COLOR_BGR2HSV)

chro_h = hsv_krodd[:,:,0]
min = np.array([chro_h.min()-offset,100,100])
max = np.array([chro_h.max()+offset,255,255])
print(min,max)
mask = cv2.inRange(hsv_human,min,max)
cv2.imshow('d',mask)
mask_inv = cv2.bitwise_not(mask)
roi = img2[y:h,x:w]
human = cv2.bitwise_and(img1,img1,mask=mask_inv)
bg = cv2.bitwise_and(roi,roi,mask=mask)
img2[y:h,x:w] = human+bg
cv2.imshow('test',img2)

cv2.waitKey()
cv2.destroyAllWindows()