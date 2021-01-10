import os
import io

Annotations_folder = input(
    "Enter the folder contatining all annotations files :")

dir_list = os.listdir(Annotations_folder)
dir_list.remove("classes.txt")

dir_list
count = 0

for file_name in dir_list:

    file = open(os.path.join(Annotations_folder, file_name), 'r')

    for line in file.readlines():

        entity_list = line.split()
        print(entity_list)
        entity_len = len(entity_list)-1

        count += (entity_len/4)

    file.close()

print(f"Total count of annotations : {count}")