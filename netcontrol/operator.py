# Copyright (c) 2017 Jared Crapo, K0TFU

import yaml

class Operator(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = '!Operator'
    
    def __init__(self,callsign):
        self.callsign = callsign
