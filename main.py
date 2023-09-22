# import datetime
# import numpy as np
# import cv2
# import pyautogui
# from win32api import GetSystemMetrics

# width = GetSystemMetrics(0)
# height = GetSystemMetrics(1)
# time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
# file_name = f'{time_stamp}.mp4'
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 format
# captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

# # Initialize webcam
# webcam = cv2.VideoCapture(0)  # Use index 0 for the default camera

# while True:
#     img = pyautogui.screenshot()
#     img_np = np.array(img)
#     img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

#     # Read a frame from the webcam
#     ret, frame = webcam.read()
    
#     if not ret:
#         # Break the loop if reading the frame fails
#         break

#     fr_height, fr_width, _ = frame.shape
#     img_final[0:fr_height, 0:fr_width, :] = frame[0:fr_height, 0:fr_width, :]
#     # pyautogui.onScreen('secret ',img_final)
#     cv2.imshow('Secret Capture', img_final)
#     # import pyautogui

# # ...

# # Display the image using pyautogui


#     # Write the frame to the video
#     captured_video.write(img_final)
    
#     if cv2.waitKey(10) == ord('q'):
#         break

# # Release resources
# webcam.release()
# captured_video.release()
# cv2.destroyAllWindows()

import datetime
import numpy as np
import cv2
import pyautogui
from win32api import GetSystemMetrics

# Get screen width and height
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# Create a timestamp for the video file
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 format
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

# Initialize webcam
webcam = cv2.VideoCapture(0)  # Use index 0 for the default camera

while True:
    try:
        # Capture a screenshot
        img = pyautogui.screenshot()
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        # Read a frame from the webcam
        ret, frame = webcam.read()

        if not ret:
            # Break the loop if reading the frame fails
            break

        # Overlay the webcam frame on the screenshot
        fr_height, fr_width, _ = frame.shape
        img_final[0:fr_height, 0:fr_width, :] = frame[0:fr_height, 0:fr_width, :]

        # Display the combined image
        cv2.imshow('Secret Capture', img_final)

        # Write the frame to the video
        captured_video.write(img_final)

        if cv2.waitKey(10) == ord('q'):
            break
    except KeyboardInterrupt:
        break

# Release resources
webcam.release()
captured_video.release()
cv2.destroyAllWindows()
