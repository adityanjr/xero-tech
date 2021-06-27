#!/usr/bin/env python
# coding: utf-8

# In[235]:


import numpy as np
import cv2 as cv
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt


# In[236]:


#img = cv.imread('C:/Users/ARCHIT/Desktop/nightimageprocessingtry.jpg',0)
#img = cv.imread('C:/Users/ARCHIT/Desktop/daytimeimageprocessingtry.jpg',0)
#img = cv.imread('C:/Users/ARCHIT/Desktop/_1.jpeg',0)
#img = cv.imread('C:/Users/ARCHIT/Desktop/image adjustments/D5.jpg',0)
#img = cv.imread('C:/Users/ARCHIT/Desktop/image adjustments/N7.jpg',0)
img = cv.imread('C:/Users/ARCHIT/Desktop/image adjustments/2.png',0)

#img = cv.cvtColor(cv.UMat(img), cv.COLOR_RGB2GRAY)
#img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

equ = cv.equalizeHist(img)
res = np.hstack((img,equ))
cv.imwrite('res.png',res)
img1 = cv.imread('res.png',0)
print(type(img1))
plt.imshow(img1)
plt.show()


# In[237]:



histr = cv.calcHist([img],[0],None,[256],[0,256]) 
hist1 = cv.calcHist([img1],[0],None,[256],[0,256])  


# In[ ]:





# In[ ]:





# In[ ]:





# In[238]:


plt.plot(histr) 
plt.show() 
plt.plot(hist1) 
plt.show() 


# In[239]:


clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv.imwrite('clahe_2.jpg',cl1)
img1= cv.imread('clahe_2.jpg',0)


# In[ ]:





# In[240]:


hist1 = cv.calcHist([img1],[0],None,[256],[0,256])  
plt.plot(hist1) 
plt.show()


# In[ ]:





# In[241]:


import cv2
import numpy as np

cl2 = cv2.resize(cl1, (640,480))
cl1 = cv2.resize(cl1, (640,480))

#gamma = 2.5
#corrected_image = np.power(cl2, gamma)


alpha = 0.8 # Contrast control (1.0-3.0)
beta = 30 # Brightness control (0-100)

corrected_image = cv2.convertScaleAbs(cl2, alpha=alpha, beta=beta)
#cv2.imshow("contrast", contrast_adjust)

img = cv2.resize(img, (640,480))
cv2.imshow("original", img)
cv2.imshow("cl1", cl1)
cv2.imshow("cl2", corrected_image)

histf = cv.calcHist([cl2],[0],None,[256],[0,256])
plt.plot(histf) 
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




