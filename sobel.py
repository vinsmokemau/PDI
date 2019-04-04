"""Sobel's Filter."""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rgb2gray(image):
    """Transform a color image to a grayscale image."""
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])

color = mpimg.imread('lobo.jpg')
gray = rgb2gray(color)

y = gray.shape[0]
x = gray.shape[1]

sobel_image = np.zeros(gray.shape)
sobel_image_x = np.zeros(gray.shape)
sobel_image_y = np.zeros(gray.shape)

for j in range(1, y - 1):
    for i in range(1, x - 1):
        image_x = abs(
            (gray[j - 1, i + 1] + 2 * gray[j, i + 1] + gray[j + 1, i + 1]) - (gray[j - 1, i - 1] + 2 * gray[j, i - 1] + gray[j + 1, i - 1])
        )
        if image_x > 255:
            sobel_image_x[j, i] = 0
        else:
            sobel_image_x[j, i] = image_x
        image_y = abs(
            (gray[j + 1, i - 1] + 2 * gray[j + 1, i] + gray[j + 1, i + 1]) - (gray[j - 1, i - 1] + 2 * gray[j - 1, i] + gray[j - 1, i - 1])
        )
        if image_y > 255:
            sobel_image_y[j, i] = 0
        else:
            sobel_image_y[j, i] = image_y
        sobel_image[j, i] = sobel_image_x[j, i] + sobel_image_y[j, i]

plt.figure("Images")

plt.subplot(2, 2, 1)
plt.title("gray")
plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title("Sobel X")
plt.imshow(sobel_image_x, cmap=plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title("Sobel Y")
plt.imshow(sobel_image_y, cmap=plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title("Sobel")
plt.imshow(sobel_image, cmap=plt.get_cmap('gray'))
plt.axis('off')

plt.show()
