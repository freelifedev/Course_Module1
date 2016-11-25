# import the necessary packages
import numpy as np
import cv2

# first, let's draw a rectangle
rectangle = np.zeros((300,300), dtype = "uint8")
cv2.rectangle(rectangle, (25,25), (275, 275), 255 , -1)
cv2.imshow("Rectangle", rectangle)


# secondly , let's draw a circle
circle = np.zeros((300,300), dtype= "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

# A bitwise 'AND' is only True when both rectangle and circle have
# a value that is 'ON'. Simply put, the bitwise AND function
# examins every pixel in rectangle and circle. If both pixels
# ave a value greater than zero, that pixl is turned 'ON' (i,e
# set to 255 in the output image). If both pixels are not greater
# than zero, then the output pixel is left 'OFF' with a value o 0.
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

# A bitwise 'OR' examines every pixel in rectanglee and circle. If
# EITHER pixel in rectangle or circle greatr then zero, then
# the output pixel has a value of 255, otherwise it it 0.
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

# bitwise 'XOR' is identical to thee 'OR' function, with one
# exception: bote rectangle and circle are not allowed to BOTH
# have values  greater than 0.
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

# Finally, the bitwise 'NOT' inverts the values of the pixels. Pixels
# with a value of 255 become 0, and pixels with a valu of 0 become
# 255.
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)


cv2.waitKey(0)