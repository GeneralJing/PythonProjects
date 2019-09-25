from pyimagesearch.zernikemoments import ZernikeMoments
from imutils.paths import list_images
import numpy as np
import argparse
import pickle
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--sprites", required=True, help="Path where the spirites will be stored")
ap.add_argument("-i", "--index", required=True, help="Path to where the index file will be stored")
args = vars(ap.parse_args())

desc = ZernikeMoments(21)
index = {}

for spritePath in list_images(args["sprites"]):
    pokemon = spritePath[spritePath.rfind("/") + 1:].replace(".png", "")
    image = cv2.imread(spritePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
