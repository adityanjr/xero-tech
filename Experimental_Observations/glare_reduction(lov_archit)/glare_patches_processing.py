import cv2
import numpy as np
from skimage import measure

image = cv2.imread('C:/Users/ARCHIT/Desktop/image adjustments/N4.jpg')#, 0).astype(np.float32) / 255
image = cv2.resize(image, (640, 480))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = image.astype(np.float32)/255

blur_img = cv2.GaussianBlur( gray, (9,9), 0 )
_,thresh_img = cv2.threshold( blur_img, 200, 255, cv2.THRESH_BINARY)
#thresh_img = cv2.erode( thresh_img, None, iterations=1 )
#thresh_img  = cv2.dilate( thresh_img, None, iterations=1 )

labels = measure.label( thresh_img, connectivity=2, background=0 )
mask = np.zeros( thresh_img.shape, dtype="uint8" )

for label in np.unique( labels ):
    # if this is the background label, ignore it
    if label == 0:
        continue
    # otherwise, construct the label mask and count the
    # number of pixels
    labelMask = np.zeros( thresh_img.shape, dtype="uint8" )
    labelMask[labels == label] = 255
    numPixels = cv2.countNonZero( labelMask )
    # if the number of pixels in the component is sufficiently
    # large, then add it to our mask of "large blobs"
    if numPixels > 300:
        mask = cv2.add( mask, labelMask )

    
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)     
#print(contours)
#print(hierarchy)

cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

gray1 = gray

for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    #print("width: " , w)
    #print("height: ", h)

    roi = gray[y:(y+h), x:(x+w)]
    #roi = cv2.resize(roi, (640, 480))
    #roi = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)
    #cv2.imshow("roi", roi)
    #print(roi)

  
    alpha = 0.7 # Contrast control (1.0-3.0)
    beta = 45 # Brightness control (0-100)

    contrast_adjust = cv2.convertScaleAbs(roi, alpha=alpha, beta=beta)
    #contrast_adjust = cv2.convertScaleAbs(roi)
    
    denoised_img = cv2.fastNlMeansDenoising(contrast_adjust,None,10,7,21)
    
    #cv2.imshow("contrast", contrast_adjust)
    #print(contrast_adjust)
    #cv2.imshow("denoised_img", denoised_img)


    gray = gray.copy()
    gray1 = gray
    gray[y: y + h, x: x + w] = contrast_adjust
    gray1[y: y + h, x: x + w] = denoised_img
    #cv2.imshow('replace', gray)

   
        
cv2.imshow('image', image)
cv2.imshow('gray', gray)
cv2.imshow('gray1', gray1)
#cv2.imshow('corrected_image', corrected_image)
#cv2.imshow('result', res)
cv2.imshow('mask', mask)
#cv2.imshow('thre', thresh_img)
cv2.waitKey()
cv2.destroyAllWindows()