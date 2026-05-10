import cv2

def draw_corners(frame, left, top, width, height, color=(0, 255, 255), length=20, thickness=2):
    cv2.line(frame, (left, top), (left + length, top), color, thickness)
    cv2.line(frame, (left, top), (left, top + length), color, thickness)

    cv2.line(frame, (left + width, top), (left + width - length, top), color, thickness)
    cv2.line(frame, (left + width, top), (left + width, top + length), color, thickness)

    cv2.line(frame, (left, top + height), (left + length, top + height), color, thickness)
    cv2.line(frame, (left, top + height), (left, top + height - length), color, thickness)

    cv2.line(frame, (left + width, top + height), (left + width - length, top + height), color, thickness)
    cv2.line(frame, (left + width, top + height), (left + width, top + height - length), color, thickness)

def draw(frame, center, radius, track_id, box_color=(0, 255, 255)):
    if radius > 10:
        height_frame, width_frame = frame.shape[:2]
        left = max(0, int(center[0] - radius))
        top = max(0, int(center[1] - radius))
        width = min(int(radius * 2), width_frame - left)
        height = min(int(radius * 2), height_frame - top)
        draw_corners(frame, left, top, width, height, color=box_color)
        cv2.putText(frame, f"id {track_id}", (left, top - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 1)