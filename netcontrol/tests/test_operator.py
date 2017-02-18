# Copyright (c) 2017 Jared Crapo, K0TFU

import unittest

from netcontrol.operator import Operator

class OperatorTest(unittest.TestCase):
    def test_operator_init(self):
        op = Operator('N7RSC')
        self.assertEqual('N7RSC', op.callsign)

        op = Operator(callsign='K0TFU')
        self.assertEqual('K0TFU', op.callsign)

