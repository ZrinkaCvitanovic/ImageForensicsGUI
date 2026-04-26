#source: https://opencv.org/resizing-and-rescaling-images-with-opencv/
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str,
                help='path to input image')
parser.add_argument('h', metavar='height_scale', type=int,
                help='desired scale for increasing height')
parser.add_argument('w', metavar='width_scale', type=int,
                     help='desired scale for increasing width')
parser.add_argument('method', type=str, choices=["cubic", "lanzos", "linear"], help="desired method for interpolation")
args = parser.parse_args()

image = cv2.imread(args.in_path)

# Load the image
low_res_img = cv2.imread(args.in_path)
low_res_img = cv2.cvtColor(low_res_img, cv2.COLOR_BGR2RGB)

height, width = low_res_img.shape[:2]
match args.method:
    case "cubic":
        method = cv2.INTER_CUBIC
    case "lanzos":
        method = cv2.INTER_LANCZOS4
    case "linear":
        method = cv2.INTER_LINEAR

parsed_path = args.in_path.split(".")
real_path = parsed_path[0]
extension = "." + parsed_path[1]

scaled_img = cv2.resize(low_res_img, (height * args.h, width * args.w), interpolation=method)
output_path = real_path + "-resize-" + args.method + "-" + str(args.h) + "-" + str(args.w) + extension
cv2.imwrite(output_path, scaled_img)