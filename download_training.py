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
import tarfile
import sys

import six.moves.urllib as urllib

def download_checkpoint(model):
  # For PlasticNet Model Zoo
  download_base = 'https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/'
  # Download the checkpoint
  opener = urllib.request.URLopener()
  opener.retrieve(download_base + model + '.tar.gz', model)

  tar = tarfile.open(model)
  tar.extractall('./out') # pipeline.config file will be included
  tar.close()

  os.remove(model)

if __name__ == '__main__':
  print(sys.argv[1])
  download_checkpoint(sys.argv[1])