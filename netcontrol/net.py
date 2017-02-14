# Copyright (c) 2017 Jared Crapo, K0TFU

class Net:
    def __init__(self):
        self.roster = {}

    def add_operator(self,operator):
        # make sure the operator's call sign isn't already in
        # the roster, and then add it
        if not operator.callsign:
            return
        
        self.roster[operator.callsign] = operator
