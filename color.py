import cv2

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)
while 1:
    _,f = cap.read()
    chromakey = f[:10, :10, :]
    hsv_chroma = cv2.cvtColor(chromakey,cv2.COLOR_BGR2HSV)
    chroma_h = hsv_chroma[:,:,0]
    print('dfdf')
    print(hsv_chroma[:,:,0])
    print( hsv_chroma[:,:,1])
    print( hsv_chroma[:,:,2])
    print('dfdf')
    cv2.imshow('test',f)
    cv2.waitKey(delay)

cap.release()
cv2.destroyAllWindows()