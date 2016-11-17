# immport the necessary packages
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# we need to keep in mind aspect ratio so the image does not look skewed
# or distorted -- therefore, we calculate the ratio of the new image to
# the old image. Let's make our new image have a witdth of 15 pixels
r = 150.0/image.shape[1]
dim = (150, int(image.shape[0]*r))

# perform thee actual resizing of the image
resized = cv2.resize(image, dim,interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)


# what if we wanted to adjust the height of the image? we can apply
# thee same concept, again keeping in mind the aspect ration, but instead
# calculating the ratio based on height -- let's make the height of the
# resized image 50 pixels
r= 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

# perform the resizing
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)


# of course, calculating the ratio each and every time we want to resize
# and image is a real pain -- let's create a function where we can specify
# ouur target width or height, and hvae it take care of the rest for us.
w = image.shape[1]
resized = imutils.resize(image, width=w*2, inter=cv2.INTER_CUBIC )
# (b,g,r) = resized[20,74]
# (b,g,r) = resized[74,20]
(b,g,r) = resized[367,170]
print "Resized ( with width 100 ) image pixel point(20,70) : Red: {r}, Green: {g}, Blue: {b}".format(r=r,g=g,b=b)

cv2.imshow("Resized via function" , resized)



# # construct the list of interpolaion methods
# methods = [
#     ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
#     ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
#     ("cv2.INTER_AREA", cv2.INTER_AREA),
#     ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
#     ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)
# ]
#
# # looop over the interpolation methods
# for (name, method) in methods:
#     # increase the size of the image of 3x using the current interpolation
#     # method
#     resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
#     cv2.imshow("Method: {}".format(name), resized)
#     cv2.waitKey(0)



cv2.waitKey()

