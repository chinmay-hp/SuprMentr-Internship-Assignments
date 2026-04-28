import cv2
import numpy as np

# Load Image (make sure image.jpg is in same folder)
image = cv2.imread('image.jpg')

# Print shape of image
print("Image Shape:", image.shape)

# Print pixel values (first 5 pixels)
print("\nSample Pixel Values:\n", image[0:5, 0:5])

# Separate channels
blue_channel = image[:, :, 0]
green_channel = image[:, :, 1]
red_channel = image[:, :, 2]

print("\nBlue Channel Shape:", blue_channel.shape)
print("Green Channel Shape:", green_channel.shape)
print("Red Channel Shape:", red_channel.shape)


