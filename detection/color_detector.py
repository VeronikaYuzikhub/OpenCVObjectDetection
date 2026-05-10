import cv2
import numpy as np

colorLower = None
colorUpper = None

def pick_color(event, x, y, flags, frame):
    global colorLower, colorUpper
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = frame[y, x]
        color = np.uint8([[pixel]])
        hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
        hue = hsv_color[0][0][0]
        colorLower = (int(hue - 10), 100, 100)
        colorUpper = (int(hue + 10), 255, 255)

def create_mask(frame):
    if colorLower is None or colorUpper is None:
        return np.zeros(frame.shape[:2], dtype=np.uint8)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(np.uint8(blurred), cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, colorLower, colorUpper)
    mask = cv2.erode(mask, kernel=None, iterations=2)
    mask = cv2.dilate(mask, kernel=None, iterations=2)
    return mask