Welcome to the PlasticNet Wiki! 

See our public repository here: https://github.com/IBM/PlasticNet

**PlasticNet** is an "**IBM Tech for Good**" open-source project developed by the IBM Space Tech team to build a repository of AI object detection models to classify types/brands of plastics, trash on beaches, trash in the ocean, etc. We can scale this effort with the global community of developers participating and contributing towards this noble effort, with long term goals to help with ocean cleanup and positively impact climate change. 


## Goals

The Goals for our project are listed below as the following:

*   Real-time **detection of different types of trash** (plastic in particular) in the ocean utilizing transfer learning on different machine learning object detection architectures
*   In the future, we would also like to be able to improve our model to be able to **recognize logos/brands on trash**, in order to detect and identify which company different types of ocean/beach trash come from
*   To build a **fully functional PlasticNet machine learning pipeline** that can be easily used to train and test object detection models based from architectures such as YOLOv4, Faster-RCNN, SSD-Resnet, Efficient-DET, Tensorflow, etc. (all accessible inside a **command line client**)
*   To provide a set of **pretrained PlasticNet models** that can be utilized for future development and improvement via **transfer learning**
*   Implement our models to work on real-time satellite and camera footage

## Basic Project Structure and Technologies Used (feat. diagram)
![](https://github.ibm.com/spacetech-interns/PlasticNet/blob/master/img/plasticnetdiagram.png)

The PlasticNet command line program combines YOLOv4 and Tensorflow Object Detection API technologies into a single, easily usable machine learning pipeline CLI. Collaborators can use the PlasticNet CLI to prepare models  for training (via transfer learning from the provided pre-trained PlasticNet models), train custom detection models built upon pre-trained PlasticNet models, export the trained models, and finally test the trained models.  The CLI was created so these steps can all be done with a few simple commands, seen [here](https://github.ibm.com/spacetech-interns/PlasticNet/wiki/Utilizing-the-PlasticNet-Command-Line-Client). Initially trained via transfer learning from pre-trained YOLO weights [(found here)](https://github.com/mattokc35/darknet#pre-trained-models), and pre-trained Tensorflow models (from the [Tensorflow Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)), our official **PlasticNet Model Zoo** (found [here](https://github.com/IBM/PlasticNet/blob/main/ModelZoo.md)) can be used by collaborators for the further improvement/development of new PlasticNet object detection models. For labeling images, we utilized IBM's Cloud Annotations (instructions found [here](https://github.ibm.com/spacetech-interns/PlasticNet/wiki/Creating-Your-Own-Dataset-for-Custom-Training)).

