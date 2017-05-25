#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import inf, NaN
from pandas import Series

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from db_process.database_mssql import FatigueDataBase
import db_process.fatigue_process as origin


class FatigueDataProcess(origin.FatigueDataProcess):
    def __init__(self, database, spindle_id, start_date, text_out=print, monitor=False):
        """
        处理数据
        :param database: 处理用数据库类型（class FatigueDataBase)
        :param spindle_id: 拧紧枪id
        :param start_date: 拧紧枪更换日期
        :param text_out: 输出方式（默认为print输出，应用一般为状态条输出）
        :param monitor: 兼容选项，无意义
        """
        self.data = database.fetch_new_record(spindle_id)
        self.start_date = start_date
        assert isinstance(self.data, Series)
        self.data_mean = self.data.resample('D').mean()
        self.data_max = self.data.resample('D').apply(self._average_largest)
        self.data_min = self.data.resample('D').apply(self._average_smallest)
        self.data_count = self.data.resample('D').apply(len)
        self.monitor = monitor


class FatigueDialog(origin.FatigueDialog):
    def __init__(self, text_out=print, monitor=False):
        QDialog.__init__(self)
        from db_process.ui_fatigue_dialog import Ui_Dialog
        self.monitor = monitor
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.spinBoxSpindleID.setMinimum(1)
        self.ui.spinBoxSpindleID.setMaximum(22)

        self.fatigue_figure = Figure()
        self.ax_fatigue = self.fatigue_figure.add_subplot(111)
        self.figure_canvas = FigureCanvas(self.fatigue_figure)

        layout_figure = QVBoxLayout()
        layout_figure.addWidget(self.figure_canvas)
        self.ui.groupBoxFigure.setLayout(layout_figure)
        self.data_process = None

        self.text_out = text_out

        self.setWindowFlags(Qt.Window)

        self.database = FatigueDataBase(self.text_out)

        self.ui.pushButtonUpdate.clicked.connect(self.update_fatigue)
        self.show()

    def update_fatigue(self):
        import pymssql
        try:
            self.ax_fatigue.clear()
            spindle_id = self.ui.spinBoxSpindleID.value()
            start_date = self.ui.dateEditUpdateDate.date().toString(Qt.ISODate)
            if self.monitor is True and self.data_process is not None:
                self.data_process.start_date = start_date
            else:
                self.data_process = FatigueDataProcess(self.database, spindle_id, start_date, monitor=self.monitor)
            fatigue = self.data_process.get_fatigue()
            self.ax_fatigue.plot(fatigue.cumsum())
            self.text_out("完成")
            self.figure_canvas.draw()
            assert isinstance(fatigue, Series)
            self.ui.labelCurrentFatigue.setNum(fatigue[-1])
        except pymssql.Error as err:
            msg_box = QMessageBox()
            msg_box.setText(self.tr("错误:{}\n可能为数据表名称错误，请重新输入".format(err)))
            msg_box.exec_()
        except Exception as err:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText(self.tr("错误:{}".format(err)))
            msg_box.exec_()
            return
