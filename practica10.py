import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(image):
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])

color = mpimg.imread('lobo.jpg')
gray = rgb2gray(color)

y = gray.shape[0]
x = gray.shape[1]

A = float(input("Enter the A: "))
B = float(input("Enter the B: "))

new_image1 = np.zeros(gray.shape)
new_image2 = np.zeros(gray.shape)

for j in range(y):
    for i in range(x):
    	if A < gray[j,i] < B:
            new_image[j,i] = 255
        else:
            new_image[j,i] = 0
