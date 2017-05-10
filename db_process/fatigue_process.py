#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import inf, NaN
from pandas import Series

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from db_process.database import DataBase


class FatigueDataBase(DataBase):
    def __init__(self, path, table, text_out=print):
        """
        读取拧紧枪数据库文件
        :param path: 数据库文件绝对路径
        :param table: 数据表名称
        """
        super().__init__(path, table)
        self.text_out = text_out

    def fetch_record(self, spindle_id, start_date):
        self.text_out("开始查询")
        self.cur.execute("""
        SELECT Date, TorqueAct
        FROM {}
        WHERE DateDiff('d', '{}', Date)>0 AND QSCode=1 AND SpindleID={}"""
                         .format(self.table, start_date, spindle_id))
        self.text_out("开始读取")
        return Series(dict(self.cur.fetchall()))


class FatigueDataProcess(object):
    def __init__(self, database, spindle_id, start_date, text_out=print):
        """
        处理数据
        :param database: 处理用数据库类型（class FatigueDataBase)
        :param spindle_id: 拧紧枪id
        :param start_date: 拧紧枪更换日期
        :param text_out: 输出方式（默认为print输出，应用一般为状态条输出）
        """
        self.data = database.fetch_record(spindle_id, start_date)
        assert isinstance(self.data, Series)
        self.data_mean = self.data.resample('D').mean()
        self.data_max = self.data.resample('D').apply(self._10_percent_largest)
        self.data_min = self.data.resample('D').apply(self._10_percent_smallest)
        self.data_count = self.data.resample('D').apply(len)

    def get_fatigue(self):
        r = self.data_min / self.data_max
        wp = 0.00000004241150082
        tau_m = self.data_mean / wp
        tau_ln = 202110000
        tau_b = 648000000
        tau_r = tau_ln * (1 - tau_m / tau_b)
        tau_a = (self.data_max - self.data_min) / wp

        nf = 378000000 * 1 / (4 * (1 / 2 / (1 - r)) * tau_a.combine(tau_r, self._combine_func) ** 2)

        di = 3.5 * self.data_count / nf
        print(di.dropna())

        return di.dropna().cumsum()

    @staticmethod
    def _combine_func(tau_a, tau_r):
        if tau_a > tau_r:
            return tau_a - tau_r
        return 0.

    @staticmethod
    def _10_percent_largest(array_like):
        if array_like.empty:
            return inf
        return array_like.nlargest(len(array_like) // 10).min()

    @staticmethod
    def _10_percent_smallest(array_like):
        if array_like.empty:
            return 0
        return array_like.nsmallest(len(array_like) // 10).max()


class FatigueDialog(QDialog):
    def __init__(self, path, table, text_out=print):
        super().__init__()
        from db_process.ui_fatigue_dialog import Ui_Dialog
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

        self.text_out = text_out

        self.setWindowFlags(Qt.Window)

        self.database = FatigueDataBase(path, table, self.text_out)

        self.ui.pushButtonUpdate.clicked.connect(self.update_fatigue)
        self.show()

    def update_fatigue(self):
        import pypyodbc
        try:
            self.ax_fatigue.clear()
            spindle_id = self.ui.spinBoxSpindleID.value()
            start_date = self.ui.dateEditUpdateDate.date().toString(Qt.ISODate)
            data_process = FatigueDataProcess(self.database, spindle_id, start_date)
            fatigue = data_process.get_fatigue()
            self.ax_fatigue.plot(fatigue)
            self.text_out("完成")
            self.figure_canvas.draw()
            assert isinstance(fatigue, Series)
            self.ui.labelCurrentFatigue.setNum(fatigue[-1])
        except pypyodbc.Error as err:
            msg_box = QMessageBox()
            msg_box.setText(self.tr("错误:{}\n可能为数据表名称错误，请重新输入".format(err)))
            msg_box.exec_()
            self.text_out("请等待重新输入")
            table_name, ok = QInputDialog.getText(self, self.tr("请输入"), self.tr("表名"))
            if ok:
                self.database.table = table_name


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dialog = FatigueDialog(r"C:\Users\sanve\OneDrive\文档\课程\2017毕设\data\20140901-20150807 - ok.accdb", "aaa")
    # dialog = FatigueDialog(r"C:\Users\sanve\OneDrive\文档\课程\2017毕设\拧紧\拧紧.accdb", "Screwing")
    app.exec_()
