# Plastic-Net Trash Detection (an IBM Space Tech project)

PlasticNet is part of "IBM Tech for Good" to build a repo of AI models to classify types, brands of plastics, trash on beaches in ocean etc. We can scale this effort with the global community of developers participating and contributing towards this noble effort, helping on Ocean Cleanup, which can also help on the Climate Change.

## Goals

The **Goals** for our project are listed below as the following: 

* Real-time detection of different types of trash (plastic in particular) in the ocean utilizing transfer learning on different machine learning object detection architectures
* In the future, we would also like to be able to improve our model to be able to recognize logos/brands on trash, in order to detect and identify which company different types of ocean/beach trash come from
* To build a fully functional **PlasticNet** machine learning pipeline that can be easily used to train and test object detection models based from architectures such as YOLOv4, Faster-RCNN, SSD-Resnet, Efficient-DET, Tensorflow, etc. (all accessible inside a command line client)
* To provide a set of pretrained **PlasticNet** models that can be utilized for future development and improvement via transfer learning
* Implement our models to work on real-time satellite and camera footage

## Demo of Object Detection

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


OCEAN PLASTIC STATISTICS:
More than 1 million seabirds and 100,000 marine animals die from plastic pollution every year.
100% of baby sea turtles have plastic in their stomachs.
There is now 5.25 trillion macro and micro pieces of plastic in our ocean & 46,000 pieces in every square mile of ocean, weighing up to 269,000 tonnes.
Every day around 8 million pieces of plastic makes their way into our oceans.
The Great Pacific Garbage Patch is around 1.6 million square kilometers – bigger than Texas.
The world produces 381 million tonnes in plastic waste yearly – this is set to double by 2034.
50% of this is single-use plastic & only 9% has ever been recycled.
Over 2 million tonnes of plastic packaging are used in the UK each year.
88% of the sea's surface is polluted by plastic waste.
Between 8 to 14 million tonnes enters our ocean every year.
Britain contributes an estimated 1.7 million tonnes of plastic annually.
The US contributes 38 million tonnes of plastic every year.
Plastic packaging is the biggest culprit, resulting in 80 million tonnes of waste yearly from the US alone.
On UK beaches there are 5000 pieces of plastic & 150 plastic bottles for each mile.
More than 1 million plastic bags end up in the trash every minute.
The world uses over 500 billion plastic bags a year – that’s 150 for each person on Earth.
8.3 billion plastic straws pollute the world’s beaches, but only 1% of straws end up as waste in the ocean.
By 2020 the number of plastics in the sea will be higher than the number of fish.
1 in 3 fish caught for human consumption contains plastic.
Plastic microbeads are estimated to be one million times more toxic than the seawater around it.
Products containing microbeads can release 100,000 tiny beads with just one squeeze.

Source: https://www.condorferries.co.uk/plastic-in-the-ocean-statistics
