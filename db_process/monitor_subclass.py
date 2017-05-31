#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5 import QtWidgets, QtCore

from pandas import Series
from datetime import datetime

from db_process.single_interface import MainWindow
from db_process.single_process import ScrewingDataProcess
from db_process.database import CompDataBase


class MonitorMainWindow(MainWindow):
    def __init__(self, file_path, table):
        super().__init__()
        self.monitor_db = CompDataBase(file_path, table, self.text_out)
        self.file_name = file_path
        self.table_name = table

    def load(self):
        self.clear_all()
        spindle_id, ok = QtWidgets.QInputDialog.getInt(self, self.tr("请输入"), self.tr("查询枪号"), 1, 1, 22)
        if not ok:
            return

        while True:
            import pypyodbc
            try:
                self.data = ScrewingDataProcess(
                    self.file_name, self.table_name, spindle_id,
                    text_out=self.ui.statusBar.showMessage, fetch_new_data=True)
                break
            except pypyodbc.Error as err:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText(self.tr("错误:{}\n指定数据表不存在，请检查".format(err)))
                msg_box.exec_()
                return
            except IndexError as err:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText(self.tr("错误:{}\n本段时间内数据量可能为空，请检查".format(err)))
                msg_box.exec_()
                return
        self.text_out("完成")
        self.spindle_id = spindle_id

        try:
            self.ui.start_time.setMinimumDate(
                QDate.fromString(str(self.data.part_date[0].date()), "yyyy-MM-dd"))
            self.ui.start_time.setMaximumDate(
                QDate.fromString(str(self.data.part_date[-1].date()), "yyyy-MM-dd"))
            self.ui.start_time.setDate(
                QDate.fromString(str(self.data.part_date[0].date()), "yyyy-MM-dd"))
            self.ui.end_time.setMinimumDate(
                QDate.fromString(str(self.data.part_date[0].date()), "yyyy-MM-dd"))
            self.ui.end_time.setMaximumDate(
                QDate.fromString(str(self.data.part_date[-1].date()), "yyyy-MM-dd"))
            self.ui.end_time.setDate(
                QDate.fromString(str(self.data.part_date[-1].date()), "yyyy-MM-dd"))
            self.ui.start_num.setMinimum(0)
            self.ui.start_num.setMaximum(len(self.data.part_date) - 1)
            self.ui.start_num.setValue(0)
            self.ui.end_num.setMinimum(0)
            self.ui.end_num.setMaximum(len(self.data.part_date) - 1)
            self.ui.end_num.setValue(len(self.data.part_date) - 1)

            # 激活控件
            self.ui.actionChange_Spindle_ID.setEnabled(True)
            self.ui.actionAddSpindle.setEnabled(True)
            self.ui.centralWidget.setEnabled(True)
            self.ui.centralWidget.setEnabled(True)
            self.ui.menuBar.setEnabled(True)
            self.ui.menuspc_figure.setEnabled(True)
            self.ui.menuPlotFrequence.setEnabled(True)
            self.comp_data = None

            # 以时间为横轴作图
            self.plot_by_time()
        except IndexError as err:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText(self.tr("错误:{}\n可能为分组量过大，无法生成有效分组".format(err)))
            msg_box.exec_()
            self.text_out("请重新设定分组数")
            self.time_period = [None, None]
            self.data = None

    def change_spindle_id(self):
        """
        改变拧紧枪号
        :return: 
        """
        self.clear_all()
        spindle_id, ok = QtWidgets.QInputDialog.getInt(self, self.tr("请输入"), self.tr("查询枪号"), 1, 1, 22)
        if spindle_id == self.spindle_id:
            self.text_out("与当前存储数据ID相同")
            return
        self.spindle_id = spindle_id
        self.data = ScrewingDataProcess(
            self.file_name, self.table_name, spindle_id,
            text_out=self.ui.statusBar.showMessage, fetch_new_data=True)
        self.comp_data = None
        self.text_out("完成")
        self.plot_by_time()

    def add_comp_spindle(self):
        """
        添加对比拧紧枪
        :return: 
        """
        spindle_id, ok = QtWidgets.QInputDialog.getInt(self, self.tr("请输入"), self.tr("对比枪号"), 1, 1, 22)
        if spindle_id == self.spindle_id:
            self.text_out("与当前分析拧紧枪ID相同")
            return
        if spindle_id == self.comp_spindle_id:
            self.text_out("与当前对比拧紧枪ID相同")
            return
        self.comp_spindle_id = spindle_id
        self.data = ScrewingDataProcess(
            self.file_name, self.table_name, spindle_id,
            text_out=self.ui.statusBar.showMessage, fetch_new_data=True)
        self.text_out("完成")
        self.plot_by_time()

    def load_comp(self):
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

    def load_fatigue(self):
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

