import cv2
import sys
import numpy as np

do_chro = False

capture1 = cv2.VideoCapture(0)

if not capture1.isOpened():
    print("ㄴㄴ")
    sys.exit

capture2 = cv2.VideoCapture('sample.mp4')

w = round(capture1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(capture1.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_count1 = round(capture1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_count2 = round(capture2.get(cv2.CAP_PROP_FRAME_COUNT))
print(f'w:{w}, h:{h},count1 :{frame_count1},count2 :{frame_count2}')

fps = capture1.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc,fps,(w,h))


while True:
    ret1 ,frame1 = capture1.read()
    if not ret1:
        break
    ret2,frame2 = capture2.read()
    
    if not ret2:
        break

    frame2 = cv2.resize(frame2,(w,h))

    hsv = cv2.cvtColor(frame1,cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv,(110,130,160),(120,160,180))
    cv2.copyTo(frame2,mask,frame1)
        


    out.write(frame1)
    cv2.imshow('test',frame1)
    key = cv2.waitKey(delay)

    if key == ord(' '):
        do_chro = not do_chro
    elif key == 27:
        break

capture1.release()
capture2.release()
out.release()
cv2.destroyAllWindows
