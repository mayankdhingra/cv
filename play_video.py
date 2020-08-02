import cv2
import time

cap = cv2.VideoCapture('mysupervideo.mp4')

if cap.isOpened() == False:
    print('ERROR: File Not Found OR Wrog Codec Used')

while cap.isOpened():
    
    ret, frame = cap.read()
    
    if ret == True:
        
        #Frame per second at which the video was recorded, 25 FPS for me
        time.sleep(1/25)
        
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(10) & 0xFF == 27:
            break
    else:
        break