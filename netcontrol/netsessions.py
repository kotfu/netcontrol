# Copyright (c) 2017 Jared Crapo, K0TFU

"""
netsessions.py

UI class for the sessions widget
"""

from PyQt5 import QtWidgets
from PyQt5 import QtCore

class NetSessions(QtWidgets.QFrame):

    def __init__(self,net):
        super().__init__()
        self.net = net
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet('background-color: #caa')
        grid = QtWidgets.QGridLayout()
        self.session_list = QtWidgets.QListWidget()
        grid.addWidget(self.session_list,1,0,1,2)
        new_button = QtWidgets.QPushButton('New')
        new_button.clicked.connect(self.new_session_clicked)
        grid.addWidget(new_button,2,1)
        self.setLayout(grid)

    @QtCore.pyqtSlot()
    def new_session_clicked(self):
        s = self.net.new_session()
        self.session_list.addItem('New session')

        