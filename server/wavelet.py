# found this function on stack over flow
import numpy as np
import pywt
import cv2

def w2d(img,mode='haar', level = 1):
    #data type conversion
    #convert to greyscale
    iAmarray = img
    iAmarray = cv2.cvtColor(iAmarray,cv2.COLOR_RGB2GRAY)
    #convert to float
    iAmarray = np.float32(iAmarray)
    iAmarray/=255
    #comput coefecients
    coeffs =pywt.wavedec2(iAmarray,mode, level = level)

    #process coeffecients
    coeffs_H = list(coeffs)
    coeffs_H[0] *=0

    iAmarray_H = pywt.waverec2(coeffs_H, mode);
    iAmarray_H *= 255
    iAmarray_H = np.uint8(iAmarray_H)

    return iAmarray_H