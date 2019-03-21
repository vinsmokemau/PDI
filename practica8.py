import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(image):
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])

color = mpimg.imread('lobo.jpg')
gray = rgb2gray(color)

y = gray.shape[0]
x = gray.shape[1]

r1 = float(input("Enter the r1: "))
r2 = float(input("Enter the r2: "))
s1 = float(input("Enter the s1: "))
s2 = float(input("Enter the s2: "))

m1 = (s1 - 0)/(r1 - 0)
m2 = (s2 - s1)/(r2 - r1)
m3 = (255 - s2)/(255 - r2)

new_image = np.zeros(gray.shape)

for j in range(y):
    for i in range(x):
        if 0 < gray[j,i] < r1:
            new_value = m1*(gray[j,i])
            new_image[j,i] = new_value
        elif r1 < gray[j,i] < r2:
            new_value = m2*(gray[j,i] - r1) + s1
            new_image[j,i] = new_value
        elif r2 < gray[j,i] < 256:
            new_value = m3*(gray[j,i] - r2) + s2
            new_image[j,i] = new_value

plt.figure("Images")
plt.subplot(1,3,1)
plt.title("Gray Process")
plt.imshow(new_image, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Gray")
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Color")
plt.imshow(color)
plt.axis('off')

plt.figure("T(r)")
x1 = np.linspace(0, r1)
y1 = m1*(x1 - r1) + s1
plt.plot(x1, y1, 'b')

x2 = np.linspace(r1, r2)
y2 = m2*(x2 - r2) + s2
plt.plot(x2, y2, 'b')

x3 = np.linspace(r2, 255)
y3 = m3*(x3 - 255) + 255
plt.plot(x3, y3, 'b')
plt.show()