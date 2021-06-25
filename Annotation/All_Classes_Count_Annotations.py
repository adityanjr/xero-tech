#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import io

total_classes = 20
all_annotation_count = []
for _ in range(total_classes):
    all_annotation_count.append(0)


Annotations_folder = input("Enter the folder contatining all annotations files :")


dir_list = os.listdir(Annotations_folder)

dir_list.remove("classes.txt")


dir_list

count = 0

for file_name in dir_list:
    try :
    	file = open(os.path.join(Annotations_folder,file_name),'r')
        	
    	for line in file.readlines():
	        all_annotation_count[int(line.split(" ")[0])] = all_annotation_count[int(line.split(" ")[0])]+1
     #   	entity_list = line.split()
     #   	print(entity_list)
     #  	entity_len = len(entity_list)-1
        	
     #  	count += (entity_len/4)
    	
    	file.close()
    except :
    	print("Some Error Here!!!")




#print(f"Total count of annotations : {count}")
print(all_annotation_count)
