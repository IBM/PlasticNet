#!/usr/bin/python3
# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cmd import Cmd
import sys
import os
import subprocess
global currentModel
global currentPath
class MyPrompt(Cmd):    
    
    
    def __init__(self):
        """
        Constructor Function
        """
        super(MyPrompt, self).__init__()
        self.currentModel = "default"

        # If CLI is installed, gets the path to the CLI. Otherwise, runs the path of this direct file as it was invoked directly
        if (os.environ.get("PLASTICNET_PATH") != None):
            self.currentPath = os.environ.get('PLASTICNET_PATH')
        else: 
            self.currentPath = os.path.dirname(os.path.abspath(__file__))

    def do_darknet_train(self, args):
        """
        Trains a model using a pretrained YOLOv4 Model
            Parameters:
                model_name: Name of the model that was downloaded
            Return:
                None
        """
        if (len(args) >= 1):
            self.currentModel = args[0]
        print("TRAINING YOLOV4 MODEL: " + str(self.currentModel))
        os.chdir("darknet")
        os.system('./darknet detector train data/obj.data cfg/yolo-obj.cfg ' + str(self.currentModel))
        os.chdir("../")
    def help_darknet_train(self):
        """
        Help Function
        """
        print("syntax: darknet_train [model_name]")
        print("trains model using pre-trained base model specified by user")
    def do_darknet_test(self, args):
        """
        Tests a model using a pretrained YOLOv4 Model on either webcam, video, or images
            Parameters:
                video_name, score (minimum confidence threshold)
        """
        os.chdir("darknet")
        args = args.split()
        if (len(args) >= 2):
            mode = args[0]
            if(mode == 'w'):
                score = args[1]
                print("Testing YOLOv4 Darknet on webcam...")
                os.system("./darknet detector demo data/obj.data cfg/yolo-obj.cfg " + ' -thresh ' + str(score) + " -c 0"  )
                #webcam
            if(mode == 'v'):
                if (len(args == 3)):
                    video_name = args[1]
                    score = args[2]
                else:
                    print("ERROR: Invalid syntax. Use help darknet_test for help.")
                    os.chdir("../")
                    return 
                print("Testing YOLOv4 Darknet on video...")
                os.system('./darknet detector demo data/obj.data cfg/yolo-obj.cfg ' + str(self.currentModel) +  ' ./data/' + str(video_name) + ' -thresh ' + str(score))
                #video
            if(mode == 'i'):
                score = args[1]
                print("Testing YOLOv4 Darknet on images...")
                os.system('./darknet detector test data/obj.data cfg/yolo-obj.cfg ' + str(self.currentModel) + ' -thresh ' + str(score))
        else:
            print("ERROR: Invalid syntax. Use help darknet_test for help.")
            os.chdir("../")
            return
        os.chdir("../")
        
    def help_darknet_test(self):
        """
        Help Function
        """
        print("syntax: darknet_test [mode (w|v|i)] [video_name (only if \'v\' mode)] [score]")
        print("tests YOLOv4 Darknet model on either webcam, video, or images with a specified minimum confidence threshold (score)")


    def do_set_model(self, args):
        """
        Function sets current model global variable that can be used for preparing, training, exporting, and testing.
        """
        print("SETTING MODEL")
        args = args.split()
        if (len(args) == 1):
            self.currentModel = args[0]
        else:
            print("ERROR: Invalid syntax. Use help set_model for help.")
            return
        print('current model set to: ' + str(self.currentModel))
    def help_set_model(self):
        """
        Help Function
        """
        print('--sets current model global variable that can be used for preparing, training, exporting, and testing')
        print('syntax: set_model [model name]')


    def do_prepare_training(self, args):
        """
        Function generates all the necessary files for training to begin. After this is complete, run train_model.
        """
        os.chdir(self.currentPath)
        args = args.split()
        model = ""
        num_classes = -1
        if (len(args) == 3):
            #yolo or tf
            mode = args[0]
            model = args[1]
            num_classes = args[2]
            print("PREPARING TRAINING FOR MODEL: " + str(model))
        elif (len(args) == 2):
            mode = args[0]
            model = args[1]
            print("PREPARING TRAINING FOR MODEL: " + str(model))
        else:
            print("ERROR: Invalid syntax. Use help prepare_training for help.")
            return
        if mode == 't':
            return_code = os.system("python prepare_training.py --arch_type " + str(mode) + " --model_name " + str(model) + " --num_classes " + str(num_classes))
        elif mode == 'y':
            print(self.currentPath)
            return_code = os.system("python prepare_training.py --arch_type " + str(mode) + " --yolo_weights " + str(model) + " --num_classes " + str(num_classes))
            weightsString = model.replace('weights', '.weights')
            os.system("cp out/" + str(weightsString) + " " + str(self.currentPath) + "/darknet")
            os.system("rm out/" + str(weightsString))
        if return_code == 0: # successful
            self.currentModel = args[1]
            print(self.currentModel)
        else:
            print("ERROR: Prepare training has failed. Check the name of the model you've specified.")
    def help_prepare_training(self):
        """
        Help Function
        """
        print("syntax: prepare_training [model_type (YOLOv4 (y) or Tensorflow (t))] [model_name (tf) or yolo_weights (y)] [OPTIONAL: num_classes]\n")
        print("generates all the necessary files for training to begin (for Tensorflow). For YOLOv4, downloads the specified pre-trained weights from PlasticNet Model Zoo. After this is complete, run train_model\n")
        print("\n")
        print("List of available models:\n")
        print("TensorFlow:")
        print("faster_rcnn_640x640_9classes_v1\nfaster_rcnn_640x640_7classes_v2\nfaster_rcnn_640x640_7classes_v1\nssd_resnet_640x640_7classes_v1")
        print("YOLO:")
        print("yolo9classv2iter27000weights\nyolo9class480x480weights\nyolo7class576x576weights\n7classyoloV2weights\nyolo4classesimgaugweights"+
        "\nyolo4classesupdatedweights\n4class8000iteration\nyolo2classes-imguag\nyolo2classes3000iterations\nyolov4weights")


    def do_train_model(self, args):
        """
        Trains model using pre-trained base model specified by user
        """
        os.chdir(self.currentPath)
        print("TRAINING MODEL: " + str(self.currentModel))
        os.system("python train_model.py --pipeline_config_path=training/pipeline.config/ " +
        "--model_dir=out/" + str(self.currentModel))
    def help_train_model(self):
        """
        Help Function
        """
        print ("syntax: train_model (no arguments needed, will use global variable \'current_model\'")
        print ("trains model using pre-trained base model specified by user")


    def do_export_model(self, args):
        """
        Function exports a model after training. Specify the same model name as you used for training
        """
        os.chdir(self.currentPath)
        args = args.split()
        if (len(args) == 1):
            model = args[0]
        else:
            print("ERROR: Invalid syntax. Use help export_model for help.")
            return
        print("EXPORTING MODEL: " + str(model))
        os.chdir(self.currentPath)
        os.chdir('models/research/object_detection')
        os.system("python exporter_main_v2.py --input_type image_tensor --pipeline_config_path" + 
        " ../../../training/pipeline.config --trained_checkpoint_dir ../../../out/" + str(model) + " " +
        "--output_directory ../../../out/" + str(model) + "/exported_model")
        os.chdir('../../../')
    def help_export_model(self):
        """
        Help Function
        """
        print("syntax: export_model [model_name]")
        print("Exports a model after training. Specify the same model name as you used for training")
    def do_test_model(self, args):
        """
        Function tests model on either webcam (w), video (v), or a directory of images (i).
        """
        os.chdir(self.currentPath)
        args = args.split()
        if (len(args) >= 1):
            mode = args[0]
            if(mode == 'w'):
                score = args[1]
                print('Testing on WEBCAM: ' + str(self.currentModel))
                current_path = self.currentPath
                os.chdir(current_path + '/test_model')
                current_path = os.getcwd()
                os.system("python " + "/test_model/" + "testTensorWebcam.py --trained_model " + str(self.currentModel) + " --score " + str(score))
                os.chdir('../')
                current_path = os.getcwd()
                print(current_path)
            elif(mode == 'v'):
                if (len(args) == 3):
                    videoName = args[1]
                    score = args[2]
                    print('Testing on VIDEO: ' + str(self.currentModel))
                    current_path = self.currentPath
                    os.chdir(current_path + '/test_model')
                    current_path = os.getcwd()
                    os.system("python " +  "/test_model/" + "testTensorVideo.py --video_name " + str(videoName) + " --trained_model " + str(self.currentModel) + " --score " + str(score))
                    os.chdir('../')
                    current_path = os.getcwd()
                    print(current_path)
                else:
                    print("ERROR: Invalid syntax. Use help test_model for help.")
                    return
            elif(mode == 'i'):
                score = args[1]
                print('Testing on IMAGES: ' + str(self.currentModel))
                current_path = self.currentPath
                os.chdir(current_path + '/test_model')
                current_path = os.getcwd()
                os.system("python " + "/test_model/" + "testTensorflow.py --trained_model" + str(self.currentModel) + " --score " + str(score))
                os.chdir('../')
                current_path = os.getcwd()
                print(current_path)
            else:
                print("ERROR: Invalid mode. Use help test_model for help.")
        else:
            print("ERROR: Invalid syntax. Use help test_model for help.")
            return
    def help_test_model(self):
        """
        Help Function
        """
        print ("syntax: test_model [w (webcam) | v (video) | i (image directory)] [video name (only if you select to test on video] [score (minimum confidence threshold value)]")
        print ("tests model on either webcam (w), video (v), or a directory of images (i)")


    def do_generatetfrecord(self, args):
        """
        Function generates both train.record and test.record for your tensorflow model, make sure your train_labels.csv is saved in images, and your images directories for train and test are saved as \'train\' and \'test\' in the images directory.
        """
        current_path = str(self.currentPath)
        os.chdir(current_path + '/prepare_records/')
        # Partition the dataset
        os.system("python partition_dataset.py")
        # Create test_labels.csv and train_labels.csv
        os.system("python xml_to_csv.py")
        #generate for train data
        os.system("python generate_tfrecord.py --csv_input=images/train_labels.csv  --output_path=train.record --image_dir=images/train")
        #generate for test data
        os.system("python generate_tfrecord.py --csv_input=images/test_labels.csv  --output_path=test.record --image_dir=images/test")
        #subprocess.call(['python generate_tfrecord.py', csvPath, outputPath, imagePath])
        os.chdir('../') 
    def help_generatetfrecord(self):
        """
        Help Function
        """
        print("syntax: generatetfrecord")
        print("--generates both train.record and test.record for your tensorflow model," + "Make sure all images are stored in prepare_records/images")


    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = MyPrompt() 
    prompt.prompt = '***PLASTIC-NET-IBM***  '
    prompt.cmdloop('WELCOME TO PLASTIC-NET! (developed by IBM Space Tech, 2021) \n Type \'help\' to see a list of documented commands!')
