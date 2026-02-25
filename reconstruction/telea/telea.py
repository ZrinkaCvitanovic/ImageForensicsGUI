#source: https://docs.opencv.org/3.4/df/d3d/tutorial_py_inpainting.html
import numpy as np
import cv2 as cv
img = cv.imread('tulips_in.png')
mask = cv.imread('tulips_mask.png', cv.IMREAD_GRAYSCALE)
dst = cv.inpaint(img,mask,3,cv.INPAINT_TELEA)
#dst = cv.inpaint(img,mask,3,cv.INPAINT_NS)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()