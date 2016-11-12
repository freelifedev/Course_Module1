# import the necesary packages
import numpy as np
import cv2

def translate(image, x,y):
    # define the translation matrix and perform the translation
    M = np.float32([[1,0,x], [0,1,y]])
    shifted = cv2.warpAffine(image, M , (image.shape[1], image.shape[0]))

    # return the translated image
    return shifted
