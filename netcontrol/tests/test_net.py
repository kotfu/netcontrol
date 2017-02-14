# Copyright (c) 2017 Jared Crapo, K0TFU

import unittest

from netcontrol.net import Net
from netcontrol.operator import Operator

class NetTest(unittest.TestCase):
    def test_net_roster(self):
        net = Net()

        # don't add empty operators
        op = Operator('')
        net.add_operator(op)
        self.assertEqual(0, len(net.roster))

        # add operators with at least a call sign
        op1 = Operator('K0TFU')
        net.add_operator(op1)
        self.assertEqual(1, len(net.roster))

        op2 = Operator('N7RSC')
        net.add_operator(op2)
        self.assertEqual(2, len(net.roster))
        
        # don't add duplicate operators
        net.add_operator(op1)
        self.assertEqual(2, len(net.roster))
        