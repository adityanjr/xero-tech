#!/usr/bin/env python
# coding: utf-8

# In[9]:


##Import directories

import cv2
import time
import os


# In[10]:


# ### Working Directory

# In[11]:


working_directory = input(" Enter your working week directory videos: ") ##Enter here your working week - Nighttime/Daytime directory

target_directory = os.path.join(working_directory,"FilteredData") ## Don't change this ( Used to create a New Folder)
print(target_directory)
os.makedirs(target_directory,exist_ok = True)

os.makedirs(os.path.join(working_directory,"DataAnnotated"),exist_ok = True)


# ### Setting the directories

# In[12]:


##Don't Change this - Also, don't change name of the Files - Make sure all videos are in folder Video

video_files = [os.path.join(working_directory,"videos",x) for x in os.listdir(os.path.join(working_directory,"videos"))]
video_containing_folder = os.path.join(working_directory,"videos")
data_info = os.listdir(video_containing_folder)


# ### Frame Extraction Function

# In[13]:


##Don't Change this

def video_extraction(video_add,video_name,target_folder,fps_rate= 4,second_s = 1):
    Video = cv2.VideoCapture(video_add)
    print("Accessing Video : ", video_add)
    print("Video dimension : ({},{},3)".format(Video.get(3),Video.get(4)))
    frame_rate = int(Video.get(5))
    print("Frame Rate : {}".format(frame_rate))
    
    if frame_rate <=4:
        print("Frame Rate Of Video is less than 4")
        return
    frames = int(frame_rate/fps_rate)
    print("Extraction of frames at : {} ".format(frames))
    
    total = 1
    sec_frame_count = 1
    total_frame_count=0   
    second_skip = second_s
    while Video.isOpened():
        ret,frame = Video.read()
        if ret != True:
            break
            
        height,width = frame.shape[:-1]
        sec_frame_count+=1
        if sec_frame_count>frame_rate:
            sec_frame_count = 1  
            total += 1
            
        if int(sec_frame_count%frames) == 0:
            if second_skip%3==0:
                total_frame_count +=1
                cv2.imwrite(target_folder+"\\"+video_name+"_{}_{}_{}.jpg".format(total_frame_count,total,sec_frame_count//frames),frame)      
                second_skip += 1
            else:
                second_skip += 1
    print("Video {}-->{} Processed ".format(video_name,target_folder),"\n")
    Video.release()
    cv2.destroyAllWindows()


# ### Setting PreProcessing Function

# In[14]:


##Don't Change this

def preprocess_data(data_info_dict,target_dir,video_files_folder):
    index = 0
    for key in data_info[index:]:
        print("Working On Index : {}".format(index))
        video_name = key
        index += 1
        print(video_name)
        saving_dir = target_dir
        video_dir = os.path.join(video_files_folder,video_name)
        video_extraction(video_dir,video_name,saving_dir)


# In[15]:

##Don't Change this

preprocess_data(data_info,target_directory,video_containing_folder)
