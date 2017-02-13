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

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
				
    button = QtWidgets.QPushButton('This is Net Control v'+__version__)
    window.setCentralWidget(button)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
