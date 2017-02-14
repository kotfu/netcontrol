# Copyright (c) 2017 Jared Crapo, K0TFU

import unittest
import yaml

from netcontrol.operator import Operator

class OperatorTest(unittest.TestCase):
    def test_operator_dump(self):
        op = Operator('K0TFU')
        txt = yaml.dump(op)
        
        newop = yaml.safe_load(txt)
        self.assertEqual(op.callsign,newop.callsign)
