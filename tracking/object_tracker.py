import cv2

tracked_objects = {}
object_id_counter = 0

def find_objects(mask, frame, min_radius=10):
    global tracked_objects, object_id_counter

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    current_frame_objects = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 300:
            continue

        ((x, y), radius) = cv2.minEnclosingCircle(contour)
        moments = cv2.moments(contour)
        if moments["m00"] > 0:
            center_x = int(moments["m10"] / moments["m00"])
            center_y = int(moments["m01"] / moments["m00"])
        else:
            center_x = int(x)
            center_y = int(y)

        if radius > min_radius:
            current_frame_objects.append((center_x, center_y, int(radius), area))

    current_frame_objects.sort(key=lambda x: x[3], reverse=True)
    current_frame_objects = current_frame_objects[:1]

    new_tracked_objects = {}
    matched_ids = []

    for new_x, new_y, new_radius, new_area in current_frame_objects:
        found_match = False
        for existing_id, existing_data in tracked_objects.items():
            if existing_id in matched_ids:
                continue
            old_x, old_y = existing_data["center"]
            distance = ((new_x - old_x) ** 2 + (new_y - old_y) ** 2) ** 0.5
            if distance < 100:
                new_tracked_objects[existing_id] = {"center": (new_x, new_y), "radius": new_radius, "frames_missing": 0}
                matched_ids.append(existing_id)
                found_match = True
                break

        if not found_match:
            new_tracked_objects[object_id_counter] = {"center": (new_x, new_y), "radius": new_radius, "frames_missing": 0}
            object_id_counter += 1

    for existing_id, existing_data in tracked_objects.items():
        if existing_id not in matched_ids:
            existing_data["frames_missing"] += 1
            if existing_data["frames_missing"] < 10:
                new_tracked_objects[existing_id] = existing_data

    tracked_objects = new_tracked_objects

    results = []
    for obj_id, obj_data in tracked_objects.items():
        results.append((obj_data["center"], obj_data["radius"], obj_id))
    return results