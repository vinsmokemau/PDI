import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

radio = 1.5
X0 = 3
Y0 = 5
Z0 = 1
eq_lambda = 0.035
alpha = 180
theta = 0
r1 = 0.01
r2 = r1
r3 = r1

X02 = 2
Y02 = 2.5
Z02 = 5

def get_x(x, y ,z):
    num = (x - X0)*math.degrees(math.cos(theta)) + (y - Y0)*math.degrees(math.sin(alpha)) - r1
    denom1 = -(x - X0)*math.degrees(math.sin(theta))*math.degrees(math.sin(alpha))
    denom2 = (y - Y0)*math.degrees(math.cos(theta))*math.degrees(math.sin(alpha))
    denom3 = -(z -Z0)*math.degrees(math.cos(alpha)) + r3 + eq_lambda
    denom = eq_lambda*(denom1 + denom2 + denom3)
    return eq_lambda*(num/denom)

def get_y(x, y, z):
    num1 = (x - X0)*math.degrees(math.sin(theta))*math.degrees(math.cos(alpha))
    num2 = (y - Y0)*math.degrees(math.cos(theta))*math.degrees(math.cos(alpha))
    num3 = (z - Z0)*math.degrees(math.sin(alpha)) - r2
    num = num1 + num2 + num3
    denom1 = -(x - X0)*math.degrees(math.sin(theta))*math.degrees(math.sin(alpha))
    denom2 = (y - Y0)*math.degrees(math.cos(theta))*math.degrees(math.sin(alpha))
    denom3 = -(z -Z0)*math.degrees(math.cos(alpha)) + r3 + eq_lambda
    denom = eq_lambda*(denom1 + denom2 + denom3)
    return eq_lambda*(num/denom)

'''
========================
3D surface (solid color)
========================

Demonstrates a very basic plot of a 3D surface using a solid color.
'''

fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v)) + 3
y = np.outer(np.sin(u), np.sin(v)) + 5
z = np.outer(np.ones(np.size(u)), np.cos(v)) + 1

# Plot the surface
ax.plot_surface(x, y, z)

ax2 = fig.add_subplot(122)

print(x)

plt.show()

