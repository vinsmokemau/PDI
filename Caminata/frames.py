"""Extracting and Saving Video Frames using OpenCV-PythonPython."""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rgb2gray(image):
    """Transform a color image to a grayscale image."""
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])

# Opens the Video file
cap = cv2.VideoCapture('caminata_lenta.mp4')
i = 0
frames = []
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        break
    if len(str(i)) > 1:
        cv2.imwrite('frame' + str(i) + '.jpg', frame)
        frames.append(rgb2gray(mpimg.imread('frame' + str(i) + '.jpg')))
    else:
        cv2.imwrite('frame0' + str(i) + '.jpg', frame)
        frames.append(rgb2gray(mpimg.imread('frame0' + str(i) + '.jpg')))
    i += 1

cap.release()
cv2.destroyAllWindows()

"""
fig = plt.gcf()
fig.show()

for gray_frame in frames:
    plt.imshow(gray_frame, cmap=plt.get_cmap('gray'))
    fig.canvas.draw()
"""
