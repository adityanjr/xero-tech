#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import cv2
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
import os


# In[25]:


def frameProcessing(img):
    
    equ = cv2.equalizeHist(img)
    res = np.hstack((img,equ))
    cv2.imwrite('res.png',res)
    img1 = cv2.imread('res.png',0)
    #print(type(img1))
    #plt.imshow(img1)
    #plt.show()
    
    histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
    hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])
    
    #plt.plot(histr) 
    #plt.show() 
    #plt.plot(hist1) 
    #plt.show() 
    
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img)

    cv2.imwrite('clahe_2.jpg',cl1)
    img1= cv2.imread('clahe_2.jpg',0)
    
    hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])  
    #plt.plot(hist1) 
    #plt.show()
    
    #cl1 = cv2.resize(cl1, (640,480))
    
    alpha = 0.8 # Contrast control (1.0-3.0)
    beta = 30 # Brightness control (0-100)

    corrected_image = cv2.convertScaleAbs(cl1, alpha=alpha, beta=beta)
    
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl2 = clahe.apply(corrected_image)
    #cv2.imshow("cl2", cl2)

    corrected_image = cv2.convertScaleAbs(cl2, alpha=alpha, beta=beta)
    #cv2.imshow("cl2_adjusted", cl2)
    
    corrected_image = cv2.cvtColor(corrected_image, cv2.COLOR_GRAY2RGB)
    
    return corrected_image
    
    


# In[26]:


# some code to extract frames from a video and store them in a particular directory

def Extract_Frames(path = "C:/Users/ARCHIT/Desktop/VideoProcess/vid2.mp4", extr_img_dir="C:/Users/ARCHIT/Desktop/VideoProcess/Extr_imgs"):
    count = 0
    vidcap = cv2.VideoCapture(path)
    framerate = vidcap.get(5)
    success, image = vidcap.read()
    success = True
    frameSize = (image.shape[1], image.shape[0])
    print(frameSize)
    out = cv2.VideoWriter('C:/Users/ARCHIT/Desktop/VideoProcess/final_vid2.avi',cv2.VideoWriter_fourcc(*'DIVX'), framerate, frameSize) ## Output video Path 
    #out = cv2.VideoWriter('C:/Users/ARCHIT/Desktop/VideoProcess/final_vid.avi',cv2.VideoWriter_fourcc(*'MJPG'), framerate, frameSize)
    while success:# and count <1600 :
        try:
            #vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*333))#1000))
            success,image = vidcap.read()
            if not success:
                break
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Here the image will have only one channel
            #image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
            
            image = frameProcessing(image)
            
            #cv2.imshow("image", image)            
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            
            #print (f'Read a new frame + {(image.shape[1], image.shape[0])}' + str(count) + ' :', success,)
            out.write(image)
            # cv2.imwrite( os.path.join(extr_img_dir , "frame%d.jpg" % count), image)          # save frame as JPEG file
            count = count + 1
            #cv2_imshow(image)
        except Exception as e:
            print("Some error occured here : " + e)
            #break
    out.release()
            
Extract_Frames()
print("done!")


# In[ ]:





# In[ ]:





# In[ ]:




