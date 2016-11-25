# import the necssary packages
import numpy as np
import argparse
import cv2

# construct the arguments parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find external contours in the image
(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
clone = image.copy()

# loop over the contours
for c in cnts:
    # compute the moments of the contou which can be used to compute the
    # centroid or "center of mass" of the region
    M = cv2.moments(c)
    cX = int (M["m10"] / M["m00"])
    cY = int (M["m01"] / M["m00"])

    # draw the center of the contour on the image
    cv2.circle(clone, (cX,cY), 10, (0,255,0), -1)


# show the output image
cv2.imshow("Centroids", clone)
cv2.waitKey(0)

clone = image.copy()

# loop over the contours again
for (i,c) in enumerate(cnts):
    # compute the area and the perimeter of the contour
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    print "Contor #%d -- area: %.2f, perimeter: %.2f" % (i+1, area, perimeter)

    # draw the contour on the image
    cv2.drawContours(clone, [c], -1, (0,255,0), 2)

    # compute the center of the contour and draw the contour number
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.putText(clone, "#%d" % (i+1), (cX-20, cY), cv2.FONT_HERSHEY_SIMPLEX,
                1.25, (255,255,255),4)

# show the output image
cv2.imshow("Contours", clone)

# clone thee original image
clone = image.copy()

# loop over the conours
for c in cnts:
    # fint a bounding box to the contour
    (x,y,w,h) = cv2.boundingRect(c)
    cv2.rectangle(clone, (x,y), (x+w, y+h), (0,255,0), 2)

# show the output image
cv2.imshow("Bounding Boxes", clone)
cv2.waitKey(0)

clone = image.copy()

# loop over the contours
for c in cnts:
    # fit a rotated bounding box to thee contour and draw a rotated bounding box
    box = cv2.minAreaRect(c)
    box = np.int0(cv2.cv.BoxPoints(box))
    cv2.drawContours(clone, [box], -1, (0,255,0),2)

# show the output image
cv2.imshow("Rotated Boundng Boxes", clone)
cv2.waitKey(0)
clone = image.copy()

# loop over the countours
for c in cnts:
    # fit aminimum enclosing circle to the contour
    ((x,y), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(clone, (int(x), int(y)), int(radius), (0,255,0),2)

# show the output image
cv2.imshow("Min-Enclosing Circles", clone)
cv2.waitKey(0)
clone = image.copy()

# loop over the contours
for c in cnts:
    # to fit an ellipse, our ontour must have at least 5 points
    if len(c) >= 5:
         # fit an ellipse to thee contour
        ellipse = cv2.fitEllipse(c)
        cv2.ellipse(clone, ellipse, (0,255,0), 2)

# show the output image
cv2.imshow("Ellipses", clone)
cv2.waitKey(0)


