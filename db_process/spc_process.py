#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from PyQt5 import QtWidgets, QtCore

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
        self.setWindowState(Qt.WindowMaximized)

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
        self.ui.slider_spc.setMaximum(len(self.spc_series) - self.ui.spin_range.value() - 1)
        self.ui.spin_spc.setMaximum(len(self.spc_series) - self.ui.spin_range.value() - 1)
        self.ui.total_part.setNum(len(self.spc_series))

    def plot_spc(self):
        self.ax_spc.clear()
        start = self.ui.spin_spc.value()
        end = self.ui.spin_spc.value() + self.ui.spin_range.value()
        ran = self.spc_range_series[start:end].mean() * 0.212

        cl = self.spc_mean_series[start:end].mean()
        ucl1 = cl + ran / 3
        ucl2 = cl + ran / 3 * 2
        ucl3 = cl + ran
        lcl1 = cl - ran / 3
        lcl2 = cl - ran / 3 * 2
        lcl3 = cl - ran

        self.ax_spc.plot(self.spc_mean_series[start:end])
        self.ax_spc.scatter(range(start, end), self.spc_mean_series[start:end])
        self.ax_spc.hlines(cl, start, end)
        self.ax_spc.hlines(ucl1, start, end, color="green")
        self.ax_spc.hlines(lcl1, start, end, color="green")
        self.ax_spc.hlines(ucl2, start, end, color="orange")
        self.ax_spc.hlines(lcl2, start, end, color="orange")
        self.ax_spc.hlines(ucl3, start, end, color="red")
        self.ax_spc.hlines(lcl3, start, end, color="red")
        self.figure_canvas.draw()
        self.ui.statusbar.showMessage("当前分析点时间范围：{} - {}".format(self.spc_date[start][0],
                                                                 self.spc_date[end][1]))

        # 判断SPC状态
        # 是否为“有点过界”
        for i in range(start, end):
            if self.spc_mean_series[i] > ucl3 or self.spc_mean_series[i] < lcl3:
                self.ui.label_type.setText("有点过界")
                return

        # 是否为“倾向”
        for i in range(start + 1, end - 6):
            if self.spc_mean_series[i] == self.spc_mean_series[i - 1]:
                continue
            position = (self.spc_mean_series[i] > self.spc_mean_series[i - 1])
            for j in range(6):
                if self.spc_mean_series[i + j] == self.spc_mean_series[i + j - 1] or\
                                position != (self.spc_mean_series[i + j] > self.spc_mean_series[i + j - 1]):
                    break
            else:
                if position:
                    self.ui.label_type.setText("有上行倾向")
                else:
                    self.ui.label_type.setText("有下行倾向")
                return

        # 是否为“间断链”
        check_list = [(11, 10), (14, 12), (17, 14), (20, 16)]
        for check_num, check_count in check_list:
            for i in range(start, end - check_num):
                u_over_count = 0
                l_over_count = 0
                for j in range(check_num):
                    if self.spc_mean_series[i + j] > cl:
                        u_over_count += 1
                    if self.spc_mean_series[i + j] < cl:
                        l_over_count += 1
                if u_over_count > check_count or l_over_count > check_count:
                    self.ui.label_type.setText("间断链")
                    return

        # 是否为链异常
        for i in range(start, end - 9):
            if self.spc_mean_series[i] == cl:
                continue
            position = (self.spc_mean_series[i] > cl)
            for j in range(9):
                if position != (self.spc_mean_series[i + j] > cl) or self.spc_mean_series[i + j] == cl:
                    break
            else:
                self.ui.label_type.setText("链异常")
                return

        # 是否为“点屡屡接近控制线”
        for i in range(start, end - 3):
            over_count = 0
            for j in range(3):
                if self.spc_mean_series[i + j] > ucl2 or self.spc_mean_series[i + j] < lcl2:
                    over_count += 1
            if over_count > 1:
                self.ui.label_type.setText("点屡屡接近控制线")
                return

        self.ui.label_type.setText("正常")

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
