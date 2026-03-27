import random
import cv2
import argparse

def add_noise(img):

    # Getting the dimensions of the image
    row, col = img.shape[:2]
    
    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
      
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
        
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
        
        # Color that pixel to white
        img[y_coord][x_coord] = 255
        
    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
      
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
        
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
        
        # Color that pixel to black
        img[y_coord][x_coord] = 0
        
    return img

# salt-and-pepper noise can # be applied only to grayscale images
# Reading the color image in grayscale image
parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str,
	 				help='path to input image')
args = parser.parse_args()

img = cv2.imread(args.in_path)
output_image = add_noise(img)
output_path = args.in_path + "_noised.png"
#Storing the image
cv2.imwrite(output_path, output_image)