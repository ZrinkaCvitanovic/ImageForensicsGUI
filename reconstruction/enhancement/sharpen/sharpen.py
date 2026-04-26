import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str, help='path to input image')
parser.add_argument('method', metavar='method', type=str, choices=['kernel', 'laplacian'], 
                    help="desired method for sharpening your image")
args = parser.parse_args()

# Create the sharpening kernel
image = cv2.imread(args.in_path)
if (args.method == "kernel"):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    # Sharpen the image
    sharpened = cv2.filter2D(image, -1, kernel)
else:
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    # Scale the Laplacian output for visualization
    laplacian = np.uint8(np.absolute(laplacian))
    # Add the Laplacian output to the original image
    sharpened = cv2.addWeighted(image, 1, laplacian, 1, 0)

parsed_path = args.in_path.split(".")
real_path = parsed_path[0]
extension = "." + parsed_path[1]
#Save the image
output_path = real_path + "-sharpen-" + args.method + extension
cv2.imwrite(output_path, sharpened)