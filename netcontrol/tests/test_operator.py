# Copyright (c) 2017 Jared Crapo, K0TFU

import unittest
import yaml

from netcontrol.operator import Operator

class OperatorTest(unittest.TestCase):
    def test_operator_init(self):
        op = Operator('N7RSC')
        self.assertEqual('N7RSC', op.callsign)

        op = Operator(callsign='K0TFU')
        self.assertEqual('K0TFU', op.callsign)
    
    def test_operator_dump(self):
        op = Operator(callsign='K0TFU')
        op.firstname = 'Jared'
        op.lastname = 'Crapo'
        
        txt = yaml.dump(op)
        
        newop = yaml.safe_load(txt)
        self.assertEqual(op.callsign, newop.callsign)
        self.assertEqual(op.firstname, newop.firstname)
        self.assertEqual(op.lastname, newop.lastname)
