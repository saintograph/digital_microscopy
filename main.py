import cv2
import numpy as np

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

img_counter = 0
contrast = 1.00
brightness = 20.00

while rval:
    rval, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame[:,:,2] = np.clip(contrast * frame[:,:,2] + brightness, 0, 255)
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    # cv2.putText(frame, str(brightness), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
    cv2.imshow("preview", frame)
    # rval, frame = vc.read()
    key = cv2.waitKey(20)

    if key == 27: # ESCAPE pressed
        break
    elif key == 101:
        brightness += 1.00
    elif key == 113:
        brightness -= 1.00
    elif key == 32: # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

vc.release()
cv2.destroyWindow("preview")