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
            new_image1[j,i] = 255
        else:
            new_image1[j,i] = gray[j,i]

for j in range(y):
    for i in range(x):
        if A < gray[j,i] < B:
            new_image2[j,i] = 255
        else:
            new_image2[j,i] = 0

plt.figure(1)

plt.subplot(2,2,1)
plt.title("Gray Slay 2")
plt.imshow(new_image1, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2,2,2)
plt.title("Gray")
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2,2,3)
x1 = np.linspace(0, A)
y1 = (x1)
plt.plot(x1, y1, 'b')

x1 = np.linspace(A, A+1)
m1 = (255 - A)/(A+1 - A)
y1 = m1*(x1-A) + A
plt.plot(x1, y1, 'b')

x1 = np.linspace(A+1, B)
m1 = (254 - 255)/(B - A+1)
y1 = m1*(x1-B) + 254
plt.plot(x1, y1, 'b')

x1 = np.linspace(B, B+1)
m1 = (B - 254)/(B+1 - B)
y1 = m1*(x1-B) + 254
plt.plot(x1, y1, 'b')

x1 = np.linspace(B, 255)
y1 = (x1)
plt.plot(x1, y1, 'b')

plt.figure(2)

plt.subplot(2,2,1)
plt.title("Gray Slay 1")
plt.imshow(new_image2, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2,2,2)
plt.title("Gray")
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.axis('off')

plt.subplot(2,2,3)
x1 = np.linspace(0, A)
m1 = (1 - 0)/(A - 0)
y1 = m1*(x1)
plt.plot(x1, y1, 'b')

x1 = np.linspace(A, A+1)
m1 = (255 - 1)/(A+1 - A)
y1 = m1*(x1-A) + 1
plt.plot(x1, y1, 'b')

x1 = np.linspace(A+1, B)
m1 = (254 - 255)/(A+1 - B)
y1 = m1*(x1-B) + 255
plt.plot(x1, y1, 'b')

x1 = np.linspace(B, B+1)
m1 = (1 - 254)/(B+1 - B)
y1 = m1*(x1-B) + 254
plt.plot(x1, y1, 'b')

x1 = np.linspace(B+1, 255)
m1 = (0 - 1)/(255 - B+1)
y1 = m1*(x1-B+1) + 1
plt.plot(x1, y1, 'b')

plt.show()