import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(image):
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])

color = mpimg.imread('lobo.jpg')
gray = rgb2gray(color)

y = gray.shape[0]
x = gray.shape[1]

negative = np.zeros(gray.shape)

for j in range(y):
    for i in range(x):
        negative[j,i] = 255 - gray[j,i]

plt.figure(1)

plt.subplot(1,3,1)
plt.title("Gray Negative")
plt.imshow(negative, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Gray")
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Color")
plt.imshow(color)
plt.axis('off')
plt.show()
