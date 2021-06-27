# Traffic_Infratech

## How to access Global Variables anywhere in any python script

from dotenv import load_dotenv </br>
import settings </br>
global_variables = settings.load_global_variables()         <------   this will return a list of global variables</br>
list-will-be-like =  [fps,num_lines, line_co_ordinates, num_droi, droi_co_ordinates, location_to_store_csv, folder_containing_videos] </br>

## Flow Of work

User inputs: FPS(optional) , DROI(Area of Interest), Lines, Folder Containing Videos/Normal Videos, Location to store csv/output files.</br>
.env file and corresponding setting.py file </br>
Gui.py </br>
main.py </br>
store_video_buffer.py </br>
take_user_inputs.py</br>
extract_frames.py </br>
preprocess_to_same_scale.py </br>
feature_enhancement.py </br>
YOLO detector, counter, tracker (Will be updated at later stage) </br>
csv_Saver.py </br>

