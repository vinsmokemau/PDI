import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(image):
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])

color = mpimg.imread('222.jpg')
gray = rgb2gray(color)
gray = gray[0:512,0:512]

y = gray.shape[0]
x = gray.shape[1]

for i in range(1,7):
    step = 2**i
    new_image = np.zeros(gray.shape)
    for a in range(0, y, step):
        for b in range(0, x, step):
            new_image[a:a+step, b:b+step] += np.mean(gray[a:a+step,b:b+step])
    plt.figure("Image {}".format(512/step))
    plt.imshow(new_image, cmap = plt.get_cmap('gray'))
    plt.axis('off')

plt.show()
