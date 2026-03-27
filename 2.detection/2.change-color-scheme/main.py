import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str, help='path to input image')
parser.add_argument('method', metavar='method', type=str, choices=['hsv', 'lum'], 
                    help="desired method for converting your image")
args = parser.parse_args()


original_img = cv2.imread(args.in_path)
hsv_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)
cv2.imwrite("hsv.png", hsv_img)
