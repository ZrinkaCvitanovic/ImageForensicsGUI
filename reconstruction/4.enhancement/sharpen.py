import cv2
import numpy as np

# Load the image
image = cv2.imread("blurry.jpg")

# Create the sharpening kernel
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# Sharpen the image
sharpened_image = cv2.filter2D(image, -1, kernel)

#Save the image
cv2.imwrite('sharpened_image.jpg', sharpened_image)