# source: https://www.geeksforgeeks.org/python/add-a-salt-and-pepper-noise-to-an-image-with-python/
#source: https://www.askpython.com/python/examples/adding-noise-images-opencv
import random
import cv2
import argparse
import numpy as np

def salt_and_pepper(img, noise_ratio=0.02):
    noisy_image = img.copy()
    h, w, c = noisy_image.shape
    noisy_pixels = int(h * w * noise_ratio)
 
    for _ in range(noisy_pixels):
        row, col = np.random.randint(0, h), np.random.randint(0, w)
        if np.random.rand() < 0.5:
            noisy_image[row, col] = [0, 0, 0] 
        else:
            noisy_image[row, col] = [255, 255, 255]
 
    return noisy_image

def gaussian(img, mean=0, std=25):
    noise = np.random.normal(mean, std, img.shape).astype(np.uint8)
    noisy_image = cv2.add(img, noise)
    return noisy_image

def random_noise(img, intensity=25):
    noisy_image = img.copy()
    noise = np.random.randint(-intensity, intensity + 1, noisy_image.shape)
    noisy_image = np.clip(noisy_image + noise, 0, 255).astype(np.uint8)
    return noisy_image

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str,
	 				help='path to input image')
parser.add_argument('type', metavar='noise_type', type=str, choices=["gaussian", "salt-and-pepper", "random"], help='desired type of noise')
args = parser.parse_args()
img = cv2.imread(args.in_path)
img_gray =cv2.imread(args.in_path, cv2.IMREAD_GRAYSCALE)
output_image = img

remove_ext = args.in_path.split(".")
real_path = remove_ext[0]
extension = "." + remove_ext[1]

if args.type == "salt-and-pepper":
    output_image = salt_and_pepper(img) # salt-and-pepper noise can be applied only to grayscale images??
    output_path = real_path + "_salt-and-pepper" + extension
elif args.type == "gaussian":
    output_image = gaussian(img)
    output_path = real_path + "_gaussian" + extension

else:
    output_image = random_noise(img)
    output_path = real_path + "_random" + extension

cv2.imwrite(output_path, output_image)