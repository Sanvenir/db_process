#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from PyQt5 import QtWidgets

from pandas import Series

from db_process.ui_spcwindow import Ui_SPCWindow
from db_process.custom_class import MyFigureCanvas


class SPCWindow(QtWidgets.QMainWindow):
    def __init__(self, total_normal_data):
        super().__init__()
        self.spc_series = self.load_data(total_normal_data)
        self.spc_mean_series = Series([series.mean() for series in self.spc_series])
        self.spc_range_series = Series([series.max() - series.min() for series in self.spc_series])
        self.spc_date = [(series.first_valid_index(), series.last_valid_index()) for series in self.spc_series]

        self.ui = Ui_SPCWindow()
        self.ui.setupUi(self)

        # 添加图表
        self.figure_spc = Figure()
        self.ax_spc = self.figure_spc.add_subplot(111)
        self.figure_canvas = MyFigureCanvas(self.figure_spc)

        # 连接控件
        self.ui.button_spc.clicked.connect(self.refresh_button)
        self.ui.slider_spc.valueChanged.connect(self.plot_spc)

        self.figure_canvas.set_mouse_double_click(self.show_detail)

        self.ui.figure_layout.addWidget(self.figure_canvas)

        self.refresh_button()

        self.show()

    def refresh_button(self):
        """
        点击刷新按钮后的工作
        :return: 
        """
        self.update_widgets()
        self.ui.slider_spc.setValue(self.ui.spin_spc.value())
        self.plot_spc()

    def update_widgets(self):
        """
        刷新控件值
        :return: 
        """
        self.ui.slider_spc.setMaximum(len(self.spc_series) - self.ui.spin_range.value())
        self.ui.spin_spc.setMaximum(len(self.spc_series) - self.ui.spin_range.value())
        self.ui.total_part.setNum(len(self.spc_series))

    def plot_spc(self):
        self.ax_spc.clear()
        start = self.ui.spin_spc.value()
        end = self.ui.spin_spc.value() + self.ui.spin_range.value()
        ran = self.spc_range_series[start:end].mean() * 0.212
        self.ax_spc.plot(self.spc_mean_series[start:end])
        self.ax_spc.scatter(range(start, end), self.spc_mean_series[start:end])
        self.ax_spc.hlines(self.spc_mean_series[start:end].mean(), start, end)
        self.ax_spc.hlines(self.spc_mean_series[start:end].mean() + ran, start, end)
        self.ax_spc.hlines(self.spc_mean_series[start:end].mean() - ran, start, end)
        self.figure_canvas.draw()
        self.ui.statusbar.showMessage("当前分析点时间范围：{} - {}".format(self.spc_date[start][0],
                                                                 self.spc_date[end][1]))

    def show_detail(self):
        start = self.ui.spin_spc.value()
        end = self.ui.spin_spc.value() + self.ui.spin_range.value()
        for i in range(start, end):
            plt.plot(self.spc_series[i])
        plt.show()

    @staticmethod
    def load_data(total_normal_data):
        """
        导入数据，total_normal_data为主程序中导入的数据
        :param total_normal_data: 
        :return: 
        """
        spc_series = []
        current_part = 0
        while current_part + 16 < len(total_normal_data):
            spc_series.append(total_normal_data[current_part:current_part + 16])
            current_part += 16
        return spc_series

