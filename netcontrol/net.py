# Copyright (c) 2017 Jared Crapo, K0TFU

import persistent
import persistent.mapping

from netcontrol.session import Session

class Net(persistent.Persistent):

    """Persistable class for a ham radio net
    
    Capture the core data for a ham radio net. See Session for a
    specific instance of a net.
    
    Attributes
    ----------
    name: str
        Name of this net
    schedule: str
        When this net occurs, i.e. "Every Thursday at 8:30pm"
    frequency: str
        Frequency where the net occurs, i.e. "447.100- T100Hz"
    manager: Operator
        The Operator who is the manager of this net
    operators: dict
        The Operators who have been seen on this net
    sessions: list
        list of sessions when this net has occured

    """

    def __init__(self):
        self.name = None
        self.schedule = None
        self.frequency = None
        self.manager = None
        self.operators = persistent.mapping.PersistentMapping()
        self.sessions = persistent.list.PersistentList()

    def add_operator(self,operator):
        # don't add operators without a callsign
        if operator.callsign:
            # use the callsign as the key = no duplicates
            # self.operators[operator.callsign] = operator
            self.operators[operator.callsign] = operator

    def new_session(self):
        # create a new session
        s = Session(self)
        self.sessions.append(s)
        return s

