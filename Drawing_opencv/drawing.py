import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3, )).tolist()

    pt = np.random.randint(0, high=300, size=(2, ))

    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# test code
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
radius = canvas.shape[1]//3


sidelen = canvas.shape[1]//30
startflag = False
for j in range(0, 30):
    for i in range(0, 16):
        if i % 2 == 0 and startflag == False and j % 2 == 0:
            startX = sidelen
            startY = sidelen * j
            startflag = True
        elif i % 2 != 0 and startflag == False and j % 2 !=0:
            startX = 0
            startY = sidelen * j
            startflag = True

        endX = startX + sidelen
        endY = startY + sidelen
        cv2.rectangle(canvas, (startX, startY), (endX, endY), red, -1)

        startX = startX + 2 * sidelen
    startflag = False


cv2.circle(canvas, (centerX, centerY), 50, green, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# # initialize our canvas as a 300x300 with 3 channels,
# # Red, Green, and Blue, with a black background
# canvas = np.zeros((300, 300, 3), dtype = "uint8")
#
# # loop over the image in 10 pixel blocks
# for (row, y) in enumerate(range(0, 300, 10)):
# 	for (col, x) in enumerate(range(0, 300, 10)):
# 		# initialize the color as red
# 		color = (0, 0, 255)
#
# 		# check to see if BOTH the row and column are
# 		# even or odd, and if so, update the background
# 		# color
# 		if row % 2 == col % 2:
# 			color = (0, 0, 0)
#
# 		# draw a 10x10 rectangle
# 		cv2.rectangle(canvas, (x, y), (x + 10, y + 10),
# 			color, -1)
#
# # draw a green circle at the center of the image
# cv2.circle(canvas, (150, 150), 50, (0, 255, 0), -1)
#
# # show the output image
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)