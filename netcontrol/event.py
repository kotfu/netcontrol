# Copyright (c) 2017 Jared Crapo, K0TFU

import datetime
import persistent

class Event(persistent.Persistent):

    """Base class for all net events to inherit from
    """

    def __init__(self):
        self.datetime = datetime.datetime.now()
        super().__init__()
