import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str,
                help='path to input image')
parser.add_argument('method', type=str, choices=["median", "gaussian"], help="desired method for denoising")

args = parser.parse_args()
image = cv2.imread(args.in_path)
remove_ext = args.in_path.split(".")
real_path = remove_ext[0]
extension = remove_ext[1]

if args.method == "median":
    denoised_image = cv2.medianBlur(image, 5)
    output_path = real_path + "-Median_blur." + extension
    cv2.imwrite(output_path, denoised_image)

elif args.method == "gaussian":
    denoised_image = cv2.GaussianBlur(image, (5,5),0)
    output_path = real_path + "-Gaussian_blur." + extension
    cv2.imwrite(output_path, denoised_image)


