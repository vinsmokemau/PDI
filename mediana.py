import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import skimage

def rgb2gray(image):
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])

color = mpimg.imread('lobo.jpg')
salt_pepper = skimage.util.random_noise(color, mode='s&p', seed=None, clip=True)
gray = rgb2gray(salt_pepper)

y = gray.shape[0]
x = gray.shape[1]

new_image = np.zeros(gray.shape)

loop = True

while loop:
    mask = int(input("Ingresa el tamaño de la máscara: "))
    if mask % 2 == 0:
        print("El tamaño de la máscara debe ser impar")
    else:
        loop = False

skip = mask // 2

for j in range(skip,y-skip):
    for i in range(skip,x-skip):
        new_image[j,i] = np.median(np.sort(gray[j-skip:j+skip,i-skip:i+skip], axis=None))

plt.figure("Images")
plt.subplot(1,2,1)
plt.title("Salt & Pepper")
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Median Filter")
plt.imshow(new_image, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.show()