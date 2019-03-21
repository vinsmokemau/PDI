import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(image):
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])

color = mpimg.imread('222.jpg')
gray = rgb2gray(color)

y = gray.shape[0]
x = gray.shape[1]

plt.figure(1)
plt.subplot(2,4,1)
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.axis('off')

for i in range(1,8):
    new_image = np.zeros(gray.shape)
    for a in range(0, y):
        for b in range(0, x):
            pixel_bit = np.binary_repr(int(gray[a,b]), width=8)
            pixel_bit = pixel_bit[8-i:8]
            pixel_bit += '0'*i
            new_image[a,b] = float(int(pixel_bit, 2))
    plt.subplot(2,4,9-i)
    plt.imshow(new_image, cmap = plt.get_cmap('gray'))
    plt.axis('off')

plt.show()
