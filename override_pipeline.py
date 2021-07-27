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