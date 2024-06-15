import cv2
import numpy as np

def scale(img, sca_x=1, sca_y=1):
    h,w = img.shape
    h_n,w_n = int(h*sca_y),int(w*sca_x)
    img_n = np.zeros((h_n,w_n),dtype=np.uint8)

    for y in range(h):
        for x in range(w):
            img_n[int(sca_y*y),int(sca_x*x)] =img[y,x]

    return img_n
    
    
def scale2(img, sca_x=1, sca_y=1):
    h,w = img.shape
    h_n,w_n = int(h*sca_y),int(w*sca_x)
    img_n = np.zeros((h_n,w_n),dtype=np.uint8)

    for y in range(h_n):
        for x in range(w_n):
            img_n[y,x] =img[int(y/sca_y),int(x/sca_x)]

    return img_n
    

def nearest(img, sca_x=1, sca_y=1):
    h,w = img.shape
    h_n,w_n = int(h*sca_y),int(w*sca_x)
    img_n = np.zeros((h_n,w_n),dtype=np.uint8)

    for y in range(int(h*sca_y)):
        for x in range(int(w*sca_x)):
            try:
                img_n[y,x] = img[round(y/sca_y),round(x/sca_x)]
            except:
                pass

    return img_n

def linear(img, sca_x=1, sca_y=1):
    h,w = img.shape
    h_n,w_n = int(h*sca_y),int(w*sca_x)
    img_n = np.zeros((h_n,w_n),dtype=np.uint8)

    for y in range(int(h*sca_y)):
        for x in range(int(w*sca_x)):
            q = x/sca_x - int(x/sca_x)
            p = y/sca_y - int(y/sca_y)

            try:
                X = int(x/sca_x)
                Y = int(y/sca_y)
                value = (1-q)*(1-p)*img[Y,X] + p*(1-q)*img[Y+1,X] + (1-p)*q*img[Y,X+1] + q*p*img[Y+1,X+1]
                if value>255:
                    img_n[y,x] = 255
                else:
                    img_n[y,x] = value

            except:
                pass
    return img_n

img = cv2.imread('elonmusk.jpg',cv2.IMREAD_GRAYSCALE)
result2 = linear(img,2,1)
result = nearest(img,2,1)

cv2.imshow('test1',result2)
cv2.imshow('test2',result)

cv2.waitKey()

cv2.destroyAllWindows()