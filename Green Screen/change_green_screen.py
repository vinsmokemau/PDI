import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('green_screen_frames/frame00.jpg')


def change_green_screen(image):
    """Change the green background for an image."""
    image_copy = np.copy(image)
    image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

    lower_green = np.array([0, 70, 0])
    upper_green = np.array([80, 255, 100])

    mask = cv2.inRange(image_copy, lower_green, upper_green)

    masked_image = np.copy(image_copy)
    masked_image[mask != 0] = [0, 0, 0]

    background_image = cv2.imread('new_screen_frames/frame00.jpg')
    background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

    background_image[mask == 0] = [0, 0, 0]

    final_image = background_image + masked_image

    return final_image
