import cv2
import matplotlib.pyplot as plt

image = cv2.imread("lobo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0


g = image.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0

y = image.copy()
# set green and red channels to 0
y[:, :, 1] = 0

c = image.copy()
# set blue and red channels to 0
c[:, :, 0] = 0

p = image.copy()
# set blue and green channels to 0
p[:, :, 2] = 0


plt.subplot(3,3,1)
plt.imshow(b)
plt.axis('off')

plt.subplot(3,3,2)
plt.imshow(g)
plt.axis('off')

plt.subplot(3,3,3)
plt.imshow(r)
plt.axis('off')

plt.subplot(3,3,4)
plt.imshow(y)
plt.axis('off')

plt.subplot(3,3,5)
plt.imshow(c)
plt.axis('off')

plt.subplot(3,3,6)
plt.imshow(p)
plt.axis('off')

plt.subplot(3,3,7)
plt.imshow(gray)
plt.axis('off')

plt.subplot(3,3,8)
plt.imshow(gray)
plt.axis('off')

plt.subplot(3,3,9)
plt.imshow(gray)
plt.axis('off')

plt.show()

"""# RGB - Blue
cv2.imshow('B-RGB', b)

# RGB - Green
cv2.imshow('G-RGB', g)

# RGB - Red
cv2.imshow('R-RGB', r)
cv2.waitKey(0)"""
