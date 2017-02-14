# Copyright (c) 2017 Jared Crapo, K0TFU

import yaml

class Net(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = '!Net'
    
    def __init__(self):
        self.operators = {}
        self.description = ''

    def add_operator(self,operator):
        # don't add operators without a callsign
        if operator.callsign:
            # use the callsign as the key = no duplicates
            self.operators[operator.callsign] = operator
