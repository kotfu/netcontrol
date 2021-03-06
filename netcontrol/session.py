# Copyright (c) 2017 Jared Crapo, K0TFU

import datetime
import persistent
import persistent.mapping

from netcontrol.checkin import Checkin

class Session(persistent.Persistent):

    """Model class for a single session of a directed ham radio net
    
    Data elements for a specific instance of a directed net
    
    Attributes
    ----------
    net_control_station: Operator
        The net control for this session of the net
    frequency: str
        Frequency for this session of the net, i.e. "447.100- T100Hz"
    start: datetime
        date and time in UTC zone when the session began
    operators: dict
        The amateur operators who have checked in to this net
    events: list
        sequential list of events that occured in this net
    """
    
    def __init__(self,net):
        self.net = net
        self.net_control_station = None
        self.frequency = None
        self.start_datetime = None
        self.operators = persistent.mapping.PersistentMapping()
        self.events = persistent.list.PersistentList()

    def checkin(self,operator):
        # don't add operators without a callsign
        if operator.callsign:
            # use the callsign as the key = no duplicates
            self.operators[operator.callsign] = operator
            self.events.append(Checkin(operator))
            # add this operator to the net if they aren't there
            self.net.add_operator(operator)

    def start(self):
        self.start_datetime = datetime.datetime.now()