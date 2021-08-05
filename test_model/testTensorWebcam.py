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


"""
Object Detection (On Webcam) From PlasticNet Tensorflow Saved Model
=====================================
"""

import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tensorflow as tf
import pathlib
import cv2
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
from IPython.display import display
from object_detection.utils import ops as utils_ops, label_map_util, visualization_utils as vis_util
from absl import app, flags

# Flag provides name of trained model we want to test
flags.DEFINE_string('trained_model', None, 'Trained Model')
# Flag provides the minimum confidence threshold
flags.DEFINE_string('score', None, 'Score')

FLAGS = flags.FLAGS

def load_model(PATH_TO_MODEL_DIR):
  """
  Function will load model that is saved in the PATH_TO_MODEL_DIR
  """
  model_dir = pathlib.Path(PATH_TO_MODEL_DIR)
  model = tf.saved_model.load(str(model_dir))
  return model

def run_inference_for_single_image(model, image):
  """
  Function tests model for single image, and draws boxes of detections on the frame
  """
  image = np.asarray(image)
  # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
  input_tensor = tf.convert_to_tensor(image)
  # The model expects a batch of images, so add an axis with `tf.newaxis`.
  input_tensor = input_tensor[tf.newaxis,...]

  # Run inference
  model_fn = model.signatures['serving_default']
  output_dict = model_fn(input_tensor)

  # All outputs are batches tensors.
  # Convert to numpy arrays, and take index [0] to remove the batch dimension.
  # We're only interested in the first num_detections.
  num_detections = int(output_dict.pop('num_detections'))
  output_dict = {key:value[0, :num_detections].numpy() 
                 for key,value in output_dict.items()}
  output_dict['num_detections'] = num_detections

  # detection_classes should be ints.
  output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
   
  # Handle models with masks:
  if 'detection_masks' in output_dict:
    # Reframe the the bbox mask to the image size.
    detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
              output_dict['detection_masks'], output_dict['detection_boxes'],
               image.shape[0], image.shape[1])      
    detection_masks_reframed = tf.cast(detection_masks_reframed > 0.5,
                                       tf.uint8)
    output_dict['detection_masks_reframed'] = detection_masks_reframed.numpy()
    
  return output_dict

def show_inference(model, image_np, score, category_index):
    """
    Function outputs the visualized results of a detection on a frame.
    """
    # Run single detection
    output_dict = run_inference_for_single_image(model, image_np)
    # Visualization of the results of a detection.
    final_img=vis_util.visualize_boxes_and_labels_on_image_array(
       image_np,
       output_dict['detection_boxes'],
       output_dict['detection_classes'],
       output_dict['detection_scores'],
       category_index,
       instance_masks=output_dict.get('detection_masks_reframed', None),
       use_normalized_coordinates=True,
       min_score_thresh=float(score), #minimum confidence threshold
       line_thickness=8)
    return(final_img)




def main(argv):

  # provide path to model directory
  trained_model = FLAGS.trained_model

  # Provide minimum confidence threshold
  score = FLAGS.score
  PATH_TO_MODEL_DIR = '../out/' + str(trained_model) + '/exported_model/saved_model'

  #Provide the path to the label map file (label_map.pbtxt), change if you want your own label map
  PATH_TO_LABELS = '../out/label_map.pbtxt'
  # List of the strings that is used to add correct label for each box.
  category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)


  # Enable GPU dynamic memory allocation
  gpus = tf.config.experimental.list_physical_devices('GPU')
  for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)

  # Load model
  detection_model = load_model(PATH_TO_MODEL_DIR)
  detection_model.signatures['serving_default'].output_dtypes
  detection_model.signatures['serving_default'].output_shapes
  
  #  Start video capture on the webcam
  cap = cv2.VideoCapture(0)

  # Set size for video capture 
  frame_width = int(cap.get(3))
  frame_height = int(cap.get(4))
    
  size = (frame_width, frame_height)

  # save webcam result as mp4 video file
  result = cv2.VideoWriter('detections/webcam_result.mp4', cv2.VideoWriter_fourcc(*'MP4V'),20.0, size)

  while 1:
      # Keep looping until user hits 'q'. Will loop through frames of live video in webcam and run detection tests on each frame.
      _,img = cap.read()
      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      final_img = show_inference(detection_model, img, score, category_index)

      final_img = cv2.cvtColor(final_img, cv2.COLOR_RGB2BGR)
      cv2.imshow('img', final_img)
      result.write(final_img)

      
      #break loop on q key
      if cv2.waitKey(1) == ord('q'):
          break
  cap.release()
  cv2.destroyAllWindows()


if __name__ == '__main__':
  app.run(main)
