# Copyright (c) 2017 Jared Crapo, K0TFU

import yaml

class Net(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = '!Net'
    
    def __init__(self):
        self.operators = {}
        self.description = ''

    def add_operator(self,operator):
        # make sure the operator's call sign isn't already in
        # the roster, and then add it
        if not operator.callsign:
            return
        
        self.operators[operator.callsign] = operator
