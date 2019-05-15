"""Extracting and Saving Video Frames using OpenCV-PythonPython."""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rgb2gray(image):
    """Transform a color image to a grayscale image."""
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])

# Opens the Video file
cap = cv2.VideoCapture('caminata_lenta.mp4')
i = 0
frames = []
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        break
    if len(str(i)) > 1:
        cv2.imwrite('frame' + str(i) + '.jpg', frame)
        frames.append(rgb2gray(mpimg.imread('frame' + str(i) + '.jpg')))
    else:
        cv2.imwrite('frame0' + str(i) + '.jpg', frame)
        frames.append(rgb2gray(mpimg.imread('frame0' + str(i) + '.jpg')))
    i += 1

cap.release()
cv2.destroyAllWindows()

blue_spot = rgb2gray(mpimg.imread('spot_blue.jpg'))
green_spot = rgb2gray(mpimg.imread('spot_green.jpg'))
red_spot = rgb2gray(mpimg.imread('spot_red.jpg'))

blue_spot_min = np.amin(blue_spot)
green_spot_min = np.amin(green_spot)
red_spot_min = np.amin(red_spot)

blue_spot_max = np.amax(blue_spot)
green_spot_max = np.amax(green_spot)
red_spot_max = np.amax(red_spot)

red_images = []
green_images = []
blue_images = []

for gray_frame in frames:
    red_image = np.zeros(gray_frame.shape)
    green_image = np.zeros(gray_frame.shape)
    blue_image = np.zeros(gray_frame.shape)
    y = gray_frame.shape[0]
    x = gray_frame.shape[1]
    for j in range(1, y - 1):
        for i in range(1, x - 1):
            if blue_spot_min < gray_frame[j, i] < blue_spot_max:
                blue_image[j, i] = 255
            if green_spot_min < gray_frame[j, i] < green_spot_max:
                green_image[j, i] = 255
            if red_spot_min < gray_frame[j, i] < red_spot_max:
                red_image[j, i] = 255
    red_images.append(red_image)
    green_images.append(green_image)
    blue_images.append(blue_image)

fig = plt.gcf()
fig.show()

for red_gray_image, green_gray_image, blue_gray_image in red_images, green_images, blue_images:
    plt.subplot(1, 3, 1)
    plt.imshow(red_gray_image, cmap=plt.get_cmap('gray'))
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(green_gray_image, cmap=plt.get_cmap('gray'))
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(blue_gray_image, cmap=plt.get_cmap('gray'))
    plt.axis('off')
    fig.canvas.draw()

"""
fig = plt.gcf()
fig.show()

for gray_frame in frames:
    plt.imshow(gray_frame, cmap=plt.get_cmap('gray'))
    fig.canvas.draw()
"""
