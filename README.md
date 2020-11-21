# Blood_Cell_Detection_Using_YOLO_TensorFlow

This repo will help you to train image detection using the state-of-the-art YOLOv3 computer vision algorithm on BCC Dataset.This repo works with TensorFlow 2.3 and Keras 2.4.
With this model we can detect RBC, WBC,PLATELETS.

### Input
![Input_Image](/Utils/BloodImage_00206.jpg)

### Output
![Input_Image](/Utils/BloodImage_00206_detected.jpg)


## Repo structure
+ [`1_Image_Annotation`](/1_Image_Annotation/): Scripts on annotating images
+ [`2_Training`](/2_Training/): Scripts on training your YOLOv3 model
+ [`3_Inference`](/3_Inference/): Scripts on testing your trained YOLO model on new images and videos
+ [`Data`](/Data/): Input Data, Output Data, Model Weights and Results
+ [`Utils`](/Utils/): Utility scripts used by main scripts
+ [`Image_dataset`](/Image_dataset/): BCCD Dataset is a small-scale dataset for blood cells detection.
