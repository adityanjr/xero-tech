#!/usr/bin/env python
# coding: utf-8

# In[137]:


import numpy as np
import pandas as pd
import os


# In[138]:


annotation_containing_folder = "D:\\XeroData\\DataAnotation\\Week 1\\Loc 1\\Night\\annotations"  #location of the folder where annotations are saved

annotation_containing_folder = input("enter the path to the folder where annotations are saved: ")
data_info = os.listdir(annotation_containing_folder)
data_info


# In[139]:


def annotation_count(annotation_dir, file_name):
    count = 0
    df = pd.read_csv(annotation_dir, sep = " ", header = None)
    df = df.values
    column0 = np.array(df[:,0])  
    #print(column0)
    for i in range(len(column0)):
        count += 1
    return count


# In[140]:


def readFile(data_info_dict,annotation_files_folder):
    index = 0
    cnt = 0
    for key in data_info[index:]:
        file_name = key
        
        index += 1
        #print(file_name)
        
        if file_name == 'classes.txt':
            continue
            
        
        annotation_dir = os.path.join(annotation_files_folder,file_name)
        if os.path.getsize(annotation_dir) == 0:
            continue
        
        cnt += annotation_count(annotation_dir,file_name)
        
    return cnt


# In[141]:


cnt = readFile(data_info,annotation_containing_folder)
print(cnt)


# In[ ]:




