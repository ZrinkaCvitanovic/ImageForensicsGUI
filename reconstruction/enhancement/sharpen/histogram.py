import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str, help='path to input image')
args = parser.parse_args()

image = cv2.imread(args.in_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray_image)
parsed_path = args.in_path.split(".")
real_path = parsed_path[0]
extension = "." + parsed_path[1]
output_path = real_path + "-sharpen-histogram" + extension
cv2.imwrite(output_path, equalized_image)