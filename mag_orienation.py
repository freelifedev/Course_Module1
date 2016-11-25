# import the necessary packages
import argparse
import cv2
import numpy as np
import math


# construct the argumet parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-l", "--lower-angle", type=float, default=175.0, help="Lower orientation angle")
ap.add_argument("-u", "--upper-angle", type=float, default=180.0, help="Upper orientaton angle")


args = vars(ap.parse_args())


# load the image, conver it to grayscale, and display the original image
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original" , image)

# compute gradients along the X and Y axis, respectively
gX = cv2.Sobel(gray, cv2.CV_64F, 1,0)
gY = cv2.Sobel(gray, cv2.CV_64F, 0,1)

# compute the gradient magnitude and orientation respectively
mag = np.sqrt((gX **2 ) + (gY**2))
orientation = np.arctan2(gY, gX) * (180/ np.pi) % 180

# find all pixels that are within the upper and low angle boundaries
idxs = np.where(orientation >= args["lower_angle"], orientation, -1)
idxs = np.where(orientation <= args["upper_angle"], idxs, -1)
mask = np.zeros(gray.shape, dtype="uint8")
mask[idxs >-1] = 255


partimg = np.array([[44,67,96],
                    [231, 184, 224],
                    [51, 253,36]])

sobelY = np.array([[-1,-2,-1],
                   [0,0,0],
                   [1,2,1]])

sobelX = np.array([[-1,0,1],
                  [-2,-0,2],
                  [-1,0,1]])

sobelPartY = partimg * sobelY
sumY = sobelPartY.sum()
print "sobel part Y sum is {}".format(sumY)

sobelPartX = partimg * sobelX
sumX = sobelPartX.sum()
print "sobel part X sum is {}".format(sumX)



# question3
xx = sumX
yy = sumY
# xx = -7
# yy = -186
mag = np.sqrt((xx**2 ) + (yy**2))
orientation = np.arctan2(yy, xx) * (180/ np.pi) % 180
theta = math.atan2(yy,xx)
print "mag = {} , orientation = {}, arctan2 = {}".format(mag, orientation, theta)
print "np.arctan2(yy, xx) = {}".format(np.arctan2(yy, xx) * 180/math.pi)


# show the images
cv2.imshow("Mask" , mask)
# cv2.waitKey(0)
