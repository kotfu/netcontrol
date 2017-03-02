# Copyright (c) 2017 Jared Crapo, K0TFU

"""
netsetup.py

UI class for the net setup widget
"""

from PyQt5 import QtWidgets
from PyQt5 import QtCore

class NetSetup(QtWidgets.QFrame):

    def __init__(self,net):
        super().__init__()
        self.net = net
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet('background-color: #aac')
        self.name_edit = QtWidgets.QLineEdit()
        self.freq_edit = QtWidgets.QLineEdit()
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.name_edit,0,0)
        grid.addWidget(self.freq_edit,0,1)
        self.setLayout(grid)
