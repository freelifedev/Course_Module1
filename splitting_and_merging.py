# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image and grab each channel: Red , Green, and Blue. It's
# Important to note that OpenCV stores an image as Numpy array with
# its cannels in reverse order! When we call cv2.split, we are
# actually getting the channels as Blue, Green, Red!
image = cv2.imread(args["image"])
(B,G,R) = cv2.split(image)

r = R[94,180]
print "Question1 . Red color at 180,94 : {}".format(r)
b = B[78,13]
print "Question2. The value of the Blue channel at x=13, y=78  {}".format(b)
g = G[5,80]
print "Question3. And the Green channel at x=80,y=5 : {}".format(g)


# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
# cv2.waitKey(0)


# question2
kernel = np.array([[-1,0,1],
       [-2,0,2],
       [-1,0,1]])

src = np.array([[202,119,154],
          [106,119,11],
          [186,48,250]])

result = kernel * src
sumrst = np.sum(result)
print "result = M: {r}, Sum = {s}".format(r=result,s=sumrst)


# question3
K = np.array([
    [1.0/9.0,1.0/9,1.0/9],
    [1.0/9,1.0/9,1.0/9],
              [1.0/9,1.0/9,1.0/9]], dtype='f')

I = np.array([[18.0,143,222],
              [233,179,97],
              [234,142,149]], dtype='f')
R = K *I
print "K ={k}, I={i}, R={rst}, Sum={s}".format(k=K,i=I,rst=R, s=np.sum(R))


# merge the image back together again
# merged = cv2.merge([B,G,R])
# cv2.imshow("Merged", merged)
# cv2.waitKey(0)
cv2.destroyAllWindows()
