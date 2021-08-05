**NOTE:** Before installing anything with PlasticNet, you will need to have installed Protobufs: you can do so here: https://github.com/protocolbuffers/protobuf/releases

Download the correct version for your Operating System, then extract the zip. Add this directory to your system path so that the protoc command is recognized. 

If you wish to forego using the CLI and only use the python scripts, this wiki page entails how each script would be run and the parameters you can configure. 

To get a model to run from start to finish, you will have to do the following steps:
* Download a Pretrained Model & Configure its Pipeline File
* Partition your Data into Test & Train sets 
* Generate a CSV from your Test & Train XML Sets (TensorFlow)
* Generate TF Record Files from your CSV Files (TensorFlow)
* Begin Training
* Export the Model when Training is Complete
* Test the Model with Images, Video, or Webcam to validate your model

## Initial Setup

To install all the dependencies for the project, it is recommended you run the setup script in the conda environment of your choice.

First, create a conda environment, then use ```conda activate (env-name)``` and ```python setup.py``` in the `PlasticNet` directory.

This will install all the dependencies you need, install the tensorflow and darknet repositories, and set up TensorFlow. This will also install the CLI to your machine. If you wish to avoid this, you can set up everything manually:

First, you will want to install all of the requirements for darknet and tensorflow. You can do this by running the following command:

```pip install -r requirements.txt```

This will take some time on the first installation. 

Next, you will want to clone the darknet repository and the TensorFlow model garden into your PlasticNet directory. Run the following commands:

To install Darknet:

```git clone https://github.com/mattokc35/darknet.git```

To install TensorFlow:

```git clone https://github.com/tensorflow/models.git```

Once the TensorFlow repository is cloned, you will have to do some additional steps to install it. 
Navigate into the `research` directory within Tensorflow:
```cd models/research```

Next, convert TensorFlow's protobuf files to python files:

```
protoc -I=./ --python_out=./ ./object_detection/protos/*.proto
```

Export your python PATH. On Mac/Linux, run the following:

```bash
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/sli
```

In this second command, you will want to ```cd ..``` and ```pwd``` to get the path to the models directory. You can copy paste it in the second command, replacing `/path/to/models` with your path to the models directory.
 
```bash
export PYTHONPATH=$PYTHONPATH:/path/to/models
```


If all is done correctly, this should complete the installation of tensorflow and the necessary dependencies. 

## Partitioning the Dataset

#### TensorFlow
To partition the dataset in TensorFlow, you will first want to add all of your images into `prepare_records/images/`

Navigate back to the `prepare_records` directory and run the following script to partition your dataset into 80% train and 20% test.

```python partition_dataset.py```

Once this script has finished running, all of your files should be moved into the `train` and `test` folders within `images`. You can now create a CSV file from these entries using the following command:

```python xml_to_csv.py```

If you have added or removed any classes, you will need to edit the function on line 41 that returns the label number from the name before you run the following scripts. 

Finally, you will need to create the tfrecord files:

```bash
python generate_tfrecord.py --csv_input=images/train_labels.csv  --output_path=train.record --image_dir images/train
```

```bash
python generate_tfrecord.py --csv_input=images/test_labels.csv  --output_path=test.record --image_dir images/test
```

This will generate the tfrecords and place them in the right places, so once your downloaded model is configured, you are able to begin training. 

#### YOLO
To partition your dataset with YOLO, you will want to place all of your images in `darknet/data/obj`. Then you can run the script ```python traintestsplit.py```. This will place your images into train and test folders within `data/obj`. 

## Downloading a Pretrained Model and Configuring its Pipeline File

First, select a pretrained model that you would like to use for transfer learning. You can select either a YOLO Model or a TensorFlow Model from [this list](https://github.ibm.com/spacetech-interns/PlasticNet/wiki/PlasticNet-Model-Zoo-Metrics). When this guide references model name, use the name listed on that page as the downloadable name. 

#### TensorFlow
If you are using TensorFlow, the easiest way to download and configure the files at the same time is through the `prepare_training.py` script. 

Run 
```
python prepare_training.py --arch_type t --model_name (model name)
```

This will download the model you've specified, and place the pipeline file in `training/pipeline.config`. 
Generally, for the tensorflow models, the only thing you would need to change in the Pipeline file is the number of classes and perhaps the image augmentation parameters. If you wish to perform transfer learning on top of one of our models, and you know how many classes are in your dataset, you can do ```python prepare_training.py --model_name (model name) --num_classes (number of classes)``` to overwrite the number of classes in the pipeline file so there is nothing for you to change. 

The only thing you will need to provide from here is a label_map.pbtxt. For ease of use with the project and any model variations you may be training, we recommend placing this in the `/out/` folder. An example label map is shown below, so you can see how to format yours:


```
item {
  name: "plastic-bag"
  id: 1
}
item {
  name: "plastic-bottle"
  id: 2
}
```
If you do not wish to train, you can skip to the testing section if you have downloaded a model. None of the rest of the steps are necessary to test. Our models are ready to test as packaged. 

#### YOLO

At the time of writing this guide, there is not a script that modifies YOLO Configuration for you. To download a yolo model, you can download the weights manually from the model zoo, by clicking on the model you want, or you can run the following command to download the weights to the out directory. 

```
python prepare_training.py --arch_type y --yolo_weights (name of yolo weights)
```

You will likely want to move this to the `/darknet/` folder - but you can also just specify the file path when you begin training or testing. 

Within darknet, there are quite a few parameters you will want to change within the config file.

Go into the `cfg/` directory and open `yolo-obj.cfg`. In this file, you can make changes based on the number of classes in your model. 

The following changes need to be made:
* change line `max_batches` to (classes*2000, but not less than number of training images and not less than 6000), e.g. max_batches=6000 if you train for 3 classes
* change line `steps` to 80% and 90% of max_batches, e.g. steps=4800,5400 if `max_batches` == 6000
* set network size `width=416` and `height=416` or any value multiple of 32
* In each [yolo] layer, change `classes=` to `classes=(your number of classes)`
* change `filters=` to `filters=(classes + 5)x3` in the 3 [convolutional] before each [yolo] layer, keep in mind that it only has to be the last [convolutional] before each of the [yolo] layers.

You will also need to edit the `obj.names` and the `obj.data` files which are included in the `/data` folder. 
The `obj.names` file should contain each class's name on a separate line, and the `obj.data` file will require you to update the number of classes and ensure that the paths to `train`, `test` (valid), `names`, are correct. 

## Beginning Training
It is recommended that all of training happens within a tmux window so you can leave the training happening even when the command line is closed. To get started, type `tmux`. This will bring you to a new window. To exit, you can do `CMD + B + D` and the session will continue to run. 

#### TensorFlow
Once you are happy with all of your configuration, you should be able to train your tensorflow model using the train_model.py script. 

```bash
python train_model.py --pipeline_config_path=../../../training/pipeline.config/ --model_dir=../../../out/(model_name)
```

This will run a lot of preprocessing, but once you see the losses showing up in the console. If the model is training properly, output should look something like this:
```
I0802 13:41:51.557678 140033896219008 model_lib_v2.py:701] {‘Loss/BoxClassifierLoss/classification_loss’: 0.154603,
 ‘Loss/BoxClassifierLoss/localization_loss’: 0.16872177,
 ‘Loss/RPNLoss/localization_loss’: 0.24726836,
 ‘Loss/RPNLoss/objectness_loss’: 0.05993971,
 ‘Loss/regularization_loss’: 0.0,
 ‘Loss/total_loss’: 0.63053286,
 ‘learning_rate’: 0.08}
```

To get the most out of tensorflow, it's highly recommended that you use TensorBoard to monitor the training process so you can decide when to stop the training. 

In either a new TMUX session or a new terminal, run the following commmand:
```bash
tensorboard --logdir=/path/to/model/dir/train --bind_all
```
Replace "/path/to/model/dir" with the directory within "out" that includes your model. Make sure to direct tensorboard to the `/train` directory within this directory.

Once this runs, you will be able to view graphs of your training metrics accessible at (YOUR IP):6006. Tensorboard will link you to this when the command runs.

#### YOLO

When you are satisfied with your configuration, you need to `make` the makefile. Before doing so, you may want to ensure that everything in the Makefile is what you want to use - if you have CUDA, OpenCV, and CuDNN installed, you may want to make sure these are set to 1 in the makefile so that training will run more efficiently. 

Within the darknet folder, run `make`. This will create a darknet executable that you can use for training. 

Once the make command finishes executing, you can start training with the following command:
```bash
./darknet detector train data/obj.data cfg/yolo-obj.cfg ../out/(MODEL NAME).weights
```

Unlike TensorFlow, yolo will complete its training according to the max number of iterations you have set in your configuration file. You can leave the session and just wait for training to terminate. 

## Export the Model when Training is Complete

#### TensorFlow

When your model has converged, you will want to stop training. Go into the terminal where your training is happening, and Command + C or Control + C. It will take a bit for TensorFlow to respond, but the training will stop. 

Once the training has stopped, you will want to run the following commands to export the model.

```bash
cd models/research/object detection
python exporter_main_v2.py --input_type image_tensor --pipeline_config_path ../../../training/pipeline.config —-trained_checkpoint_dir ../../../out/(MODEL NAME) --output_directory ../../../out/(MODEL NAME)/exported_model
```
When this command finishes executing, you will be able to use the testing scripts to validate the model.

#### YOLO

YOLO will save its weights automatically when the training completes. You do not have to run any commands to export it. 

## Testing the Model

#### TensorFlow

When testing a TensorFlow model, you can use the scripts that we have provided within the `test_model` folder. 

Navigate to this folder and then run the scripts you would like to run. If you would like to test on videos or images, you will need to add these into the respective images and videos folders. 

To test with a video, use the following command:
```bash
python testTensorVideo.py --trained_model (model name) --video_name (video name, including file extension) --score (threshold confidence needed for a bounding box to show)
```

To test with images, use the following command:
```bash
python testTensorflow.py --trained_model (model name) --score (threshold confidence needed for a bounding box to show)
```
This will run your model on all of the images in the images folder. 

To test on webcam, use the following command:
```bash
python testTensorWebcam.py --trained_model (model name) --score (threshold confidence needed for a bounding box to show)
```

#### YOLO
Within Darknet, there are ways to test on videos and images as well. Without a GPU, these will run extremely slowly, so we recommend the alternative method. However, these are already included in your installation.

The following command should run your model on a video:
```
./darknet detector demo data/obj.data cfg/yolo-obj.cfg (path to weights file) (path to video file) -thresh (score for bounding boxes)
```

The alternative method we used comes from the following repository:
https://github.com/theAIGuysCode/tensorflow-yolov4-tflite

This converts your YOLO model into a TensorFlow model that you can test with some scripts included in that repository. We didn't include it in the stock installation to save space, however you can easily clone this repository and test YOLO with the instructions included on that repository. 
