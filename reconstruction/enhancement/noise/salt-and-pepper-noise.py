# source: https://www.geeksforgeeks.org/python/add-a-salt-and-pepper-noise-to-an-image-with-python/
#source: https://www.askpython.com/python/examples/adding-noise-images-opencv
import random
import cv2
import argparse
import numpy as np

def salt_and_pepper(img):
    row, col = img.shape[:2]
    # Randomly pick some pixels in the image for coloring them white
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
      
        # Pick a random y and x coordinate and color them white
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        img[y_coord][x_coord] = 255
        
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
        # Pick a random y and x coordinate and color it black
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        img[y_coord][x_coord] = 0
        
    return img

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
if args.type == "salt-and-pepper":
    output_image = salt_and_pepper(img) # salt-and-pepper noise can be applied only to grayscale images??
    output_path = args.in_path + "_salt-and-pepper"
elif args.type == "gaussian":
    output_image = gaussian(img)
    output_path = args.in_path + "_gaussian.png"

else:
    output_image = random_noise(img)
    output_path = args.in_path + "_random.png"

#Storing the image
cv2.imwrite(output_path, output_image)