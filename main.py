import cv2
import numpy as np
from collections import deque
from capture.camera import args, open_stream
from detection.color_detector import create_mask
from tracking.object_tracker import find_objects
from display.renderer import draw
import detection.color_detector as color_detector

pts = deque(maxlen=args["buffer"])
camera = open_stream()
current_frame = None

def pick_color(event, x, y, flags, param):
    global colorLower, colorUpper
    if event == cv2.EVENT_LBUTTONDOWN and current_frame is not None:
        if 0 <= y < current_frame.shape[0] and 0 <= x < current_frame.shape[1]:
            pixel = current_frame[y, x]
            color = np.uint8([[pixel]])
            hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
            hue = hsv_color[0][0][0]
            color_detector.colorLower = (int(hue - 10), 100, 100)
            color_detector.colorUpper = (int(hue + 10), 255, 255)

cv2.namedWindow("Tracker")
cv2.setMouseCallback("Tracker", pick_color)

while True:
    return_value, frame = camera.read()
    if not return_value:
        break

    current_frame = frame

    if color_detector.colorLower is None:
        cv2.imshow("Tracker", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    mask = create_mask(frame)
    objects = find_objects(mask, frame)

    for center, radius, track_id in objects:
        cx, cy = int(center[0]), int(center[1])
        if 0 <= cy < frame.shape[0] and 0 <= cx < frame.shape[1]:
            object_color = tuple(map(int, frame[cy, cx]))
        else:
            object_color = (0, 255, 255)
        draw(frame, center, radius, track_id, box_color=object_color)

    if len(objects) > 0:
        pts.appendleft(objects[0][0])

    cv2.imshow("Tracker", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()