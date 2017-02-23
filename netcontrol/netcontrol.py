#!/usr/bin/env python3
# Copyright (c) 2017 Jared Crapo, K0TFU

"""
netcontrol.py

Tool for ham radio net controllers to run and log a net
"""

import sys
import os
from PyQt5 import QtWidgets
import transaction
import ZODB

from netcontrol.net import Net
from netcontrol import __version__

class NetControl(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.initDB()
    
    def initUI(self):
        self.setWindowTitle('This is Net Control v'+__version__)
        
        name_edit = QtWidgets.QLineEdit()
        freq_edit = QtWidgets.QLineEdit()
        session_list = QtWidgets.QListWidget()
        new_button = QtWidgets.QPushButton('New')
        
        grid = QtWidgets.QGridLayout()
        grid.addWidget(name_edit,0,0)
        grid.addWidget(freq_edit,0,1)
        grid.addWidget(session_list,1,0,1,2)
        grid.addWidget(new_button,2,1)
        
        
        mc = MainContainer()
        mc.setLayout(grid)
        self.setCentralWidget(mc)
        
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

class MainContainer(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
            

def main():
    app = QtWidgets.QApplication(sys.argv)
    nc = NetControl()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

