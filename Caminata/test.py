# Extracting and Saving Video Frames using OpenCV-PythonPython
import cv2

# Opens the Video file
cap = cv2.VideoCapture('00023.MTS')
i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        break
    cv2.imwrite('kang' + str(i) + '.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()
