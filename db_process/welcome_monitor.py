#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore

from db_process.ui_welcome import Ui_MainWindow


class WelcomeWindow(QMainWindow):
    def __init__(self, file_path, table):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)

        self.ui.actionOpenComp.triggered.connect(self.load_comp)
        self.ui.actionSpindleFatigue.triggered.connect(self.load_fatigue)
        self.ui.actionOpen.triggered.connect(self.load_single)

        self.ui.actionOpenMssql.triggered.connect(self.load_single_mssql)
        self.ui.actionFatigueMssql.triggered.connect(self.load_fatigue_mssql)
        self.ui.actionOpenCompMssql.triggered.connect(self.load_comp_mssql)

        self.resize(400, 400)

        self.text_out = self.ui.statusBar.showMessage
        self.file_name = file_path
        self.table_name = table

    def load_fatigue_mssql(self):
        """
        开启疲劳计算模块
        :return:
        """
        while True:
            import pypyodbc
            from db_process.fatigue_mssql import FatigueDialog
            try:
                self.fatigue_dialog = FatigueDialog(self.file_name, self.table_name, text_out=self.text_out,
                                                    monitor=True)
                return True
            except pypyodbc.Error as err:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText(self.tr("错误:{}\n请检查数据库文件".format(err)))
                msg_box.exec_()
                return False

    def load_comp_mssql(self):
        while True:
            import pypyodbc
            from db_process.multi import SelectDialog
            try:
                self.select_dialog = SelectDialog(self.file_name, self.table_name, text_out=self.text_out)
                self.select_dialog.ui.checkBoxAllData.setChecked(True)
                self.select_dialog.accept()
                self.select_dialog.show()
                return True
            except pypyodbc.Error as err:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText(self.tr("错误:{}\n请检查数据库文件".format(err)))
                msg_box.exec_()
                return False

    def load_single_mssql(self):
        from db_process.monitor_subclass import MonitorMainWindow
        self.single_window = MonitorMainWindow(self.file_name, self.table_name)

    def load_fatigue(self):
        """
        开启疲劳计算模块
        :return:
        """
        file_name, ok = QtWidgets.QFileDialog.getOpenFileName(
            self, caption=self.tr("打开数据库"), filter=self.tr("Database Files (*.accdb)"))
        if not ok:
            return
        table_name, ok = QtWidgets.QInputDialog.getText(self, self.tr("请输入"), self.tr("表名"))
        if not (ok and table_name):
            return
        while True:
            import pypyodbc
            from db_process.fatigue_mssql import FatigueDialog
            try:
                self.fatigue_dialog = FatigueDialog(file_name, table_name, text_out=self.text_out)
                return True
            except pypyodbc.Error as err:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText(self.tr("错误:{}\n可能为数据表名称错误，请重新输入".format(err)))
                msg_box.exec_()
                self.text_out("请等待重新输入")
                table_name, ok = QtWidgets.QInputDialog.getText(self, self.tr("请输入"), self.tr("表名"))
                if not (ok and table_name):
                    return

    def load_comp(self):
        """
        读取数据库以对比拧紧枪
        :return:
        """
        file_name, ok = QtWidgets.QFileDialog.getOpenFileName(
            self, caption=self.tr("打开数据库"), filter=self.tr("Database Files (*.accdb)"))
        if not ok:
            return
        table_name, ok = QtWidgets.QInputDialog.getText(self, self.tr("请输入"), self.tr("表名"))
        if not (ok and table_name):
            return
        while True:
            import pypyodbc
            from db_process.multi import SelectDialog
            try:
                self.select_dialog = SelectDialog(file_name, table_name, text_out=self.text_out)
                self.select_dialog.show()
                return True
            except pypyodbc.Error as err:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText(self.tr("错误:{}\n可能为数据表名称错误，请重新输入".format(err)))
                msg_box.exec_()
                self.text_out("请等待重新输入")
                table_name, ok = QtWidgets.QInputDialog.getText(self, self.tr("请输入"), self.tr("表名"))
                if not (ok and table_name):
                    return

    def load_single(self):
        from db_process.single_interface import MainWindow
        self.single_window = MainWindow()
