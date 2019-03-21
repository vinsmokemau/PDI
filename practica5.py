import math
import numpy as np
import matplotlib.pyplot as plt

X0 = 0.5
Y0 = 0.5
Z0 = 2.5
eq_lambda = 0.035
alpha = 220
theta = 50
r1 = 0.01
r2 = r1
r3 = r1

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

for z in range(9):
    z *= 0.1
    y = 0.4
    x_list = [get_x(x*0.1, y, z) for x in range(5,8)]
    y_list = [get_y(x*0.1, y, z) for x in range(5,8)]
    plt.plot(x_list, y_list, 'b')

    x = 0.5
    x_list = [get_x(x, y*0.1, z) for y in range(4,7)]
    y_list = [get_y(x, y*0.1, z) for y in range(4,7)]
    plt.plot(x_list, y_list, 'b')

    y = 0.6
    x_list = [get_x(x*0.1, y, z) for x in range(5,8)]
    y_list = [get_y(x*0.1, y, z) for x in range(5,8)]
    plt.plot(x_list, y_list, 'b')

    x = 0.7
    x_list = [get_x(x, y*0.1, z) for y in range(4,7)]
    y_list = [get_y(x, y*0.1, z) for y in range(4,7)]
    plt.plot(x_list, y_list, 'b')

plt.show()