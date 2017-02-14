# Copyright (c) 2017 Jared Crapo, K0TFU

import unittest
import yaml

from netcontrol.net import Net
from netcontrol.operator import Operator

class NetTest(unittest.TestCase):
    def test_net_operators(self):
        net = Net()
        self.assertEqual(0, len(net.operators))

        # don't add empty operators
        op = Operator()
        net.add_operator(op)
        self.assertEqual(0, len(net.operators))

        # add operators with at least a call sign
        op1 = Operator('K0TFU')
        net.add_operator(op1)
        self.assertEqual(1, len(net.operators))

        op2 = Operator(callsign='N7RSC')
        net.add_operator(op2)
        self.assertEqual(2, len(net.operators))
        
        # don't add duplicate operators
        net.add_operator(op1)
        self.assertEqual(2, len(net.operators))
        
    def test_net_dump(self):
        net = Net()
        op1 = Operator(callsign='K0TFU')
        net.add_operator(op1)
        op2 = Operator()
        op2.callsign = 'N7RSC'
        net.add_operator(op2)
        txt = yaml.dump(net)
        
        newnet = yaml.safe_load(txt)
        self.assertEqual(2, len(net.operators))
        self.assertEqual('N7RSC', net.operators['N7RSC'].callsign)
        
        