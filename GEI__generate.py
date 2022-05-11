## Deep Sort Result Folder -> YOLACT Silhouette Image -> GEI 
import os
import shutil
os.chdir("/home/MMI22sunki/Yolov5_DeepSort_Pytorch") ## Change Directory

dir_path = '/home/MMI22sunki/Yolov5_DeepSort_Pytorch/yolov5/rembg_copy/yolov5s_osnet_ibn_x1_0_MSMT17/crops/person'
dir_path_2= "/home/MMI22sunki/Yolov5_DeepSort_Pytorch/yolov5/rembg_copy/GEIext/A/test"

## Check Directory Existance
## Remove Folder and Files in This Path
if os.path.exists(dir_path_2):
    shutil.rmtree(dir_path_2)

if os.path.exists(dir_path):
    shutil.rmtree(dir_path)

## Python file execution 
os.system("python3 track.py --source /home/MMI22sunki/Yolov5_DeepSort_Pytorch/yolov5/data/images/fixed_video.mp4 --yolo_model yolov5s.pt  --save-crop --exist-ok --classes 0")
os.chdir("/home/MMI22sunki/Yolov5_DeepSort_Pytorch/yolov5/rembg_copy")
shutil.rmtree("/home/MMI22sunki/Yolov5_DeepSort_Pytorch/yolov5/rembg_copy/tes")
os.mkdir("tes")

os.system("python -m pathtest")
os.chdir("/home/MMI22sunki/Yolov5_DeepSort_Pytorch/yolov5/rembg_copy/GEIext/A")
os.mkdir("test")
os.chdir("/home/MMI22sunki/Yolov5_DeepSort_Pytorch/yolov5/rembg_copy/")

os.system("python -m testremove")
os.system("python -m testGEI")