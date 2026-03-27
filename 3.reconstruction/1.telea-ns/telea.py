#source: https://docs.opencv.org/3.4/df/d3d/tutorial_py_inpainting.html
import numpy as np
import cv2 as cv
import argparse
import imageio

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str, help='path to input image')
parser.add_argument('mask_path', metavar='mask_path', type=str, help='path to mask image')
parser.add_argument('-t', action='store_true')
parser.add_argument('-ns', action='store_true')
args = parser.parse_args()

if not args.t and not args.ns:
    print("Set -t or -ns flag for Telea or Navier-Stokes inpainting respectively.")
    exit(1)
img = cv.imread(args.in_path, cv.COLOR_BGR2RGB)
dst = img
mask = cv.imread(args.mask_path, cv.IMREAD_GRAYSCALE)
method = ""
if (args.t):    
    dst = cv.inpaint(img,mask,30,cv.INPAINT_TELEA)
    method = "telea"
else    :
    dst = cv.inpaint(img,mask,30,cv.INPAINT_NS)
    method = "ns"

out_path = args.in_path + "_result_" + method + ".png"
imageio.v2.imwrite(out_path, dst)
