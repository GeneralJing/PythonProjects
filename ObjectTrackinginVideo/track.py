import numpy as np
import argparse
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="path to the (optional) video file")
args = vars(ap.parse_args())

blueLower = np.array([100, 67, 0], dtype="uint8")
blueUpper = np.array([255, 128, 50], dtype="uint8")

camera = cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame) = camera.read()

    if not grabbed:
        break

    blue = cv2.inRange(frame, blueLower, blueUpper)
    blue = cv2.GaussianBlur(blue, (3, 3), 0)