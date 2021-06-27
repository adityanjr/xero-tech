#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import numpy as np
from skimage import measure
# %matplotlib inline
from matplotlib import pyplot as plt

class night_time:
    
    def local_patch_method(og_image):
        image = cv2.resize(og_image, (640, 480))
        gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = image.astype(np.float32)/255
        blur_img = cv2.GaussianBlur( gray, (9,9), 0 )
        _,thresh_img = cv2.threshold( blur_img, 200, 255, cv2.THRESH_BINARY)
        labels = measure.label( thresh_img, connectivity=2, background=0 )
        mask = np.zeros( thresh_img.shape, dtype="uint8" )
        for label in np.unique( labels ):
            if label == 0:
                continue
            labelMask = np.zeros( thresh_img.shape, dtype="uint8" )
            labelMask[labels == label] = 255
            numPixels = cv2.countNonZero( labelMask )
    
            if numPixels > 300:
                
            
                mask = cv2.add( mask, labelMask)
                contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)     
                cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
                gray1 = gray
                for contour in contours:
                    x,y,w,h = cv2.boundingRect(contour)
                    image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
                    roi = gray[y:(y+h), x:(x+w)]
                alpha = 0.7 # Contrast control (1.0-3.0)
                beta = 45 # Brightness control (0-100)
                    
 
                contrast_adjust = cv2.convertScaleAbs(roi, alpha=alpha, beta=beta)
                denoised_img = cv2.fastNlMeansDenoising(contrast_adjust,None,10,7,21)
    
   


                gray = gray.copy()
                gray1 = gray
                gray[y: y + h, x: x + w] = contrast_adjust
                gray1[y: y + h, x: x + w] = denoised_img
                return gray1
    def cl2_method(image):
        clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl1 = clahe.apply(img)
        return cl1
    
        
    


# In[ ]:


class day_time:
    


# In[ ]:





# In[ ]:





# In[ ]:




