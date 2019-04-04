import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import skimage

def rgb2gray(image):
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])

color = mpimg.imread('lobo.jpg')
gray = rgb2gray(color)

y = gray.shape[0]
x = gray.shape[1]

new_image = np.zeros(gray.shape)
pass_high = np.zeros(gray.shape)

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
        new_image[j,i] = np.mean(gray[j-skip:j+skip,i-skip:i+skip])

pass_high = np.subtract(gray,new_image)

plt.figure("Images")
plt.subplot(1,3,1)
plt.title("Gris")
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Pasa Bajas")
plt.imshow(new_image, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Pasa Altas")
plt.imshow(pass_high, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.show()