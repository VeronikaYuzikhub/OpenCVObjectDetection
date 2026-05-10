import argparse
import cv2

size_for_img = (15, 15)

parsedArgs = argparse.ArgumentParser()
parsedArgs.add_argument("-v", "--video", help="path to the video file")
parsedArgs.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(parsedArgs.parse_args())

def open_stream():
    img1 = cv2.VideoCapture(0)
    if not img1.isOpened():
        raise RuntimeError("Cannot open camera..")
    return img1

def load_capture(path: str):
    img2 = cv2.imread(path)
    img2 = cv2.resize(img2, size_for_img)
    return img2