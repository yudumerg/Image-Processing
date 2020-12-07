# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:17:57 2020

@author: asus
"""


import cv2
import numpy as np

img = cv2.imread("card.png")
cv2.imshow("Original",img)

width = 400
height = 500

pts1 = np.float32([[230,1],[1,472],[540,150],[338,617]])
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

#transformed image
imgOutput = cv2.warpPerspective(img, matrix,(width,height))
cv2.imshow("Last Img",imgOutput)
