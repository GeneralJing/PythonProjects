import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0]*r))

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

r = 110.0 / image.shape[0]
print(int(image.shape[1]*r))

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)

resized = imutils.resize(image, width=100)
cv2.imshow("Resized1 via Function", resized)

resized = imutils.resize(image, height=50)
cv2.imshow("Resized2 via Function", resized)
cv2.waitKey(0)