# Copyright (c) 2017 Jared Crapo, K0TFU

import unittest
import yaml

from netcontrol.net import Net
from netcontrol.session import Session
from netcontrol.operator import Operator

class SessionTest(unittest.TestCase):
    def test_session_operators(self):
        
        # setup a net with one known operator
        net = Net()
        net.description = "DHRA Weekly Net"
        op1 = Operator('K0TFU')
        net.add_operator(op1)
        
        session = Session(net)
        self.assertEqual(0, len(session.operators))

        # don't add empty operators
        op = Operator()
        session.checkin(op)
        self.assertEqual(0, len(session.operators))

        # add operators with at least a call sign
        session.checkin(op1)
        self.assertEqual(1, len(session.operators))
        
        # op1 was already known to the net, so net operators
        # shouldn't have changed
        self.assertEqual(1, len(net.operators))
        
        # op2 is new to the net, so both session and net should now
        # have 2 operators
        op2 = Operator(callsign='N7RSC')
        session.checkin(op2)
        self.assertEqual(2, len(session.operators))
        self.assertEqual(2, len(net.operators))
        
        # make sure 
        # don't add duplicate operators
        session.checkin(op1)
        self.assertEqual(2, len(session.operators))
        self.assertEqual(2, len(net.operators))
        