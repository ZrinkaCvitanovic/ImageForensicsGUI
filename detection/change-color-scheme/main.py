#source: https://docs.opencv.org/3.4/df/d9d/tutorial_py_colorspaces.html
#source: https://docs.opencv.org/4.x/d5/d0f/tutorial_py_gradients.html
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str, help='path to input image')
parser.add_argument('method', metavar='method', type=str, choices=['hsv', 'lum'], 
                    help="desired method for converting your image")
args = parser.parse_args()
original_img = cv2.imread(args.in_path)
remove_ext = args.in_path.split(".")
real_path = remove_ext[0]
extension = "." + remove_ext[1]
if args.method == "hsv":
    result = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)
    output_path = real_path + "-HSV" + extension
else:
    #grayscale = cv2.cvtColor(original_img, cv2.IMREAD_GRAYSCALE)
    #result = cv2.Laplacian(grayscale,cv2.CV_64F)
    sobelx8u = cv2.Sobel(original_img,cv2.CV_8U,1,0,ksize=5)
    # Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U
    sobelx64f = cv2.Sobel(original_img,cv2.CV_64F,1,0,ksize=5)
    abs_sobel64f = np.absolute(sobelx64f)
    sobel_8u = np.uint8(abs_sobel64f)
    result = sobel_8u
    output_path = real_path + "-LUM" + extension

cv2.imwrite(output_path, result)
