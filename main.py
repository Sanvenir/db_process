#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from db_process.interface import MainWindow
from db_process.welcome import WelcomeWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = WelcomeWindow()
    win.show()
    sys.exit(app.exec_())
