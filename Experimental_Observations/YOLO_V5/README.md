1. Install Pytorch
2. pip install -r requirements.txt
3. How to install pytorch : https://pytorch.org/get-started/locally/
4. Change Working Directory to YOLO_V5
5. python detect.py --source <path_of_video_or_img> --weights <model_weights_name> --conf <confidence_value_between_0.00_and_1.00>
6. Output will be stored in YOLOv5->inference->output
</br>
</br>
Reference Speeds on i7 and NVIDIA GTX 1050 Ti </br>
</br>
Total_time = 309 sec </br>
170 mb wala yolov5x.pt </br>
0.085s per frame </br>
</br>
total time = 62.5 sec </br>
14 mb wala yolov5s.pt </br>
per frame = 0.014s </br>
</br>
Total Time = 105s </br>
40mb wala yolov5m.pt </br>
per frame 0.026 </br>
</br>
Total Time = 175s </br>
per frame : 0.048s </br>
yolov5l : 90mb wala </br>
