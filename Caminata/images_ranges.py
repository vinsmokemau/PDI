import cv2
import numpy as np
import matplotlib.image as mpimg


def rgb2gray(image):
    """Transform a color image to a grayscale image."""
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])

frame_id = 0
frames = []
for id in range(44):
    if len(str(frame_id)) > 1:
        frames.append(rgb2gray(mpimg.imread('frame' + str(frame_id) + '.jpg')))
    else:
        frames.append(rgb2gray(mpimg.imread('frame0' + str(frame_id) + '.jpg')))

blue_spot_min = 178.713
green_spot_min = 146.654
red_spot_min = 133.808

blue_spot_max = 228.09
green_spot_max = 178.43
red_spot_max = 181.65

red_images = []
blue_frame_id = 0

for gray_frame in frames:
    blue_image = np.zeros(gray_frame.shape)
    y = gray_frame.shape[0]
    x = gray_frame.shape[1]
    for j in range(1, y - 1):
        for i in range(1, x - 1):
            if blue_spot_min < gray_frame[j, i] < blue_spot_max:
                blue_image[j, i] = 255
    if len(str(blue_frame_id)) > 1:
        cv2.imwrite('blueframe' + str(blue_frame_id) + '.jpg', blue_image)
    else:
        cv2.imwrite('blueframe0' + str(blue_frame_id) + '.jpg', blue_image)
    blue_frame_id += 1

"""
fig = plt.gcf()
fig.show()

for red_gray_image in red_images:
    plt.subplot(1, 3, 1)
    plt.imshow(red_gray_image, cmap=plt.get_cmap('gray'))
    plt.axis('off')
    fig.canvas.draw()
"""
