import cv2
import numpy as np

#PATH FOR IMAGE 1 (BASE IMAGE)
img1 = cv2.imread('dog_backpack.png')
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
#PATH FOR IMAGE 2 (COPYRIGHT)
img2 = cv2.imread('watermark_no_copy.png') 
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

img2 = cv2.resize(img2,(600,600))

large_img = img1
small_img = img2

x_offset = large_img.shape[1] - small_img.shape[1]
y_offset = large_img.shape[0] - small_img.shape[0]

rows, cols, channels = img2.shape 
roi = img1[y_offset:large_img.shape[0],x_offset:large_img.shape[1]]

img2gray = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)

mask_inv = cv2.bitwise_not(img2gray)
white_background = np.full(img2.shape,255,dtype=np.uint8)

bk = cv2.bitwise_or(white_background,white_background,mask=mask_inv)
fg = cv2.bitwise_or(img2,img2,mask=mask_inv)
final_roi = cv2.bitwise_or(roi,fg)

cv2.namedWindow(winname='backpack')

large_img = img1
small_img = final_roi

large_img[y_offset:y_offset+small_img.shape[0],x_offset:x_offset+small_img.shape[1]] = small_img

large_img = cv2.cvtColor(large_img,cv2.COLOR_BGR2RGB)

while True:
    
    cv2.imshow('backpack',large_img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break