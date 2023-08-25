# import cv2 as cv
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# img= cv.imread('bloodvessel.jpg')
# im2=img.copy()
# im2=cv.cvtColor(im2,cv.COLOR_BGR2GRAY)
# (mincval,maxval,minloc,maxloc)=cv.minMaxLoc(img)
# cv.circle(im2,maxloc,20,'r',5)
# cv.imshow('original',img)
# cv.imshow('original',im2)
# # cv.imwrite(r"brightspot.jpg",im2)

# cv.waitKey()
# cv.destroyAllWindows()

import cv2
import numpy as np

image = cv2.imread("bloodvessel.jpg")

image1 = image.copy()
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(minval, maxval, minloc, maxloc) = cv2.minMaxLoc(gray)

cv2.circle(image,maxloc,40,2)

cv2.imshow("Original Image",image1)
cv2.imshow("Processed Image",image)
cv2.imwrite("bright_spot.jpg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()