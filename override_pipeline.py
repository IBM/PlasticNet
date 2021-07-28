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

from google.protobuf import text_format

from object_detection.utils import config_util
from object_detection.protos import preprocessor_pb2

def override_pipeline(pipeline, override_dict, num_classes=0):
  configs = config_util.get_configs_from_pipeline_file(pipeline)

  meta_arch = configs["model"].WhichOneof("model")
  override_dict['model.{}.num_classes'.format(meta_arch)] = num_classes
  configs = config_util.merge_external_params_with_configs(configs, kwargs_dict=override_dict)
  pipeline_config = config_util.create_pipeline_proto_from_configs(configs)
  config_util.save_pipeline_config(pipeline_config, "./training") # replace with where pipeline file is to be stored
