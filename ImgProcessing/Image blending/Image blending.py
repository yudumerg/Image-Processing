# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:02:59 2020

@author: asus
"""

import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("img1.JPG")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

img2 = cv2.imread("img2.JPG")
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)


print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (600,600))
print(img1.shape)

img2 = cv2.resize(img2,(600,600))
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#Blended Img= Alpha*img1+beta*img2
blended = cv2.addWeighted(src1= img1,alpha = 0.5, src2 =img2, beta = 0.5 , gamma=0)
plt.figure()
plt.imshow(blended)