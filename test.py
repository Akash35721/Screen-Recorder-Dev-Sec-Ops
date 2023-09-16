from PIL import ImageGrab
import numpy as np
import cv2 


while True:
    img = ImageGrab.grab(bbox=(0, 0, 1280, 720))
    img_np = np.array(img)
    cv2.imshow('Screen Capture', img_np)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
