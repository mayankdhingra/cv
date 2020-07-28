import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# FUNCTION - DRAW CIRCLE
def draw_circle(event,x,y,flags,param):
    
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),20,(255,0,0),thickness=10)
    


# SHOWING PICTURE 
img = np.zeros((512,512,3))
cv2.namedWindow(winname='my_circle')
cv2.setMouseCallback('my_circle',draw_circle)

while True:
    
    cv2.imshow('my_circle',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()