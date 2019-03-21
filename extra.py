import math
import numpy as np
from random import randint
import matplotlib.pyplot as plt

new_image = np.zeros((300, 300, 3), dtype=int)

beam1_center = 150
beam2_center = 150
i_loop = 0
x_ball_center = 26
y_ball_center = 150

# Initial potition
plt.figure()
for y in range(300):
    for x in range(300):
        if (0 <= x <= 15) and (beam1_center - 25 <= y <= beam1_center + 25):
            pass
        elif (285 <= x <= 300) and (beam2_center - 25 <= y <= beam2_center + 25):
            pass
        elif (16 <= x <= 36) and (y_ball_center - math.sqrt( 100 - (x - x_ball_center)**2 ) <= y <= y_ball_center + math.sqrt( 100 - (x - x_ball_center)**2 )):
            pass
        else:
            new_image[y,x,0] = 255
            new_image[y,x,1] = 255
            new_image[y,x,2] = 255

plt.imshow(new_image)
plt.axis('off')
plt.pause(0.1)
plt.ioff()

new_image = np.zeros((300, 300, 3), dtype=int)

for bounce in range(6):
    i_loop += 1
    last_y = y_ball_center
    y = randint(25, 275)
    if i_loop % 2 == 1:
        x_ball_center = 275
        m = (last_y - y) / (25 - 275)
    else:
        x_ball_center = 25
        m = (last_y - y) / (275 - 25)

    for i in range(0, 251, 5):
        if i_loop % 2 == 1:
            x_ball_center = 25 + i
            y_ball_center = m*(x_ball_center-275) + y
            if beam2_center - 25 <= y <= beam2_center + 25:
                pass
            elif beam2_center <= y:
                beam2_center += 2
            elif beam2_center >= y:
                beam2_center -= 2
        else:
            x_ball_center = 275 - i
            y_ball_center = m*(x_ball_center-25) + y
            if beam1_center - 25 <= y <= beam1_center + 25:
                pass
            elif beam1_center <= y:
                beam1_center += 2
            elif beam1_center >= y:
                beam1_center -= 2
        for y_plot in range(300):
            for x_plot in range(300):
                if (0 <= x_plot <= 15) and (beam1_center - 25 <= y_plot <= beam1_center + 25):
                    pass
                elif (285 <= x_plot <= 300) and (beam2_center - 25 <= y_plot <= beam2_center + 25):
                    pass
                elif (x_ball_center - 10 <= x_plot <= x_ball_center + 10) and (y_ball_center - math.sqrt( 100 - (x_plot - x_ball_center)**2 ) <= y_plot <= y_ball_center + math.sqrt( 100 - (x_plot - x_ball_center)**2 )):
                    pass
                else:
                    new_image[y_plot,x_plot,0] = 255
                    new_image[y_plot,x_plot,1] = 255
                    new_image[y_plot,x_plot,2] = 255

        plt.imshow(new_image)
        plt.axis('off')
        plt.pause(0.001)
        plt.ioff()

        new_image = np.zeros((300, 300, 3), dtype=int)


plt.show()
