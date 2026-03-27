import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str,
                help='path to input image')
args = parser.parse_args()

image = cv2.imread(args.in_path)

denoised_image = cv2.medianBlur(image, 5)
output_path = args.in_path + "_denoised.png"
cv2.imwrite(output_path, denoised_image)
