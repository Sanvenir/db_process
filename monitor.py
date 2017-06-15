#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from db_process.welcome_monitor import WelcomeWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = WelcomeWindow(r"E:\learn\2017毕设\data\拧紧.accdb", r"Screwing")
    win.show()
    sys.exit(app.exec_())
