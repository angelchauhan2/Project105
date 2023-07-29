import os
import cv2

path="Images/"
Images=[]
os.listdir(path)
os.splitexr(Images)
if Images in ['.gif', '.png','.jpg','.jpeg','.jfif']:
    Images = path+"/"+Images

frame = cv2.imread(Images[0])

