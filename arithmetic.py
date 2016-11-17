# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# images are Numpy arrays, stored as unsinged 8 bit integer -- this
# implies teat the values of our pixels will be in the range [0, 255]; when
# using functions like cv2.add and cv2.subtract, values willl be clipped
# to this range, event if the added or subtracted value fall outside the
# range of [0, 255]. Check out an example:
print "max of 255: " + str(cv2.add(np.uint8([200]), np.uint8([100])))
print "min of 0: "  + str(cv2.subtract(np.uint8([50]), np.uint8([100])))
print "Quiz3 1-251: "  + str(cv2.subtract(np.uint8([1]), np.uint8([251])))

    # NOTE: if you use Nupy arithmetic operations on these arrays, the value
    # willl be modulos (wrap around) instead of being clipped to the [0, 255]
    # range. This is imporant to keep in mind when working with imagesp

print "wrap around: " + str(np.uint8([200]) + np.uint8([100]))
print "wrap around: " + str(np.uint8([50]) - np.uint8([100]))
print "wrap around: quiz2 200+68 " + str(np.uint8([200]) + np.uint8([68]))
print "wrap around: quiz4 1-251 " + str(np.uint8([1]) - np.uint8([251]))


# let's increase the intensity of all pixels in our image by 100 -- we
# accomplish this by constructiong  a numpy aray that is the same size of
# our matrix (filled with ones ) and the multiplying it by 100 to create an
# array filled with 100's , then we simply add the iages together: notice
# how the image is "brighter"
M = np.ones(image.shape, dtype= "uint8") * 75
added = cv2.add(image, M)
cv2.imshow("Added", added)

(b,g,r) = added[152,61]
print "Quiz5 grand_canyn.png + Matrix(75) : pixel value : Red = {r} , Green = {g}, Blue = {b}".format(r=r,g=g,b=b
                                                                                                      )

# similarity, we can subtract 50 from all pixels in our image and make it
# darker
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image , M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)