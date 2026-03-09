import cv2

image = cv2.imread('ela.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray_image)

cv2.imwrite('equalised.jpg',equalized_image)