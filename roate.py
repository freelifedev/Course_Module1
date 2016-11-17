# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Oiginal", image)

# grab thee dimentions of the image and calculate the center of the image
(h,w) = image.shape[:2]
(cX, cY) = (w/2, h/2)

# # rotate our image by 45 degrees
# M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
# rotated = cv2.warpAffine(image, M, (w,h))
# cv2.imshow("Rotated by 45 Degrees", rotated)
#
# # rotate our image by -90 degrees
# M = cv2.getRotationMatrix2D((cX, cY) , -90, 1.0)
# rotated = cv2.warpAffine(image, M, (w,h*2))
# cv2.imshow("Rotated by -90 Degrees", rotated)
#
#
# # rotate our image around an arbitarry point rather than the center
# M = cv2.getRotationMatrix2D((cX-50, cY+50), 45, 1.0)
# rotated = cv2.warpAffine(image, M, (w,h))
# cv2.imshow("Rotated by Offset & 45 degrees", rotated)
#

# finally, let's use our helper function is imutils to rotate the image by
# 180 degrees ( lipping it upside down )
rotated = imutils.rotate(image, -30)
(b,g,r) = rotated[254,335]
# (b,g,r) = rotated[335,254]
print "After roate clockwise 30 , Pixel at (335, 254) - Red :{r} , Green :{g} , Blue :{b}".format(r=r,g=g,b=b)
cv2.imshow("Rotated by 180 Degrees", rotated)

rotated = imutils.rotate(image, 110)
(b,g,r) = rotated[136,312]
print "After rotate count-clockwise 110 , Pixel at (312,136) - Red: {r}, Green: {g}, Blue: {b}".format(r=r,g=g,b=b)
cv2.imshow("Rotated by 110 Degrees", rotated)

rotated = imutils.rotate(image, 88, (50,50))
(b,g,r) = rotated[10,10]
print "After rotate count-clockwise 88 , Pixel at (10,1) - Red: {r}, Green: {g}, Blue: {b}".format(r=r,g=g,b=b)
cv2.imshow("Rotated by 88 Degrees", rotated)




cv2.waitKey(0)

