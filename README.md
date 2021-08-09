# Plastic-Net Trash Detection (an IBM Space Tech Team project)


**PlasticNet** is an "**IBM Tech for Good**" open-source project developed by the IBM Space Tech team to build a repository of AI object detection models to classify types/brands of plastics, trash on beaches, trash in the ocean, etc. We can scale this effort with the global community of developers participating and contributing towards this noble effort, with long term goals to help with ocean cleanup and positively impact climate change.

For more information on how to get started, check out the **PlasticNet Wiki** [here](https://github.com/IBM/PlasticNet/wiki)!

## Goals

The **Goals** for our project are listed below as the following: 

* Real-time detection of different types of trash (plastic in particular) in the ocean utilizing transfer learning on different machine learning object detection architectures
* In the future, we would also like to be able to improve our model to be able to recognize logos/brands on trash, in order to detect and identify which company different types of ocean/beach trash come from
* To build a fully functional **PlasticNet** machine learning pipeline that can be easily used to train and test object detection models based from architectures such as YOLOv4, Faster-RCNN, SSD-Resnet, Efficient-DET, Tensorflow, etc. (all accessible inside a command line client)
* To provide a set of pretrained **PlasticNet** models that can be utilized for future development and improvement via transfer learning
* Implement our models to work on real-time satellite and camera footage

## Basic Project Structure and Technologies Used (feat. diagram)

![img](/img/plasticnetdiagram.png)

The PlasticNet command line program combines YOLOv4 and Tensorflow Object Detection API technologies into a single, easily usable machine learning pipeline CLI. Collaborators can use the PlasticNet CLI to prepare models  for training (via transfer learning from the provided pre-trained PlasticNet models), train custom detection models built upon pre-trained PlasticNet models, export the trained models, and finally test the trained models.  The CLI was created so these steps can all be done with a few simple commands, seen [here](https://github.ibm.com/spacetech-interns/PlasticNet/wiki/Utilizing-the-PlasticNet-Command-Line-Client). Initially trained via transfer learning from pre-trained YOLO weights [(found here)](https://github.com/mattokc35/darknet#pre-trained-models), and pre-trained Tensorflow models (from the [Tensorflow Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)), our official **PlasticNet Model Zoo** (found [here](https://github.com/IBM/PlasticNet/blob/main/ModelZoo.md)) can be used by collaborators for the further improvement/development of new PlasticNet object detection models. For labeling images, we utilized IBM's Cloud Annotations (instructions found [here](https://github.ibm.com/spacetech-interns/PlasticNet/wiki/Creating-Your-Own-Dataset-for-Custom-Training)).

## Demo of Object Detection

**YOLOv4 9 class v3 PlasticNet Demo (**best YOLO model**, with face masks and fishing nets included):**

*(Click to watch)*

[![PlasticNet Demo](https://img.youtube.com/vi/eQRkLSfv8CY/0.jpg)](https://youtu.be/eQRkLSfv8CY "YOLO PlasticNet Demo")

**Tensorflow Faster RCNN v3 7 class PlasticNet Transfer Learning Demo:**

*(Click to watch)*

[![PlasticNet Demo](https://img.youtube.com/vi/qGlRkV5cWzQ/0.jpg)](https://youtu.be/qGlRkV5cWzQ "Tensorflow Faster-RCNN PlasticNet Demo")

See our (in-progress) demo here: https://docs.google.com/presentation/d/1D04HwL_vGas8BhgN-ztyltyDpgY5WQ-SIR7O7K86HQ8/edit?usp=sharing


## Get Started

To get started with PlasticNet, you first must clone the repository using the following command:

```
git clone https://github.com/IBM/PlasticNet.git
```

Once the repository is cloned, you can run the following command in the python evironment of your choice. (NOTE: It is recommended that this is done in a new python environment, to avoid any issues between package dependencies)

The setup script currently only supports MacOS, but Windows and Linux support will be added soon.
```
cd PlasticNet && python setup.py
```

Once the setup script has finished running, you should restart your terminal session and run the following command:

```
PlasticNet
```

This will open the PlasticNet terminal, so you can easily download our models from our model zoo, test the models on videos, webcam, and images, or train on top of an existing model.

A list of all commands can be found by typing `help`, and more detailed instructions about aguments for any command can be found with `help [command name]`.

To exit the command line, type `quit`. 

## Using YOLO Models

If you intend to train YOLO Models, you, may have to make some changes to the Makefile depending on your system. The Makefile is located in ./darknet, and you will want to update these parameters to whatver your system has, 1 meaning enabled.

```
GPU=1
CUDNN=0
CUDNN_HALF=0
OPENCV=1
AVX=0
OPENMP=0
LIBSO=0
```
It is highly recommended you install CUDNN & OpenCV for use with Darknet, as it will expedite the training process. 

You can additionally update the `yolo-obj.cfg` file (located in /darknet/cfg/) with any parameters you choose, specifically the number of iterations, classes, and filters. A guide for what these values should be set to can be found here: [https://github.com/mattokc35/darknet#how-to-train-to-detect-your-custom-objects](https://github.com/mattokc35/darknet#how-to-train-to-detect-your-custom-objects)

After you have updated this makefile and/or the configuration file, run `make clean` and `make` to be able to start darknet training with the PlasticNet CLI.


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



## Ocean Plastic Statistics

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
