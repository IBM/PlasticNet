# PlasticNet: Saving the Ocean with Machine Learning (IBM Space Tech)

### Problem: 

On average, humans dump around 8 million metric tons (~17.6 billion pounds) of trash into the ocean each year. At this rate, total plastic in the ocean will outweigh all of the ocean's fish by 2050. Ocean and beach pollution is a real issue, with consequences extending far beyond the mere superficial effects of making our beaches and oceans look less "pretty", such as:


* Depletion of oxygen content in the water

* Effect of toxic wastes on marine animals 

* Failure in the reproductive system of marine animals

* Contamination of the food chains

* Effect on human health

* Disruption to the cycle of coral reefs

In particular, plastics are the most common element found in the ocean today, and is especially harmful to the environment since it does not break down easily and is often mistaken as food by marine animals. In an effort to join the fight against global ocean pollution, the IBM Space Tech team has begun work on an open-source machine learning neural-network object detection project, **PlasticNet**. 

Our project is based from YOLOv4 Darknet detection and Tensorflow Object Detection API models, and provides an environment where developers can easily prepare, train, and test detection models which will identify different types of plastic (and non-plastic) trash in the ocean/on the beach. 


The **Goals** for our project are listed below as the following: 

* Real-time detection of different types of trash (plastic in particular) in the ocean utilizing transfer learning on different machine learning object detection architectures
* In the future, we would also like to be able to improve our model to be able to recognize logos/brands on trash, in order to detect and identify which company different types of ocean/beach trash come from
* To build a fully functional **PlasticNet** machine learning pipeline that can be easily used to train and test object detection models based from architectures such as YOLOv4, Faster-RCNN, SSD-Resnet, Efficient-DET, Tensorflow, etc. (all accessible inside a command line client)
* To provide a set of pretrained **PlasticNet** models that can be utilized for future development and improvement via transfer learning
* Implement our models to work on real-time satellite and camera footage

### Approach:
// todo architecture diagram type thing

The main goal, and the starting point for this project, was to be able to detect some of the most common types of ocean trash from a camera feed.

To be able to perform transfer learning and adapt a well-trained model to recognize trash, we first had to gather a large dataset of images that we could use to train off of. At first, we scoured Google Images for viable images of trash that we could label and use as a part of the dataset. 

After we had a dataset of about 500 images, we began labeling the images in [IBM Cloud Annotations](https://cloud.annotations.ai/). At the start, the team labeled every piece of detectable trash within the images, and we ended up with an overdefined model of classes. We then duplicated our annotations project, and started building models from, at first, our two most populated classes, then four, then six, and so on. Starting this way allowed us to see what types of trash would be seen more often and are more important to prioritze the detection of. 

Using these datasets, we were able to apply transfer learning on various models from the [TensorFlow Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) and models based on [YOLOv4](https://github.com/AlexeyAB/darknet).  From this point, we began a cycle of changing model parameters, testing new models, and improving model performance. 

Improving model performance included recognizing what our model was failing to recognize, or in some cases, detecting incorrectly. For example, one of our first models would often detect a potato chip bag as a metal can - both of these often have colorful pictures on the outside, and

## Findings:

## Project Extensions:

Want to get involved or use PlasticNet for yourself? See our project here: https://github.com/IBM/PlasticNet

