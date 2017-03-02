#!/usr/bin/env python3
# Copyright (c) 2017 Jared Crapo, K0TFU

"""
netcontrol.py

Tool for ham radio net controllers to run and log a net
"""

import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtCore

import transaction
import ZODB

from netcontrol.net import Net
from netcontrol.netsessions import NetSessions
from netcontrol.netsetup import NetSetup
from netcontrol import __version__

class NetControl(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initDB()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('This is Net Control v'+__version__)
        
        # session layout
        session_widget = NetSessions(self.net)
        
        # setup layout
        setup_widget = NetSetup(self.net)

        
        # build the stack
        self.stackl = QtWidgets.QStackedLayout()
        self.stackl.addWidget(session_widget)
        self.stackl.addWidget(setup_widget)
        stack = QtWidgets.QWidget()
        stack.setLayout(self.stackl)

        # build the sidebar
        sidebar = QtWidgets.QFrame()
        sidebar.setStyleSheet('background-color: #aca')
        grid = QtWidgets.QGridLayout()

        sessions_button = QtWidgets.QPushButton('Sessions')
        sessions_button.clicked.connect(self.switch_to_sessions)
        grid.addWidget(sessions_button,0,0)

        ops_button = QtWidgets.QPushButton('Operators')
        grid.addWidget(ops_button,1,0)
        
        setup_button = QtWidgets.QPushButton('Setup')
        setup_button.clicked.connect(self.switch_to_setup)
        grid.addWidget(setup_button,2,0)
        
        sidebar.setLayout(grid)
        
        # build the header bar
        header = QtWidgets.QFrame()
        grid = QtWidgets.QGridLayout()
        title = QtWidgets.QLabel()
        title.setText('This is Net Control v'+__version__)
        grid.addWidget(title,0,0)
        header.setLayout(grid)
        header.setStyleSheet('background-color: #999')
        
        # assemble the main components and put them in the container
        nc = NetContainer()
        grid = QtWidgets.QGridLayout()
        # start at row zero for one row and spread all the way to the right
        grid.addWidget(header,0,0,1,-1)
        # sidebar spans rows 1 all the way to the bottom, in column zero
        grid.addWidget(sidebar,1,0,-1,1)
        # stack takes up the rest
        grid.addWidget(stack,1,1,-1,-1)
        nc.setLayout(grid)
        self.setCentralWidget(nc)
        
        
        # menubar
        exitAction = QtWidgets.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        
        menubar = self.menuBar()
        # this turns off the mac native menubar and shows it like it would on win or *nix
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exitAction)
        
        self.show()
    
    def initDB(self):
        # TODO fix this to read from a real file
        # for now, just create a temporary in-memory database
        self.memory_db = ZODB.DB(None)
        self.connection = self.memory_db.open()
        self.dbroot = self.connection.root
        self.dbroot.net = Net()
        self.net = self.dbroot.net
        transaction.commit()

    @QtCore.pyqtSlot()
    def switch_to_setup(self):
        self.stackl.setCurrentIndex(1)

    @QtCore.pyqtSlot()
    def switch_to_sessions(self):
        self.stackl.setCurrentIndex(0)

        
        
        
class NetContainer(QtWidgets.QWidget):
    

    def __init__(self):
        super().__init__()
            

def main():
    app = QtWidgets.QApplication(sys.argv)
    nc = NetControl()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

