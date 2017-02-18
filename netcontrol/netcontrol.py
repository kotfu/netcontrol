#!/usr/bin/env python3
# Copyright (c) 2017 Jared Crapo, K0TFU

"""
netcontrol.py

Tool for ham radio net controllers to run and log a net
"""

import sys
import os
from PyQt5 import QtWidgets
from netcontrol import __version__

class NetControl(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        button = QtWidgets.QPushButton('This is Net Control v'+__version__)
        self.setCentralWidget(button)
        
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
        
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    nc = NetControl()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

