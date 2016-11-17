# import the necessary packages
import argparse
import cv2
import imutils

# construct the argumen parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# flip the image horizontally
flipped = cv2.flip(image, 1)
(b,g,r) = flipped[235,259]
print "Flipped image pixel value : Red ={r}, Green = {g}, Blue = {b}".format(r=r,g=g,b=b)

cv2.imshow("Flipped Horizontally", flipped)

rotated = imutils.rotate(flipped, 45)
cv2.imshow("Rotated by 45 Degrees", rotated)

flipped = cv2.flip(rotated, 0)
(b,g,r) = flipped[189,441]
print "Flipped vertically , Pixel (441,189) is Red = {r}, Green = {g}, Blue={b}".format(r=r,g=g,b=b)
cv2.imshow("Flipped vertically", flipped)

# # flip the image vertically
# flipped = cv2.flip(image, 0)
# cv2.imshow("Flipped Vertically", flipped)
#
# # flip the image alone both axes
# flipped = cv2.flip(image, -1)
# cv2.imshow("Flipped Horizontally & Vetically", flipped)


cv2.waitKey(0)