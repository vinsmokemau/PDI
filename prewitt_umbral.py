"""Prewitt's Filter."""
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

umbral = int(input('Ingrese un valor de umbral: '))

prewitt_image = np.zeros(gray.shape)
prewitt_image_x = np.zeros(gray.shape)
prewitt_image_y = np.zeros(gray.shape)

for j in range(1, y - 1):
    for i in range(1, x - 1):
        new_value_x = abs(
            (gray[j - 1, i + 1] + gray[j, i + 1] + gray[j + 1, i + 1]) - (gray[j - 1, i - 1] + gray[j, i - 1] + gray[j + 1, i - 1])
        )
        new_value_y = abs(
            (gray[j + 1, i - 1] + gray[j + 1, i] + gray[j + 1, i + 1]) - (gray[j - 1, i - 1] + gray[j - 1, i] + gray[j - 1, i - 1])
        )
        new_value = new_value_x + new_value_y
        if new_value_x > umbral:
            prewitt_image_x[j, i] = new_value_x
        if new_value_y > umbral:
            prewitt_image_y[j, i] = new_value_y
        if new_value_x > umbral:
            prewitt_image[j, i] = new_value

plt.figure("Images")

plt.subplot(2, 2, 1)
plt.title("gray")
plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title("Prewitt X")
plt.imshow(prewitt_image_x, cmap=plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title("Prewitt Y")
plt.imshow(prewitt_image_y, cmap=plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title("Prewitt")
plt.imshow(prewitt_image, cmap=plt.get_cmap('gray'))
plt.axis('off')

plt.show()
