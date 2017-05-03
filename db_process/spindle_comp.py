#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

import matplotlib
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QVBoxLayout
from pandas import Series

from db_process.config import Configuration as cf
from db_process.database import DataBase

matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from db_process.custom_class import MyFigureCanvas


class CompDataBase(DataBase):
    def __init__(self, path, table):
        """
        读取拧紧枪数据库文件
        :param path: 数据库文件绝对路径
        :param table: 数据表名称
        """
        super().__init__(path, table)

    def fetch_record(self, spindle_id, data):
        """
        获取数据库数据
        :param spindle_id: 所需获取的拧紧枪号集合 
        :param data: 将数据存入该字典中，关键字为拧紧枪号，内容为每个拧紧枪的SingleDataProcess
        :return: 选取数据的开始时间与结束时间
        """
        self.cur.execute("""
        SELECT SpindleID, Date, TorqueAct, QSCode
        FROM {}""".format(self.table))
        print("读取数据中……")
        row = self.cur.fetchone()
        if row is None:
            raise IndexError("没有数据")
        start_date = row[1]
        end_date = None
        while row is not None:
            if row[0] not in spindle_id:
                continue
            end_date = row[1]
            if row[3] == 1:
                data[row[0]].total_normal_data[end_date] = row[2]
            data[row[0]].total_data[end_date] = row[3]
            row = self.cur.fetchone()
        print("序列化……")
        for spindle in data.values():
            spindle.serieslize()
        return start_date, end_date

    def fetch_record_date(self, spindle_id, start_date, end_date, data):
        """
        按时间读取数据
        :param spindle_id: 
        :param start_date: 开始日期
        :param end_date: 结束日期
        :param data: 
        :return: 
        """
        self.cur.execute("""
        SELECT SpindleID, Date, TorqueAct, QSCode
        FROM {} WHERE DateDiff('d', '{}', Date)>0 AND DateDiff('d', '{}', Date)<0""".
                         format(self.table, start_date, end_date))
        print("读取数据中……")
        row = self.cur.fetchone()
        if row is None:
            raise IndexError("选定范围内没有数据")
        start_date = row[1]
        while row is not None:
            if row[0] not in spindle_id:
                continue
            end_date = row[1]
            if row[3] == 1:
                data[row[0]].total_normal_data[end_date] = row[2]
            data[row[0]].total_data[end_date] = row[3]
            row = self.cur.fetchone()
        if not data.keys():
            raise IndexError("选定范围内没有数据")
        print("序列化……")
        for spindle in data.values():
            spindle.serieslize()
        return start_date, end_date


class SingleDataProcess(object):
    def __init__(self):
        self.total_data = {}
        self.total_normal_data = {}

    def serieslize(self):
        """
        Convert total_data and total_normal_data to Series
        :return: 
        """
        self.total_data = Series(self.total_data)
        self.total_normal_data = Series(self.total_normal_data)


class CompDataProcess(object):
    def __init__(self, select_spindle_id, start_date, end_date):
        self.data = {}
        for spindle in select_spindle_id:
            self.data[spindle] = SingleDataProcess()
        db = CompDataBase(r"C:\Users\sanve\OneDrive\文档\课程\2017毕设\拧紧\拧紧.accdb", "Screwing")
        if start_date is None or end_date is None:
            self.start_date, self.end_date = db.fetch_record(select_spindle_id, self.data)
        else:
            self.start_date, self.end_date = db.fetch_record_date(select_spindle_id, start_date, end_date, self.data)


class CompDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        from Scripts.ui_comp_dialog import Ui_Dialog
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.start_time = None
        self.end_time = None

        self.setGeometry(self.parent().x() + self.parent().width() + 10, self.parent().y() + 55,
                         1000, self.parent().rect().height())

        self.torque_figure = Figure()
        self.ax_torque_comp = self.torque_figure.add_subplot(111)
        self.figure_canvas = MyFigureCanvas(self.torque_figure)

        layout_torque = QVBoxLayout()
        layout_torque.addWidget(self.figure_canvas)
        self.ui.tab_torque_var.setLayout(layout_torque)

        self.figure_canvas.set_mouse_double_click(self.plot_detail)

        self.plot()
        self.show()

    def plot(self):
        self.ax_torque_comp.clear()
        self.start_time = self.parent().ui.dateEditStart.date().toString(Qt.ISODate)
        self.end_time = self.parent().ui.dateEditEnd.date().toString(Qt.ISODate)
        for index, button in enumerate(self.parent().ui.buttonGroup.buttons()):
            if button.isChecked():
                if self.ui.radioButtonByTime.isChecked():
                    self.ax_torque_comp.plot(self.parent().comp_data_process.data[index + 1].
                                             total_normal_data[self.start_time:self.end_time],
                                             label="Spindle {}".format(index + 1))
                if self.ui.radioButtonByCount.isChecked():
                    self.ax_torque_comp.plot(self.parent().comp_data_process.data[index + 1].
                                             total_normal_data[self.start_time:self.end_time].tolist(),
                                             label="Spindle {}".format(index + 1))
                self.ax_torque_comp.legend()
        self.figure_canvas.draw()

    def plot_detail(self):
        plt.close()
        for index, button in enumerate(self.parent().ui.buttonGroup.buttons()):
            if button.isChecked():
                if self.ui.radioButtonByTime.isChecked():
                    plt.plot(self.parent().comp_data_process.data[index + 1].
                             total_normal_data[self.start_time:self.end_time],
                             label="Spindle {}".format(index + 1))
                if self.ui.radioButtonByCount.isChecked():
                    plt.plot(self.parent().comp_data_process.data[index + 1].
                             total_normal_data[self.start_time:self.end_time].tolist(),
                             label="Spindle {}".format(index + 1))
                plt.legend()
        plt.show()


class SelectDialog(QDialog):
    def __init__(self, state, parent=None):
        super().__init__(parent)
        from Scripts.ui_spindle_dialog import Ui_Dialog
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.dateEditEnd.setDate(QDate.currentDate())
        self.ui.dateEditStart.setDate(QDate.currentDate().addMonths(-cf.reverse_month))

        self.ui.pushButtonSelectAll.clicked.connect(self.select_all)
        self.ui.pushButtonSelectReverse.clicked.connect(self.select_reverse)

        self.comp_data_process = None
        self.comp_dialog = None

        self._state = state

    def select_all(self):
        """
        全选
        :return: 
        """
        for button in self.ui.buttonGroup.buttons():
            button.setChecked(True)

    def select_reverse(self):
        """
        反选
        :return: 
        """
        for button in self.ui.buttonGroup.buttons():
            button.setChecked(not button.isChecked())

    def change_state(self):
        """
        改变类状态，从打开数据库变为设置绘图状态
        :return: 
        """
        self._state = SetDialog
        self.ui.checkBoxAllData.setEnabled(False)
        self.ui.dateEditStart.setEnabled(True)
        self.ui.dateEditEnd.setEnabled(True)
        self.ui.dateEditStart.setMinimumDate(
            QDate.fromString(str(self.comp_data_process.start_date.date()), "yyyy-MM-dd"))
        self.ui.dateEditStart.setMaximumDate(
            QDate.fromString(str(self.comp_data_process.end_date.date()), "yyyy-MM-dd"))
        self.ui.dateEditStart.setDate(
            QDate.fromString(str(self.comp_data_process.start_date.date()), "yyyy-MM-dd"))
        self.ui.dateEditEnd.setMinimumDate(
            QDate.fromString(str(self.comp_data_process.start_date.date()), "yyyy-MM-dd"))
        self.ui.dateEditEnd.setMaximumDate(
            QDate.fromString(str(self.comp_data_process.end_date.date()), "yyyy-MM-dd"))
        self.ui.dateEditEnd.setDate(
            QDate.fromString(str(self.comp_data_process.end_date.date()), "yyyy-MM-dd"))

    def reverse_state(self):
        self._state = LoadDialog
        self.ui.dateEditStart.clearMinimumDate()
        self.ui.dateEditStart.clearMaximumDate()
        self.ui.dateEditEnd.clearMinimumDate()
        self.ui.dateEditEnd.clearMaximumDate()
        for button in self.ui.buttonGroup.buttons():
            button.setEnabled(True)

    def accept(self):
        self._state.accept(self)


class LoadDialog(SelectDialog):
    @staticmethod
    def accept(self):
        """
        打开数据库状态下，点击确定显示数据分析窗口
        :param self: 
        :return: 
        """
        select_spindle_id = set()
        for index, button in enumerate(self.ui.buttonGroup.buttons()):
            if button.isChecked():
                select_spindle_id.add(index + 1)
            else:
                button.setEnabled(False)
        if self.ui.checkBoxAllData.isChecked():
            start_date = end_date = None
        else:
            start_date, end_date = self.ui.dateEditStart.date().toString(Qt.ISODate),\
                                   self.ui.dateEditEnd.date().toString(Qt.ISODate)

        self.setEnabled(False)
        try:
            self.comp_data_process = CompDataProcess(select_spindle_id, start_date, end_date)
            self.setEnabled(True)
            self.change_state()
            self.comp_dialog = CompDialog(self)
            self.comp_dialog.exec()
            self.close()
        except IndexError as err:
            msg_box = QMessageBox()
            msg_box.setText(self.tr("错误:{}\n请重新输入".format(err)))
            msg_box.exec_()
        finally:
            self.setEnabled(True)


class SetDialog(SelectDialog):
    @staticmethod
    def accept(self):
        self.comp_dialog.plot()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = SelectDialog(LoadDialog)
    dialog.show()
    sys.exit(app.exec_())