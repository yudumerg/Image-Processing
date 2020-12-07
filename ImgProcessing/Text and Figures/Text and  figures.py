# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:55:01 2020

@author: asus
"""


import cv2
import numpy as np

#create img
img = np.zeros((512,512,3),np.uint8) #black img
print(img.shape)
cv2.imshow("Black",img)

#Line
#(img,starting point,end point,color,thickness)
cv2.line(img,(100,100),(100,300),(0,255,0),3) #BGR 
cv2.imshow("Line",img)

#Rectangle
#(img,starting point,end point,color)
cv2.rectangle(img,(0,0),(256,256),(255,0,0),cv2.FILLED) 
cv2.imshow("Rectangle",img)

#Circle
#(img,center,r,color)
cv2.circle(img,(300,300),45,(0,0,255))
cv2.imshow("Circle",img)

#Text
#(img,starting point,end point,font,thickness,color)
cv2.putText(img,"Image",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("Text",img)
