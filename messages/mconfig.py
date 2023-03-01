import yaml
import os

from easydict import EasyDict

config_yaml_path = os.path.join(os.path.dirname(__file__), 'mconfig.yaml')
with open(config_yaml_path, 'r') as f:
    configs_dict = yaml.load(f, Loader=yaml.FullLoader)
mconfigs = EasyDict(configs_dict)
