import os, sys, random
import xml.etree.ElementTree as ET
from glob import glob
import pandas as pd
from shutil import copyfile
import shutil  
import random

annotations = glob('/home/amartya/Project_For_CV/github_YOLO/Image_dataset/BCCD/Annotations/*.xml')
random.shuffle(annotations)
print(annotations)
os.makedirs('/home/amartya/Project_For_CV/github_YOLO/Image_dataset/train_images') 
df = []
cnt = 0
for file in annotations:
    cnt+=1
    #filename = file.split('/')[-1].split('.')[0] + '.jpg'
    #filename = str(cnt) + '.jpg'
    xml_file='/'+file
    ####jpg_file=file.split('.')[0] + '.jpg'
    if cnt <=324:
        file_name = os.path.basename(xml_file)[:-4]
        parsedXML = ET.parse(file)
        for node in parsedXML.getroot().iter('object'):
            blood_cells = node.find('name').text
            xmin = int(node.find('bndbox/xmin').text)
            xmax = int(node.find('bndbox/xmax').text)
            ymin = int(node.find('bndbox/ymin').text)
            ymax = int(node.find('bndbox/ymax').text)

            row = [file_name+'.jpg', xmin, ymin, xmax, ymax,blood_cells]
            df.append(row)
        
        #to move the xml file
        destination_xml = os.path.join('/home/amartya/Project_For_CV/github_YOLO/Image_dataset/train_images',file_name) + '.xml'
        shutil.move(xml_file,destination_xml)

        #to move the jpg file 
        source_jpg = os.path.join('/home/amartya/Project_For_CV/github_YOLO/Image_dataset/BCCD/JPEGImages',file_name) + '.jpg'
        destination_jpg = os.path.join('/home/amartya/Project_For_CV/github_YOLO/Image_dataset/train_images',file_name) + '.jpg'
        shutil.move(source_jpg,destination_jpg)    
    else:
        break


data = pd.DataFrame(df, columns=['image', 'xmin', 'ymin', 'xmax', 'ymax','label'])

data[['image', 'xmin', 'ymin', 'xmax', 'ymax','label']].to_csv('Annotations-export.csv', index=False)