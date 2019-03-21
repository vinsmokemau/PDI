import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(image):
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])

img = mpimg.imread('lobo.jpg')
gray = rgb2gray(img)

"""
Ex:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('lobo.jpg')     
gray = rgb2gray(img)    
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.show()

"""
