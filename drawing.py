# import the necessary packages
import numpy as np
import cv2

# initialize our canvas as a 300*300 with 3 channels, Red, Green,
# and Blue, with a black background
canvas = np.zeros((800,1300,3), dtype="uint8")

#draw a gren line from the top-left corner of our canvas to the
# bottom-right
green = (0,255,0)
cv2.line(canvas, (0,0), (300,300), green)
cv2.imshow("Canvas", canvas)
# cv2.waitKey()

# now, draw a 3 pixel thick red lne from the top-right corner to the
# bottom-left
red = (0,0,255)
cv2.line(canvas, (300,0), (0,300), red,3)
cv2.imshow("Canvas", canvas)
# cv2.waitKey()

# draw a green 50*0 pixel square , starting at 10*10 and ending a 60*60
cv2.rectangle(canvas, (10, 10), (60,60), green)
cv2.imshow("Canvas",canvas)
# cv2.waitKey(0)

# draw another rectangle , this time we'll make it red and 5 pixels thick
cv2.rectangle(canvas, (50,200), (200,225), red , 5)
cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# let's draw one last rectangle: blue and filled in
blue = (255,0,0)
cv2.rectangle(canvas, (200,50), (225,125), blue, -1)
cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# reset our canvas and draw a white circle at the center of the canvas with
# increasing redii - from 25 pixels to 150 pixels
canvas = np.zeros((800, 300, 3), dtype="uint8")
(centerX, centerY) =(canvas.shape[1] /2, canvas.shape[0] /2)
white = (255, 255, 255)

for r in xrange(0,175,25):
    cv2.circle(canvas, (centerX, centerY), r, white)

# show our work of art
cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# let's go crazy and draw 25 random circles
for i in xrange(0,25):
    # randomly generate a radius size between 5 and 200, generate a random
    # color, and then pck a random point on ou canvas where the circle
    # will be drawn
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))

    # draw our random circle
    cv2.circle(canvas, tuple(pt), radius, color, -1)

# show our materpiece
cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)


# load the image of Adrian n Folorida
image = cv2.imread('florida_trip.jpg')

# draw a circle around my face, two filled in circles covering my ecyes, and
# a rectangle surrounding my mouth
cv2.circle(image, (168,188), 90, (0,0,255), 2)
cv2.circle(image, (150,164), 10 , (0,0,255), -1)
cv2.circle(image, (192,174), 10, (0,0,255), -1)
cv2.rectangle(image, (134,200), (186,218), (0,0,25), -1)

# show the output image
cv2.imshow('Output', image)
cv2.waitKey(0)