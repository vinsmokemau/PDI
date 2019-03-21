import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

def rgb2gray(image):
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])

color = mpimg.imread('lobo.jpg')

red = color.copy()
red[:, :, 1] = 0
red[:, :, 2] = 0

green = color.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0

blue = color.copy()
blue[:, :, 0] = 0
blue[:, :, 1] = 0

yellow = color.copy()
yellow[:, :, 2] = 0

purple = color.copy()
purple[:, :, 1] = 0

cyan = color.copy()
cyan[:, :, 0] = 0

# First Plot
plt.figure(1)
plt.subplot(2,2,1)
plt.imshow(color)
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(red)
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(green)
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(blue)
plt.axis('off')

#Second Plot
plt.figure(2)
plt.subplot(2,2,1)
plt.imshow(color)
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(yellow)
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(cyan)
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(purple)
plt.axis('off')

#Third Plot
plt.figure(3)
plt.subplot(2,2,1)
plt.imshow(color)
plt.axis('off')

plt.subplot(2,2,2)
redgray = rgb2gray(red)    
plt.imshow(redgray, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2,2,3)
greengray = rgb2gray(green)    
plt.imshow(greengray, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2,2,4)
bluegray = rgb2gray(blue)    
plt.imshow(bluegray, cmap = plt.get_cmap('gray'))
plt.axis('off')

#Fourth Plot
plt.figure(4)
plt.subplot(2,2,1)
gray = rgb2gray(color)
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2,2,2)
redgray = rgb2gray(red)    
plt.imshow(redgray, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2,2,3)
greengray = rgb2gray(green)    
plt.imshow(greengray, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2,2,4)
bluegray = rgb2gray(blue)    
plt.imshow(bluegray, cmap = plt.get_cmap('gray'))
plt.axis('off')

#Fifth Plot

xx, yy = np.mgrid[0:gray.shape[0], 0:gray.shape[1]]
fig = plt.figure(figsize=(10,10))
ax = fig.gca(projection='3d')
"""
ax.plot_surface(xx, yy, gray ,rstride=1, cstride=1, cmap=plt.cm.gray,linewidth=2)
ax.view_init(80, 30)
"""
ax.plot_surface(xx, yy, gray, cmap=cm.coolwarm, linewidth=0, antialiased=False)

plt.show()