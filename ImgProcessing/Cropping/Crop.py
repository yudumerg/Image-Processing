

import cv2

img = cv2.imread("lenna.png")
print("Image Shape:",img.shape)
cv2.imshow("original",img)

#resized

imgResized = cv2.resize(img,(800,800))
print("Resized Img Shape:",imgResized.shape)
cv2.imshow("Img Resized", imgResized)

#crop
imgCropped = img[:200,:300]
cv2.imshow("Cropped Img",imgCropped)
