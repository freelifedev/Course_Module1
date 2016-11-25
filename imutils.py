# import the necesary packages
import numpy as np
import cv2

def translate(image, x,y):
    # define the translation matrix and perform the translation
    M = np.float32([[1,0,x], [0,1,y]])
    shifted = cv2.warpAffine(image, M , (image.shape[1], image.shape[0]))

    # return the translated image
    return shifted

def rotate(image, angle, center=None, scale = 1.0):
    # grab the dimensions of the image
    (h,w) = image.shape[:2]

    # ifthe center is None, initialize it as the center of
    # the image
    if center is None:
        center = (w/2, h/2)

    # perform the rotation
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M , (w,h))

    # return the rotated immage
    return rotated

def resize(image, width=None, height=None, inter = cv2.INTER_AREA):
    # initialize the dimentions of the image to be resized and
    # grab the image size
    dim = None
    (h,w) = image.shape[:2]

    # if both th width and heightare None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimentions
        r = height /float(h)
        dim = (int(w*r), height)

    # otherwise, the height is None
    else :
        # calculate the ratio of the width and construct the
        # dimentions
        r = width / float(w)
        dim = (width , int(h*r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # erturn the resized image
    return resized


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0-sigma)*v))
    upper = int(min(255, (1.0+sigma) *v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged
