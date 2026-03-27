import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str, help='path to input image')
parser.add_argument('lower', metavar="lower_threshold", type=int, help='minimum value of a gradient for a pixel, anything below will certainly be rejected as an edge candidate')
parser.add_argument('higher', metavar="higher_threshold", type=int, help='maximum value of a gradient for a pixel to be accepted as an edge')

parser.add_argument('--robust', action="store_true", 
                    help="use for blurry or noisy images")
parser.add_argument('--both', action="store_true", 
                    help="use if unsure")
args = parser.parse_args()

gray_image = cv2.imread(args.in_path, cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(gray_image, args.lower, args.higher)

if args.robust or args.both:
    equalized_image = cv2.equalizeHist(gray_image)
    #output_path = input_path + "_equalized.png"
    #cv2.imwrite(output_path, equalized_image) 

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    background = cv2.morphologyEx(equalized_image, cv2.MORPH_DILATE, kernel)
    shadow_removed = cv2.subtract(background, equalized_image)
    #output_path = input_path + "_no_shadows.png"
    #cv2.imwrite(output_path, shadow_removed) 

    gaussian_blur = cv2.GaussianBlur(gray_image, (5, 5), 0)
    bilateral_filter = cv2.bilateralFilter(gray_image, 9, 75, 75)
    #output_path = input_path + "_no_blur.png"
    #cv2.imwrite(output_path, bilateral_filter) 

    segmented_map = cv2.Canny(bilateral_filter, 50, 150)  # Edge detection
    segmented_map = cv2.dilate(segmented_map, None, iterations=1) 

    output_path = args.in_path + "_" + str(args.lower) + "_" + str(args.higher) + "_edges_robust.jpg"
    cv2.imwrite(output_path, segmented_map) 
else: 
    output_path = args.in_path + "_" + str(args.lower) + "_" + str(args.higher) + "_edges.jpg"
    cv2.imwrite(output_path, edges) 

if args.both:
    output_path = args.in_path + "_" + str(args.lower) + "_" + str(args.higher) + "_edges.jpg"
    cv2.imwrite(output_path, edges) 
