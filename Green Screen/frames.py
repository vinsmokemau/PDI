"""Extracting and Saving Video Frames using OpenCV-PythonPython."""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Opens the Video file
cap = cv2.VideoCapture('00039.MTS')
i = 0
frames = []
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        break
    if len(str(i)) > 1:
        cv2.imwrite('frame' + str(i) + '.jpg', frame)
    else:
        cv2.imwrite('frame0' + str(i) + '.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()
