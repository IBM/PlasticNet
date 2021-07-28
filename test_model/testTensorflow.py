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
Object Detection (On Image) From PlasticNet Tensorflow Saved Model
=====================================
"""
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging (1)
import pathlib
import tensorflow as tf
import cv2
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from absl import app, flags
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time
import warnings
warnings.filterwarnings('ignore')   # Suppress Matplotlib warnings

# Flag provides name of trained model we want to test
flags.DEFINE_string('trained_model', None, 'Trained Model')
# Flag provides the minimum confidence threshold
flags.DEFINE_string('score', None, 'Score')

FLAGS = flags.FLAGS


def load_image_into_numpy_array(path):
    """Load an image from file into a numpy array.
    Puts image into numpy array to feed into tensorflow graph.
    Note that by convention we put it into a numpy array with shape
    (height, width, channels), where channels=3 for RGB.
    Args:
      path: the file path to the image
    Returns:
      uint8 numpy array with shape (img_height, img_width, 3)
    """
    return np.array(Image.open(path))

def main(argv):

  #from google.colab.patches import cv2_imshow
  # Enable GPU dynamic memory allocation
  gpus = tf.config.experimental.list_physical_devices('GPU')
  for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)

  # Path to image directory is inside PlasticNet/test_model/images (drop all your images here you want to test)
  LIST_IMAGE_PATHS = []
  for root, dirs, files in os.walk(os.path.abspath("images/")):
      for file in files:
          LIST_IMAGE_PATHS.append(os.path.join(root, file))

  # Provide path to model directory
  trained_model = FLAGS.trained_model
  # minimum confidence threshold
  score = FLAGS.score

  #Provide path to model directory
  PATH_TO_MODEL_DIR = '../out/' + str(trained_model) + '/exported_model/saved_model'

  #Provide the path to the label map file (label_map.pbtxt), change if you want your own label map
  PATH_TO_LABELS = '../saved_models/tensorflow_7_test/label_map.pbtxt'

  # LOAD THE MODEL
  from object_detection.utils import label_map_util
  from object_detection.utils import visualization_utils as viz_utils
  PATH_TO_SAVED_MODEL = PATH_TO_MODEL_DIR
  print('Loading model...', end='')
  start_time = time.time()

  # Load saved model and build detection function
  detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)
  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Done! Took {} seconds'.format(elapsed_time))
  
  # List of the strings that is used to add correct label for each box.
  category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
  
  
  # Run detection test on each image in the images folder, and draw boxes around each object detected.                                                                   
  print('Running inference for images')
  counter = 0
  for image_path in LIST_IMAGE_PATHS:
    print(image_path)
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_expanded = np.expand_dims(image_rgb, axis=0)
    # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
    input_tensor = tf.convert_to_tensor(image)
    # The model expects a batch of images, so add an axis with `tf.newaxis`.
    input_tensor = input_tensor[tf.newaxis, ...]
    # input_tensor = np.expand_dims(image_np, 0)
    detections = detect_fn(input_tensor)
    # All outputs are batches tensors.
    # Convert to numpy arrays, and take index [0] to remove the batch dimension.
    # We're only interested in the first num_detections.
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                  for key, value in detections.items()}
    detections['num_detections'] = num_detections
    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
    image_with_detections = image.copy()
    # SET MIN_SCORE_THRESH BASED ON YOU MINIMUM THRESHOLD FOR DETECTIONS
    viz_utils.visualize_boxes_and_labels_on_image_array(
          image_with_detections,
          detections['detection_boxes'],
          detections['detection_classes'],
          detections['detection_scores'],
          category_index,
          use_normalized_coordinates=True,
          max_boxes_to_draw=200,
          min_score_thresh=float(score),
          agnostic_mode=False)
  
    # DISPLAYS OUTPUT IMAGE
    plt.figure(figsize=(35,17))
    #figure(figsize=(8, 6), dpi = 100)
    plt.imshow(cv2.cvtColor(image_with_detections, cv2.COLOR_BGR2RGB))
    plt.savefig('detections/' + str(counter) + "_result.jpg")
    print(str(counter))
    print('Done')
    counter += 1

if __name__ == '__main__':
  app.run(main)
