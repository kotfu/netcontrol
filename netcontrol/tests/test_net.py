# Copyright (c) 2017 Jared Crapo, K0TFU

import unittest
import ZODB
import transaction

from netcontrol.net import Net
from netcontrol.operator import Operator

class NetTest(unittest.TestCase):
    def setUp(self):
        self.memory_db = ZODB.DB(None)
        self.connection = self.memory_db.open()
        self.dbroot = self.connection.root
        self.dbroot.net = Net()
        self.net = self.dbroot.net
        transaction.commit()
        
    def test_net_operators(self):
        # don't add empty operators
        op = Operator()
        self.net.add_operator(op)
        self.assertEqual(0, len(self.net.operators))

        # add operators with at least a call sign
        op1 = Operator('K0TFU')
        self.net.add_operator(op1)
        self.assertEqual(1, len(self.net.operators))

        op2 = Operator(callsign='N7RSC')
        self.net.add_operator(op2)
        self.assertEqual(2, len(self.net.operators))
        
        # don't add duplicate operators
        self.net.add_operator(op1)
        self.assertEqual(2, len(self.net.operators))
        
    def test_net_transaction_abort(self):
        self.assertEqual(0, len(self.net.operators))
        transaction.commit()
        
        op1 = Operator(callsign='K0TFU')
        self.net.add_operator(op1)
        op2 = Operator()
        op2.callsign = 'N7RSC'
        self.net.add_operator(op2)
        transaction.abort()
        
        self.assertEqual(0, len(self.net.operators))

    def test_net_transaction_commit(self):
        op1 = Operator(callsign='K0TFU')
        self.net.add_operator(op1)
        op2 = Operator()
        op2.callsign = 'N7RSC'
        self.net.add_operator(op2)
        transaction.commit()
        
        self.assertEqual(2, len(self.net.operators))
