# import the necessary packages
import cv2

# load the iage and show it
image = cv2.imread("florida_trip.png")
cv2.imshow("Original", image)

# cropping an image is accomplished using simple Numpy array slices .
# let's crop the face from the imae
face = image[85:250, 85:220]
cv2.imshow("Face", face)
cv2.waitKey(0)

# ... and now let's crop the entire body
body = image[173:235, 13:81]
# body = image[90:450, 0:290]
cv2.imshow("Body", body)
cv2.waitKey(0)

# boat and building
others = image[124:212, 225:380]
cv2.imshow("Boat and buildings", others)
cv2.waitKey(0)