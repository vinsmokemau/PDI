"""Point Detector."""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rgb2gray(image):
    """Transform a color image to a grayscale image."""
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])

color = mpimg.imread('typhosion.jpg')
gray = rgb2gray(color)

umbral = int(input('Ingrese un valor de umbral: '))
umbral_matrix = np.array([[-1, -1, -1,], [-1, 8, -1,], [-1, -1, -1,]])

y = gray.shape[0]
x = gray.shape[1]

newimage = np.zeros(gray.shape)
for j in range(1, y - 1):
    for i in range(1, x - 1):
        new_value = abs(np.sum(gray[j-1:j+2,i-1:i+2] * umbral_matrix))
        if new_value > umbral:
            newimage[j][i] = 255

plt.figure("Images")

plt.subplot(1, 2, 1)
plt.title("Gray")
plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Points")
plt.imshow(newimage, cmap=plt.get_cmap('gray'))
plt.axis('off')

plt.show()
