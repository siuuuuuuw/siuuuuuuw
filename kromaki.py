import cv2
import numpy as np

img1 = 'skkk.jpeg'
img2 = 'skkbg.jpg'


#로고 리사이징
im1= cv2.imread(img1)
im1 = cv2.resize(im1,dsize=(150,150))
im2 = cv2.imread(img2)
im2 = cv2.resize(im2,dsize=(640,360))
#로고 행,열 값


rows,cols,ch = im1.shape
#관심 영역 추출
roi = im2[:rows,:cols]
#로고- 흑백
logoGray = cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)

#임계값 기준 흰 검 분리

_,mask = cv2.threshold(logoGray,100,255,cv2.THRESH_BINARY)

#흑백 반전
mask_inv = cv2.bitwise_not(mask)

#관심영억에서 로고자리 확보
im2_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
#로고만 확실히 살려두기
im1_n = cv2.bitwise_and(im1,im1,mask = mask)


result = cv2.add(im2_bg,im1_n)#두 이미지 배열 합
im2[:rows,:cols] = result
cv2.imshow('test',im2)


cv2.waitKey()
cv2.destroyAllWindows()