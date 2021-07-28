# Plastic-Net Trash Detection (an IBM Space Tech project)

## Goals

The **Goals** for our project are listed below as the following: 

* Real-time detection of different types of trash (plastic in particular) in the ocean utilizing transfer learning on different machine learning object detection architectures
* In the future, we would also like to be able to improve our model to be able to recognize logos/brands on trash, in order to detect and identify which company different types of ocean/beach trash come from
* To build a fully functional **PlasticNet** machine learning pipeline that can be easily used to train and test object detection models based from architectures such as YOLOv4, Faster-RCNN, SSD-Resnet, Efficient-DET, Tensorflow, etc. (all accessible inside a command line client)
* To provide a set of pretrained **PlasticNet** models that can be utilized for future development and improvement via transfer learning
* Implement our models to work on real-time satellite and camera footage

## Demo of Object Detection

Faster RCNN v2 PlasticNet Demo:

[![PlasticNet Demo](https://i.ytimg.com/vi/Ym2tUIaf_LY/maxresdefault.jpg)](https://youtu.be/Ym2tUIaf_LY "PlasticNet Demo")

See our (in-progress) demo here: https://docs.google.com/presentation/d/1D04HwL_vGas8BhgN-ztyltyDpgY5WQ-SIR7O7K86HQ8/edit?usp=sharing


## Test Results

See our spreadsheet documentating our test results from different trained models here: https://docs.google.com/spreadsheets/d/1mcFC2HqjohRp2_G723D8_Xd19LuuUKD-frROiY5ksOQ/edit?usp=sharing

## Resources
Labeling Images: https://cloud.annotations.ai/

YOLO: Run locally and test with images to get familiar with it (https://pjreddie.com/darknet/yolo/)

Restoring Integrity to the Oceans (RIO): https://www.oceansintegrity.com/

Pacific Whale Foundation: https://www.pacificwhale.org/

Tensorflow Object Detection API: https://github.com/tensorflow/models/tree/master/research/object_detection

Yolo with Tensorflow: https://github.com/theAIGuysCode/tensorflow-yolov4-tflite 

Forked YOLOv4 Darknet repository: https://github.com/mattokc35/darknet






# Custom Tensorflow Pipeline for Plastic-Net

## Try out our Plastic-Net Shell program! (environment to setup and train different Plastic-Net models)

Run our setup script:
```
python setup.py

```

After running the setup script, close your current terminal window and open a new one. Then, you should be able to run our cmd executable from anywhere:
```
PlasticNet
```

## Use

To begin creating a model, run the file `prepare_training.py` with the flags of the `model_name` and `model_config_name`. For example, 
```bash
 python prepare_training.py --model_name efficientdet_d0_coco17_tpu-32.tar.gz --model_config_name ssd_efficientdet_d0_512x512_coco17_tpu-8.config
```
This downloads the correct model and config file from the tensorflow model zoo, provided the names.

Trained models will be saved in the 'out' directory. Test files are automatically configured to use this directory, and you can specify which model you want to test using command line arguments. 

