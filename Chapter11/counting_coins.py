import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurrecd", image)

canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)

(_, cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("I count {} coins in this image".format(len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)

    print ("Coin #{}".format(i+1))
    coin = image[y:y+h, x:x+w]
    cv2.imshow("Coin", coin)

    mask = np.zeros(image.shape[:2], dtype="uint8")

    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    mask = mask[y:y+h, x:x+w]
    cv2.imshow("Masked coin", cv2.bitwise_and(coin, coin, mask=mask))
    cv2.waitKey(0)