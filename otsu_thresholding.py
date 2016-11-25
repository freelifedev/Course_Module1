# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse thee arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image , convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)
cv2.imshow("Image", image)

# apply Otsu's automatic thresholding -- Ots's method automatically
# determins the best threshold value 'T' for us
(T, thresInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
# cv2.imshow("Threshold", thresInv)
print "Otsu's thresholding value: {}".format(T)

# finally, we can visualize only the masked regions in the image
# cv2.imshow("Output7777e", cv2.bitwise_and(image, image, mask = thresInv))
cv2.waitKey(0)

