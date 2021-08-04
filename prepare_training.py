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

import os
import json

from download_training import download_checkpoint
from override_pipeline import override_pipeline
from absl import app, flags
import subprocess

flags.DEFINE_string('arch_type', None, 'Darknet YOLO (y) or Tensorflow (t)')
flags.DEFINE_string('yolo_weights', None, 'name of weights file')
flags.DEFINE_string('model_name', None, 'Title of model')
flags.DEFINE_string('model_config_name', None, 'Model config name')
flags.DEFINE_integer('num_classes', None, "Number of classes")

FLAGS = flags.FLAGS

def main(argv):
  """
  Downloads and overrides the pipeline.config file distributed with any base PlasticNet models.
  Any image augmentation parameters will have to be changed manually within training/pipeline.config
  """
  #select YOLOv4 or tensorflow
  archType = FLAGS.arch_type
  yoloWeights = FLAGS.yolo_weights
  if archType == 't':

    MODEL_CHECKPOINT = FLAGS.model_name
    NUM_CLASSES = FLAGS.num_classes
    DIR_PATH = os.path.abspath(os.getcwd())
    train_record_path = DIR_PATH + '/prepare_records/train.record'
    val_record_path = DIR_PATH + '/prepare_records/test.record'
    checkpoint_path = DIR_PATH + '/checkpoint/' +  MODEL_CHECKPOINT + '/checkpoint/ckpt-0'
    label_map_path = DIR_PATH + '/prepare_records/label_map.pbtxt'
    checkpoint_type = "detection"

    override_dict = {
      'train_input_path': train_record_path,
      'eval_input_path': val_record_path,
      'train_config.fine_tune_checkpoint': checkpoint_path,
      'label_map_path': label_map_path,
      'train_config.fine_tune_checkpoint_type': checkpoint_type
     }
    download_checkpoint(MODEL_CHECKPOINT)
    override_pipeline("./out/" + MODEL_CHECKPOINT + "/exported_model/" + "pipeline.config", override_dict, NUM_CLASSES) 
  elif archType == 'y':
    print('yolo')
    download_checkpoint(yoloWeights)
if __name__ == '__main__':
  app.run(main)
