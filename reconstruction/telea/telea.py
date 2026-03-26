#source: https://docs.opencv.org/3.4/df/d3d/tutorial_py_inpainting.html
import numpy as np
import cv2 as cv
import argparse
import imageio

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str, help='path to input image')
parser.add_argument('-t', action='store_true')
parser.add_argument('-ns', action='store_true')
args = parser.parse_args()

img = cv.imread(args.in_path)
mask = cv.imread(args.in_path, cv.IMREAD_GRAYSCALE)
method = ""
try:
    if (args.t):    
        dst = cv.inpaint(img,mask,3,cv.INPAINT_TELEA)
        method = "telea"
    elif (args.ns):
        dst = cv.inpaint(img,mask,3,cv.INPAINT_NS)
        method = "ns"
        
except:
     Exception("Set -t or -ns flag for Telea or Navier-Stokes inpainting respectively.")

out_path = args.in_path + "_result_"  + method + ".jpg"
imageio.v2.imwrite(out_path, img)