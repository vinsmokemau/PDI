"""Change the Green Screen for Another video."""
import numpy as np
import cv2


def change_green_screen(image, frame_id):
    """Change the green background for an image."""
    image_copy = np.copy(image)
    image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

    lower_green = np.array([0, 70, 0])
    upper_green = np.array([80, 255, 100])

    mask = cv2.inRange(image_copy, lower_green, upper_green)

    masked_image = np.copy(image_copy)
    masked_image[mask != 0] = [0, 0, 0]

    background_image = cv2.imread(
        'new_screen_frames/frame{}.jpg'.format(
            frame_id
        )
    )
    background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

    background_image[mask == 0] = [0, 0, 0]

    final_image = background_image + masked_image

    return final_image

cap = cv2.VideoCapture('00034.MTS')

i = 0

while(cap.isOpened()):
    ret, frame = cap.read()

    if len(str(i)) > 1:
        frame_id = str(i)
    else:
        frame_id = '0' + str(i)
    i += 1

    hsi = change_green_screen(frame, frame_id)

    cv2.imshow('frame', hsi)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
