import numpy as np
import matplotlib.image as mpimg


def rgb2gray(image):
    """Transform a color image to a grayscale image."""
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])

blue_spot = rgb2gray(mpimg.imread('spot_blue.jpg'))
green_spot = rgb2gray(mpimg.imread('spot_green.jpg'))
red_spot = rgb2gray(mpimg.imread('spot_red.jpg'))

blue_spot_min = np.amin(blue_spot)
green_spot_min = np.amin(green_spot)
red_spot_min = np.amin(red_spot)

blue_spot_max = np.amax(blue_spot)
green_spot_max = np.amax(green_spot)
red_spot_max = np.amax(red_spot)

print(blue_spot_min)
print(green_spot_min)
print(red_spot_min)
print(blue_spot_max)
print(green_spot_max)
print(red_spot_max)
