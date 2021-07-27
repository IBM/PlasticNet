import os
import tarfile

import six.moves.urllib as urllib

def download_checkpoint(model):
  # for tensorflow 2 model zoo
  download_base = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/'
  # Download the checkpoint
  opener = urllib.request.URLopener()
  opener.retrieve(download_base + model + '.tar.gz', model)

  tar = tarfile.open(model)
  tar.extractall('./checkpoint') # pipeline.config file will be included
  tar.close()

  os.remove(model)


"""
  # Extract all the `model.ckpt` files.
  with tarfile.open(model) as tar:
    for member in tar.getmembers():
      member.name = os.path.basename(member.name)
      if 'model.ckpt' in member.name:
        tar.extract(member, path=output)
"""

"""
def download_config(model_config, output):
  download_base = 'https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/configs/tf2/'

  # Download the config
  opener = urllib.request.URLopener()
  opener.retrieve(download_base + model_config, model_config)

"""
