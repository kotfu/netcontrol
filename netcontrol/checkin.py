# Copyright (c) 2017 Jared Crapo, K0TFU

from netcontrol.event import Event

class Checkin(Event):

    """A checkin event
    """

    def __init__(self,operator):
        self.operator = operator
        super().__init__()
