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

#!/usr/bin/python3

from cmd import Cmd
import sys
import os
import subprocess
global currentModel
global currentPath
class MyPrompt(Cmd):    
    
    print(os.popen("mdfind kind:folder “PlasticNet”").read())
    def __init__(self):
        """
        Constructor Function
        """
        super(MyPrompt, self).__init__()
        self.currentModel = "default"

        # Looks for PlasticNet folder and will open it
        proc = subprocess.Popen(["mdfind kind:folder 'PlasticNet'",  "kind:folder 'PlasticNet'"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        final_out = str(out).split("\\")
        self.currentPath = final_out[0][2:]


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
        args = args.split()
        model = ""
        num_classes = -1
        if (len(args) == 2):
            model = args[0]
            num_classes = args[1]
            print("PREPARING TRAINING FOR MODEL: " + str(model))
        elif (len(args) == 1):
            model = ""
            num_classes = 7 # default
            print("PREPARING TRAINING FOR MODEL: " + str(self.currentModel))
        else:
            print("ERROR: Invalid syntax. Use help prepare_training for help.")
            return
        return_code = os.system("python " + str(self.currentPath) + "/" + "prepare_training.py --model_name " + str(model) + " --num_classes " + str(num_classes))
        if return_code == 0: # successful
            self.currentModel = args[0]
            print(self.currentModel)
        else:
            print("ERROR: Prepare training has failed. Check the name of the model you've specified.")
    def help_prepare_training(self):
        """
        Help Function
        """
        print("syntax: prepare_training [model_name] [OPTIONAL: num_classes]")
        print("generates all the necessary files for training to begin. After this is complete, run train_model")


    def do_train_model(self, args):
        """
        Trains model using pre-trained base model specified by user
        """
        print("TRAINING MODEL: " + str(self.currentModel))
        os.system("python " + self.currentPath + "/" + "train_model.py --pipeline_config_path=training/pipeline.config/ " +
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
        args = args.split()
        if (len(args) >= 1):
            mode = args[0]
            if(mode == 'w'):
                score = args[1]
                print('Testing on WEBCAM: ' + str(self.currentModel))
                current_path = self.currentPath
                os.chdir(current_path + '/test_model')
                current_path = os.getcwd()
                os.system("python " + self.currentPath + "/test_model/" + "testTensorWebcam.py --trained_model " + str(self.currentModel) + " --score " + str(score))
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
                    os.system("python " + self.currentPath + "/test_model/" + "testTensorVideo.py --video_name " + str(videoName) + " --trained_model " + str(self.currentModel) + " --score " + str(score))
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
                os.system("python " + self.currentPath + "/test_model/" + "testTensorflow.py --trained_model" + str(self.currentModel) + " --score " + str(score))
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
        current_path = os.getcwd()
        os.chdir(current_path + '/prepare_records/')
        # Partition the dataset
        os.system("python  " + self.currentPath  + "/prepare_records/partition_dataset.py")
        # Create test_labels.csv and train_labels.csv
        os.system("python  " + self.currentPath  + "/prepare_records/xml_to_csv.py")
        #generate for train data
        os.system("python " + self.currentPath + "/prepare_records/" + "generate_tfrecord.py --csv_input=images/train_labels.csv  --output_path=train.record --image_dir=images/train")
        #generate for test data
        os.system("python " + self.currentPath + "/prepare_records/" +  "generate_tfrecord.py --csv_input=images/test_labels.csv  --output_path=test.record --image_dir=images/test")
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
