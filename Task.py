import cv2
import numpy as np
image_name='for_watson.png'
image = cv2.imread(image_name)
h=255*np.ones((480,640,3))
for i in range(0,480):
    for j in range(0,640):
        for k in range(0,3):
            if ((image[i,j,k]!=0) and (image[i,j,k]!=255)):
                h[i,j,k]=image[i,j,k]          
filename = 'Message.jpg'
cv2.imwrite(filename, h)