#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import partial

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QVBoxLayout, QWidget, QLabel, QPushButton, QSizePolicy
from PyQt5 import QtWidgets, QtCore

from pandas import Series

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

import numpy as np

from db_process.custom_class import MyFigureCanvas
from db_process.config import Configuration as cf
from db_process.database import CompDataBase


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


class FixedLabel(QLabel):
    def __init__(self, *args):
        super().__init__(*args)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))


class CompDataProcess(object):
    def __init__(self, path, table, select_spindle_id, start_date, end_date, text_out=print):
        self.data = {}
        self.text_out = text_out
        for spindle in select_spindle_id:
            self.data[spindle] = SingleDataProcess()
        db = CompDataBase(path, table, text_out=self.text_out)
        if start_date is None or end_date is None:
            self.start_date, self.end_date = db.fetch_record(select_spindle_id, self.data)
        else:
            self.start_date, self.end_date = db.fetch_record_date(select_spindle_id, start_date, end_date, self.data)


class CompWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        from db_process.ui_comp_form import Ui_Form
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.start_time = None
        self.end_time = None

        self.torque_figure = Figure()
        self.ax_torque_comp = self.torque_figure.add_subplot(111)
        self.figure_canvas = MyFigureCanvas(self.torque_figure)

        layout_torque = QVBoxLayout()
        layout_torque.addWidget(self.figure_canvas)
        self.ui.tab_torque_var.setLayout(layout_torque)

        self.labels_qualification = {index : FixedLabel() for index in self.parent().comp_data_process.data.keys()}
        self.labels_mean = {index: FixedLabel() for index in self.parent().comp_data_process.data.keys()}
        self.labels_std = {index: FixedLabel() for index in self.parent().comp_data_process.data.keys()}
        self.labels_kurt = {index: FixedLabel() for index in self.parent().comp_data_process.data.keys()}
        self.labels_skew = {index: FixedLabel() for index in self.parent().comp_data_process.data.keys()}
        self.buttons_spindle = {index: QPushButton() for index in self.parent().comp_data_process.data.keys()}

        layout_qualification = QVBoxLayout()
        layout_mean = QVBoxLayout()
        layout_std = QVBoxLayout()
        layout_kurt = QVBoxLayout()
        layout_skew = QVBoxLayout()
        layout_spindle = QVBoxLayout()

        for key in self.parent().comp_data_process.data.keys():
            layout_qualification.addWidget(self.labels_qualification[key])
            layout_mean.addWidget(self.labels_mean[key])
            layout_std.addWidget(self.labels_std[key])
            layout_kurt.addWidget(self.labels_kurt[key])
            layout_skew.addWidget(self.labels_skew[key])
            layout_spindle.addWidget(self.buttons_spindle[key])
            self.buttons_spindle[key].setText("{}号枪".format(key))
            self.buttons_spindle[key].clicked.connect(partial(self.plot_hist, key))

        self.ui.groupBoxQualification.setLayout(layout_qualification)
        self.ui.groupBoxMean.setLayout(layout_mean)
        self.ui.groupBoxStd.setLayout(layout_std)
        self.ui.groupBoxKurt.setLayout(layout_kurt)
        self.ui.groupBoxSkew.setLayout(layout_skew)
        self.ui.groupBoxSpindleID.setLayout(layout_spindle)

        self.figure_canvas.set_mouse_double_click(self.plot_detail)

        # Part of QS Static
        self.buttons_QS = {index: QPushButton() for index in self.parent().comp_data_process.data.keys()}
        layout_qs_button = QVBoxLayout()
        for key in self.parent().comp_data_process.data.keys():
            layout_qs_button.addWidget(self.buttons_QS[key])
            self.buttons_QS[key].setText("{}号枪".format(key))
            self.buttons_QS[key].clicked.connect(partial(self.plot_static, key))
        self.ui.groupBoxQSButton.setLayout(layout_qs_button)

        self.qs_static_figure = Figure()
        self.ax_qs_static = self.qs_static_figure.add_subplot(111)
        self.qs_figure_canvas = MyFigureCanvas(self.qs_static_figure)
        self.ui.verticalLayoutStaticFigure.addWidget(self.qs_figure_canvas)

        self.display_update()
        self.check_static()

    def plot_static(self, spindle_id):
        self.ax_qs_static.clear()
        data = self.parent().comp_data_process.data[spindle_id].total_data
        assert isinstance(data, Series)
        self.ax_qs_static.pie(data[self.start_time:self.end_time].value_counts(), )
        self.qs_figure_canvas.draw()
        pass

    def plot_hist(self, spindle_id):
        plt.close()
        print(spindle_id)
        plt.hist(self.parent().comp_data_process.data[spindle_id].total_normal_data[self.start_time:self.end_time],
                 np.arange(12., 25., 0.2), histtype="stepfilled")
        plt.show()

    def check_static(self):
        data = self.parent().comp_data_process.data
        result = ""
        for spindle_id in range(1, 23):
            if spindle_id not in data.keys():
                self.ui.textBrowserStatic.setText("未获取所有拧紧枪数据")
                return
            value_counts = data[spindle_id].total_data.value_counts()
            for key in cf.qs_count.keys():
                if key in value_counts.keys():
                    cf.qs_count[key] += value_counts[key]
        for key, count in cf.qs_count.items():
            if count > 5:
                if result:
                    result += "；\n"
                result += cf.qs_result[key]
        if result:
            result += "。"
        else:
            result = "正常。"
        self.ui.textBrowserStatic.setText(result)

    def display_update(self):
        # update numbers
        self.ax_torque_comp.clear()
        self.start_time = self.parent().ui.dateEditStart.date().toString(Qt.ISODate)
        self.end_time = self.parent().ui.dateEditEnd.date().toString(Qt.ISODate)

        # plot
        for index, button in enumerate(self.parent().ui.buttonGroup.buttons()):
            key = index + 1
            self.parent().text_out("正在刷新{}号拧紧枪数据".format(key))
            if button.isEnabled():
                self.labels_mean[key].setVisible(button.isChecked())
                self.labels_std[key].setVisible(button.isChecked())
                self.labels_kurt[key].setVisible(button.isChecked())
                self.labels_skew[key].setVisible(button.isChecked())
                self.buttons_spindle[key].setVisible(button.isChecked())
                self.labels_qualification[key].setVisible(button.isChecked())
            if button.isChecked():
                self.labels_mean[key].setNum(
                    self.parent().comp_data_process.data[key].total_normal_data[self.start_time:self.end_time].mean())
                self.labels_std[key].setNum(
                    self.parent().comp_data_process.data[key].total_normal_data[self.start_time:self.end_time].std())
                self.labels_kurt[key].setNum(
                    self.parent().comp_data_process.data[key].total_normal_data[self.start_time:self.end_time].kurt())
                self.labels_skew[key].setNum(
                    self.parent().comp_data_process.data[key].total_normal_data[self.start_time:self.end_time].skew())
                self.labels_qualification[key].setText(
                    "{}号枪：{:<.2f}%".format(
                        key,
                        len(self.parent().comp_data_process.data[key].total_normal_data[self.start_time:self.end_time])
                        / len(self.parent().comp_data_process.data[key].total_data[self.start_time:self.end_time])
                        * 100)
                )
                if self.ui.radioButtonByTime.isChecked():
                    self.ax_torque_comp.plot(self.parent().comp_data_process.data[key].
                                             total_normal_data[self.start_time:self.end_time],
                                             label="Spindle {}".format(key))
                if self.ui.radioButtonByCount.isChecked():
                    self.ax_torque_comp.plot(self.parent().comp_data_process.data[key].
                                             total_normal_data[self.start_time:self.end_time].tolist(),
                                             label="Spindle {}".format(key))
                self.ax_torque_comp.legend()
        self.figure_canvas.draw()
        self.parent().text_out("完成")

    def plot_detail(self):
        plt.close()
        try:
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
        except Exception as err:
            msg_box = QMessageBox()
            msg_box.setText(self.tr("错误:{}\n可能为处理数据量过大，请尝试缩小时间范围再获取分布图".format(err)))
            msg_box.exec_()


class SelectDialog(QDialog):
    def __init__(self, path, table, parent=None, text_out=print):
        super().__init__(parent)
        from db_process.ui_spindle_dialog import Ui_Dialog
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.text_out = text_out

        self.setWindowFlags(Qt.Window)

        self.ui.dateEditEnd.setDate(QDate.currentDate())
        self.ui.dateEditStart.setDate(QDate.currentDate().addMonths(-cf.reverse_month))

        self.ui.pushButtonSelectAll.clicked.connect(self.select_all)
        self.ui.pushButtonSelectReverse.clicked.connect(self.select_reverse)

        self.comp_data_process = None
        self.comp_dialog = None

        self.path = path
        self.table = table

        self._state = LoadDialog

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
            self.comp_data_process = CompDataProcess(self.path, self.table, select_spindle_id, start_date, end_date,
                                                     text_out=self.text_out)
            self.setEnabled(True)
            self.change_state()
            self.comp_dialog = CompWidget(self)
            self.ui.horizontalLayout.addWidget(self.comp_dialog)
        except IndexError as err:
            msg_box = QMessageBox()
            msg_box.setText(self.tr("错误:{}\n请重新输入".format(err)))
            msg_box.exec_()
        except Exception as err:
            msg_box = QMessageBox()
            msg_box.setText("错误:{}".format(err))
            msg_box.exec_()
            return
        finally:
            self.setEnabled(True)


class SetDialog(SelectDialog):
    @staticmethod
    def accept(self):
        self.comp_dialog.display_update()
