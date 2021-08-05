## PlasticNet Command Line Client Demo Video

## Instructions

The CLI is supported on any operating system that can run Python, but using the CLI from any location on your computer is only available after running the following command on MacOS.

```
python setup.py
``` 

If you are running Windows or Linux, to use the CLI, you will need to navigate into the PlasticNet repository you cloned, and then after running the setup command to install all dependencies, you will need to run the following command:

```
python PlasticNet.py
```

This will launch an instance of the command line interface. To view all the commands, use `help`. You can also provide the command name as an argument to `help` and it will provide the syntax for using the command. 

## Set Model

If you have closed the command line client in between uses, or are just wanting to test models, you will need to set the model beforehand. NOTE: You do not have to run this command before running prepare_training, but if you were to close the CLI between preparing training and running the train command, you would need to set the model again. 

USAGE:
```
set_model (name of the model)
```

## Partition Dataset

#### TensorFlow
To partition your dataset for a TensorFlow model, and to additionally create the TFRecord files, you will need to run the following command:

```
generatetfrecord
```

Provided that all of your images and XML files are in the same `/prepare_records/images` directory, this command will take care of everything for you.

#### YOLO
To partition your dataset for a YOLO model, you just need to make sure your data is stored in `darknet/data/obj`. Then when you run the `prepare_training` command, the data will be partitioned as a part of that command. This will generate a test.txt and a train.txt in `darknet/data`.


## Prepare Training
This function is used to download a model from our Model Zoo and configure its paths in the pipeline file for training (if using TensorFlow). 

USAGE:
```
prepare_training (t for TensorFlow, y for Yolo) (tensorflow or yolo model name) [OPTIONAL: number of classes. Default is 9]
```

NOTE: If you are unsure of what model to download, visit the [Model Zoo](https://github.ibm.com/spacetech-interns/PlasticNet/wiki/PlasticNet-Model-Zoo-Metrics) which has information about the pretrained models and their losses, as well as their names. You can also do `help prepare_training` to get a full list of the available models. 


## Train Model

#### TensorFlow

If you would like to train a TensorFlow model using the CLI, use the following command:
```
train_model
```

This will run the training script for a TensorFlow model. You will have to keep this window running unless you launch the CLI in a tmux session, which is recommended. 

#### YOLO

If you would like to train a YOLO model using the CLI, use the following command:
```
darknet_train (darknet weights file name)
```

## Export Model

Exporting the model is only necessary on TensorFlow. It will be done automatically when training completes with YOLO. To export a tensorflow model, you will first need to Control + C the window that's running the TensorFlow Training, then you will want to run this command.

```
export_model (model name)
```

## Test Model

#### TensorFlow

You can use the following command to test your current model on webcam, images, or a video. These need to be stored in the respective images or videos folder within `/test_model/`. 

Remember, before running this command you MUST use the `set_model` command described above to set the model. 

```
test_model [w for webcam, v for video, i for images)] [video name (only if you select to test on video] [score (minimum confidence threshold value)]
```

#### YOLO

You can use the following command to test your darknet model on webcam, images, or a video. These need to be stored within `darknet/data/`.

```
darknet_test [w for webcam, v for video, i for images)] [video name (only if you select to test on video] [score (minimum confidence threshold value)]
```



