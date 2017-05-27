#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from db_process.monitor_subclass import MonitorMainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MonitorMainWindow(r"C:\Users\sanve\Documents\Learn\db_process\拧紧.accdb", r"Screwing")
    sys.exit(app.exec_())
