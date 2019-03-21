import math
import numpy as np
import matplotlib.pyplot as plt

new_image = np.zeros((300, 250, 3), dtype = int)

for y in range(250):
    for x in range(300):
        if (180 <= x <= 240) and (100 <= y <=200):
            new_image[x, y , 2] = 255
        elif (90 <= x <= 150) and ((-2*x/3)+110 <= y <= (2*x/3)-10):
            new_image[x,y,0] = 255
        elif (60 <= x <=120) and (150 <= y <= 200+math.sqrt(900-(x-90)**2)):
            new_image[x,y,0] = 255
            new_image[x,y,1] = 255
        else:
            new_image[x,y,0] = 255
            new_image[x,y,1] = 255
            new_image[x,y,2] = 255


# First Plot
plt.figure()
plt.imshow(new_image)
plt.axis('off')
plt.show()
