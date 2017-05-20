#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from db_process.interface_mssql import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
