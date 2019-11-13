from pyimagesearch.eyetracker import EyeTracker
from pyimagesearch import imutils
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="path to where the face cascade resides")
ap.add_argument("-e", "--eye", required=True, help="path to where the eye cascade resides")
ap.add_argument("-v", "--video", required=True, help="path to the (optional) video file")
args = vars(ap.parse_args())

et = EyeTracker(args["face"], args["eye"])

if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame) = camera.read()
    if args.get("video") and not grabbed:
        break