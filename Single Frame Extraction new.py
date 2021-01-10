#!/usr/bin/env python
# coding: utf-8

# # SINGLE FRAME EXTRACTION
# 
# 1. Input : A Single Video , Location of Day / Night Directory
# 
# 2. Output : Creates a FilteredData file, and annotated data file

# In[ ]:


import cv2
import time
import os


# In[ ]:


## don't change This

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


# In[ ]:


working_video_dir = input("Enter Location of the Video_directory : ") # location of the video

video_name = input("Enter Name of the video ") # Takes the Name of the video

working_dir = input("Enter the Directory of Day/Night time : ") # location of saving directory for creation of FilteredData and AnnotatedData folders

print("\n",r"Would you like to proceed [y/n] : ")

proceed_counter = input()

if proceed_counter == 'Y' or proceed_counter == 'y':
    
    # video_path : The path of the video
    
    # video_name : name of the wave
    
    # saving_dir : Location of the filtered_data folder
    
    if video_name[-3:] != "avi":
        video_name = video_name + ".avi" # add .avi to the video if not input by the user
    
    video_path = os.path.join(working_video_dir,video_name) # final path of the video
    
    saving_dir = os.path.join(working_dir,"FilteredData") # creates a FilteredData directory if not created
    annotated_dir = os.path.join(working_dir,"DataAnnotated") # creates a DataAnnotated directory if not created
    
    os.makedirs(saving_dir,exist_ok = True)
    os.makedirs(annotated_dir,exist_ok = True)
    
    video_extraction(video_path,video_name,saving_dir) # executed the main task
    
    print("\n","Processing Completed\n")
    
else:
    exit()

exit_counter = input()
exit()


# In[ ]:




