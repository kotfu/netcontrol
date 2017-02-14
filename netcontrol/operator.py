# Copyright (c) 2017 Jared Crapo, K0TFU

# serialization options http://stackoverflow.com/questions/2627555/how-to-deserialize-an-object-with-pyyaml-using-safe-load

import yaml

class Operator(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = '!Operator'
    
    def __init__(self,callsign=None):
        self.callsign = callsign
