# Copyright (c) 2017 Jared Crapo, K0TFU

# serialization options http://stackoverflow.com/questions/2627555/how-to-deserialize-an-object-with-pyyaml-using-safe-load

import persistent

class Operator(persistent.Persistent):

    """Model class for a ham radio operator
    
    Attributes
    ----------
    callsign: str
        The operators FCC issued call sign
    firstname: str
        The operator's given name(s)
    lastname: str
        The operator's surname or family name
    """

    def __init__(self, callsign=None, firstname=None):
        self.callsign = callsign
        self.firstname = None
        self.lastname = None

