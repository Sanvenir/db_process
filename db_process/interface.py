#!/usr/bin/python  
# -*- coding: utf-8 -*-  
import sys

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QDate, Qt, QThread, QTimer

from db_process.ui_mainwindow import Ui_MainWindow
from db_process.ui_datewindow import Ui_Dialog

from db_process.process import ScrewingDataProcess
from db_process.config import Configuration as cf


def log_load(cls):
    """
    防止读取数据时点击操作按钮引起故障，在读数时disable操作控件
    :param cls: 
    :return: 
    """
    load = cls.load

    def new_load(self):
        self.ui.centralWidget.setEnabled(False)
        self.ui.menuBar.setEnabled(False)
        result = load(self)
        self.ui.menuBar.setEnabled(True)
        if self.data is None:
            return result
        self.ui.centralWidget.setEnabled(True)
        self.ui.menuSetting.setEnabled(False)
        return result
    cls.load = new_load
    return cls


@log_load
class MainWindow(QMainWindow):
    """
    程序主窗口程序，UI文件为UI_MainWindow
    """
    def __init__(self):
        super().__init__()

        # 定义内部变量
        self.data = None  # 分析数据
        self.comp_data = None  # 对比数据
        self.file_name = None  # 文件名
        self.table_name = None  # 表名
        self.spindle_id = None  # 当前拧紧枪id
        self.comp_spindle_id = None  # 对比用拧紧枪id
        self.spcwindow = None
        self.time_period = [None, None]  # 分析时间段，[开始时间，结束时间]
        # 当前数据的起始组数
        self.current_start_num = None
        # 当前数据的结束组数
        self.current_end_num = None
        # 当前数据的起始时间
        self.current_start_time = None
        # 当前数据的结束时间
        self.current_end_time = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 状态信息显示在状态栏中
        self.text_out = self.ui.statusBar.showMessage

        # 消息connect
        self.ui.actionOpen.triggered.connect(self.load)
        self.ui.actionChange_Spindle_ID.triggered.connect(self.change_spindle_id)
        self.ui.actionAddSpindle.triggered.connect(self.add_comp_spindle)
        self.ui.actionClear_ALL.triggered.connect(self.clear_all)
        self.ui.actionClearTorque.triggered.connect(self.clear_torque)
        self.ui.button_time.clicked.connect(self.plot_by_time)
        self.ui.button_num.clicked.connect(self.plot_by_part)
        self.ui.button_detial_time.clicked.connect(self.plot_detail_time)
        self.ui.button_detial_num.clicked.connect(self.plot_detail_num)
        self.ui.actionspc_xr.triggered.connect(self.spc_show)
        self.ui.actionPartNum.triggered.connect(self.set_series_num)
        self.ui.actionReverseTime.triggered.connect(self.set_reverse_month)
        self.ui.actionDefaultReadTime.triggered.connect(self.set_divide_time)
        self.ui.actionDefaultLatestNum.triggered.connect(self.set_default_latest_num)
        self.ui.actionPlotSpecgram.triggered.connect(self.plot_specgram)
        self.ui.actionPlotFFT.triggered.connect(self.plot_fft)
        self.ui.actionOpenComp.triggered.connect(self.load_comp)
        self.ui.actionSpindleFatigue.triggered.connect(self.load_fatigue)

        # 生产量信息图表，包括生产量子图和生产合格率子图
        self.figure_production = Figure()
        self.ax_production = self.figure_production.add_subplot(211)
        self.ax_qualification = self.figure_production.add_subplot(212)
        self.figure_canvas_production = FigureCanvas(self.figure_production)

        # 扭矩信息图表，包括扭矩平均值子图，标准差子图，扭矩分布直方图
        self.figure_torque = Figure()
        self.ax_torque_mean = self.figure_torque.add_subplot(311)
        self.ax_torque_std = self.figure_torque.add_subplot(312)
        self.ax_torque_hist = self.figure_torque.add_subplot(313)
        self.figure_canvas_torque = FigureCanvas(self.figure_torque)

        # 添加图表
        layout_production = QtWidgets.QVBoxLayout()
        layout_production.addWidget(self.figure_canvas_production)
        self.ui.figure_production.setLayout(layout_production)
        layout_figure = QtWidgets.QVBoxLayout()
        layout_figure.addWidget(self.figure_canvas_torque)
        self.ui.figure_torque.setLayout(layout_figure)

        self.show()

    def spc_show(self):
        from db_process.spc_process import SPCWindow
        self.spcwindow = SPCWindow(self.data.total_normal_data)

    @staticmethod
    def plot_detail(*args, **kwargs):
        plt.close()
        try:
            plt.figure(1)
            plt.plot(args, kwargs)
            plt.legend()
            plt.show()
        except Exception as err:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText("错误:{}".format(err))
            msg_box.exec_()
            return

    def plot_detail_time(self):
        """
        利用matplotlit的pyplot做出以时间为横轴的详细数据图，包括生产量数据子图（每日产量和每日合格率），扭矩数据子图（分
        组扭矩均值和标准差）
        :return: 
        """
        plt.close()
        try:
            plt.figure(1)
            plt.subplot(211)
            plt.plot(self.data.part_date[self.current_start_num:self.current_end_num],
                     self.data.part_mean[self.current_start_num:self.current_end_num],
                     label="ID {} mean".format(self.spindle_id))
            plt.plot(self.data.part_date[self.current_start_num:self.current_end_num],
                     self.data.part_std[self.current_start_num:self.current_end_num],
                     label="ID {} std".format(self.spindle_id))
            if self.comp_data is not None:
                plt.plot(self.comp_data.part_date[self.current_start_num:self.current_end_num],
                         self.comp_data.part_mean[self.current_start_num:self.current_end_num],
                         label="ID {} mean".format(self.comp_spindle_id))
                plt.plot(self.comp_data.part_date[self.current_start_num:self.current_end_num],
                         self.comp_data.part_std[self.current_start_num:self.current_end_num],
                         label="ID {} std".format(self.comp_spindle_id))
            plt.legend()
            plt.subplot(212)
            plt.plot(self.data.daily_production[self.current_start_time:self.current_end_time],
                     label="Daily Production".format(self.spindle_id))
            plt.fill_between(
                self.data.daily_production[self.current_start_time:self.current_end_time].index,
                self.data.daily_qualified_production[self.current_start_time:self.current_end_time],
                label="Qualification Production")
            plt.legend()
            plt.show()
        except Exception as err:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText("错误:{}".format(err))
            msg_box.exec_()
            return

    def plot_detail_num(self):
        """
        利用matplotlit的pyplot做出以组数为横轴的详细数据图，包括扭矩数据子图（分组扭矩均值和标准差），组数与时间对应关系
        子图
        :return: 
        """
        plt.close()
        try:
            plt.figure(1)
            plt.subplot(211)
            plt.plot(range(self.current_start_num, self.current_end_num),
                     self.data.part_mean[self.current_start_num:self.current_end_num],
                     label="ID {} mean".format(self.spindle_id))
            plt.plot(range(self.current_start_num, self.current_end_num),
                     self.data.part_std[self.current_start_num:self.current_end_num],
                     label="ID {} std".format(self.spindle_id))
            if self.comp_data is not None:
                plt.plot(range(self.current_start_num, self.current_end_num),
                         self.comp_data.part_mean[self.current_start_num:self.current_end_num],
                         label="ID {} mean".format(self.comp_spindle_id))
                plt.plot(range(self.current_start_num, self.current_end_num),
                         self.comp_data.part_std[self.current_start_num:self.current_end_num],
                         label="ID {} std".format(self.comp_spindle_id))
            plt.legend()
            plt.subplot(212)
            plt.plot(self.data.part_date[self.current_start_num:self.current_end_num])
            plt.show()
        except Exception as err:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText("错误:{}".format(err))
            msg_box.exec_()
            return

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
            from db_process.fatigue_process import FatigueDialog
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
            from db_process.spindle_comp import SelectDialog
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

    def load(self):
        """
        读取数据库
        :return: 
        """
        self.clear_all()
        file_name, ok = QtWidgets.QFileDialog.getOpenFileName(
            self, caption=self.tr("打开数据库"), filter=self.tr("Database Files (*.accdb)"))
        if not ok:
            return
        table_name, ok = QtWidgets.QInputDialog.getText(self, self.tr("请输入"), self.tr("表名"))
        if not (ok and table_name):
            return
        spindle_id, ok = QtWidgets.QInputDialog.getInt(self, self.tr("请输入"), self.tr("查询枪号"), 1, 1, 22)
        if not ok:
            return
        self.time_period = [None, None]
        while True:
            import pypyodbc
            try:
                self.data = ScrewingDataProcess(
                    file_name, table_name, spindle_id, self.time_period, text_out=self.ui.statusBar.showMessage)
                break
            except pypyodbc.Error as err:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText(self.tr("错误:{}\n可能为数据表名称错误，请重新输入".format(err)))
                msg_box.exec_()
                self.text_out("请等待重新输入")
                table_name, ok = QtWidgets.QInputDialog.getText(self, self.tr("请输入"), self.tr("表名"))
                if not (ok and table_name):
                    return
            except IndexError as err:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText(self.tr("错误:{}\n本段时间内数据量可能为空，请重新输入".format(err)))
                msg_box.exec_()
                self.text_out("请等待重新输入")
                self.time_period = [None, None]
                DateWindow(self, self.time_period).exec()
            except Exception as err:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText(self.tr("错误:{}".format(err)))
                msg_box.exec_()
                return

        self.text_out("完成")

        self.file_name = file_name
        self.table_name = table_name
        self.spindle_id = spindle_id

        try:

            # 设置程序控件值的范围与当前默认值
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
            self.text_out("请重新设定分组数，并重新打开数据库")
            self.time_period = [None, None]
            self.data = None
        except Exception as err:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText(self.tr("错误:{}".format(err)))
            msg_box.exec_()
            return

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
            self.file_name, self.table_name, self.spindle_id, self.time_period,
            text_out=self.ui.statusBar.showMessage)
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
        self.comp_data = ScrewingDataProcess(
            self.file_name, self.table_name, self.comp_spindle_id, self.time_period,
            text_out=self.ui.statusBar.showMessage)
        self.text_out("完成")
        self.plot_by_time()

    def update_number(self):
        """
        更新显示数字的控件内容
        :return: 
        """
        if self.data is None:
            return
        self.ui.spindle.setText(format(self.spindle_id, '<'))
        self.ui.total_qualification.setText(
            "{:<.2f}%".format(len(self.data.total_normal_data[self.current_start_time:self.current_end_time]) /
                              len(self.data.total_data[self.current_start_time:self.current_end_time]) * 100))
        self.ui.total_production.setText(
            format(len(self.data.total_data[self.current_start_time:self.current_end_time]), '<'))
        self.ui.total_mean.setText(
            format(self.data.total_normal_data[self.current_start_time:self.current_end_time].mean(), '<.2f'))
        self.ui.total_std.setText(
            format(self.data.total_normal_data[self.current_start_time:self.current_end_time].std(), '<.2f'))
        self.ui.current_start_time.setText(str(self.current_start_time))
        self.ui.current_end_time.setText(str(self.current_end_time))
        self.ui.current_start_num.setText(str(self.current_start_num))
        self.ui.current_end_num.setText(str(self.current_end_num))
        self.ui.start_time.setDate(QDate.fromString(str(self.current_start_time.date()), "yyyy-MM-dd"))
        self.ui.end_time.setDate(QDate.fromString(str(self.current_end_time.date()), "yyyy-MM-dd"))
        self.ui.start_num.setValue(self.current_start_num)
        self.ui.end_num.setValue(self.current_end_num)

        self.ui.label_total_start.setText(str(self.data.part_date[0]))
        self.ui.label_total_end.setText(str(self.data.part_date[-1]))
        self.ui.label_total_num.setNum(len(self.data.part_date))

        if self.comp_data is not None:
            self.ui.label_comp_spindle_id.setNum(self.comp_spindle_id)
            self.ui.label_correlation.setNum(self.data.total_normal_data.corr(self.comp_data.total_normal_data))
        else:
            self.ui.label_comp_spindle_id.setText("NaN")
            self.ui.label_correlation.setText("NaN")

    def update_var_by_time(self):
        """
        以时间为标准，改变内部变量的值
        :return: 
        """
        if self.ui.start_time.date() >= self.ui.end_time.date():
            raise ValueError("开始日期请小于结束日期")
        start_time = self.ui.start_time.date().toString("yyyy-MM-dd")
        end_time = self.ui.end_time.date().toString("yyyy-MM-dd")
        self.current_start_time, self.current_end_time, self.current_start_num, self.current_end_num = \
            self.series_between_time(start_time, end_time, self.data.part_date)

    def update_var_by_part(self):
        """
        以组数为标准，改变内部变量的值
        :return: 
        """
        if self.ui.start_num.value() >= self.ui.end_num.value():
            raise ValueError("开始组数请小于结束组数")
        self.current_start_num = self.ui.start_num.value()
        self.current_end_num = self.ui.end_num.value()
        self.current_start_time = self.data.part_date[self.current_start_num]
        self.current_end_time = self.data.part_date[self.current_end_num]

    def clear_torque(self):
        """
        清除扭矩图像
        :return: 
        """
        self.ax_torque_std.clear()
        self.ax_torque_mean.clear()
        self.ax_torque_hist.clear()
        self.figure_canvas_torque.draw()
        self.ui.actionClearTorque.setEnabled(False)

    def clear_all(self):
        """
        清除所有图像
        :return: 
        """
        self.ax_production.clear()
        self.ax_qualification.clear()
        self.figure_canvas_production.draw()
        self.clear_torque()
        self.ui.actionClear_ALL.setEnabled(False)

    def plot_by_time(self):
        """
        以时间为横轴作图
        :return: 
        """
        self.clear_all()
        try:
            self.update_var_by_time()
            self.update_number()
            self.plot_production()
            self.plot_torque_time()
        except ValueError as err:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText(self.tr("错误:{}\n请重新输入".format(err)))
            msg_box.exec_()
        except Exception as err:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText(self.tr("错误:{}".format(err)))
            msg_box.exec_()
            return

    def plot_by_part(self):
        """
        以组数为横轴作图（产量图仍然以时间为横轴）
        :return: 
        """
        self.clear_all()
        try:
            self.update_var_by_part()
            self.update_number()
            self.plot_production()
            self.plot_torque_part()
        except ValueError as err:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText(self.tr("错误:{}\n请重新输入".format(err)))
            msg_box.exec_()
        except Exception as err:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText(self.tr("错误:{}".format(err)))
            msg_box.exec_()
            return

    @staticmethod
    def series_between_time(start_time, end_time, date_list):
        """
        功能静态函数，确定一个时间Series中start_time到end_time之间的最大区间
        :param start_time: 起始时间
        :param end_time: 结束时间
        :param date_list: 在start_time与end_time之间的最大区间的序列起始时间，序列结束时间，序列起始组数，序列结束组数
        :return: 
        """
        start_time = pd.to_datetime(start_time)
        end_time = pd.to_datetime(end_time)
        part_start_time = None
        part_end_time = date_list[-1]
        start_num = None
        end_num = len(date_list) - 1
        for i, date in enumerate(date_list):
            if date > start_time and part_start_time is None:
                part_start_time = date
                start_num = i
            if date > end_time:
                part_end_time = date
                end_num = i
                break
        if part_start_time is None:
            part_start_time = date_list[0]
            start_num = 0
        return part_start_time, part_end_time, start_num, end_num

    def plot_torque_time(self):
        """
        以时间为横轴绘制扭矩图
        :return: 
        """
        self.ax_torque_mean.plot(self.data.part_date[self.current_start_num:self.current_end_num],
                                 self.data.part_mean[self.current_start_num:self.current_end_num],
                                 label="ID {} Mean".format(self.spindle_id))
        if self.comp_data is not None:
            self.ax_torque_mean.plot(self.comp_data.part_date[self.current_start_num:self.current_end_num],
                                     self.comp_data.part_mean[self.current_start_num:self.current_end_num],
                                     label="ID {} Mean".format(self.comp_spindle_id))
        self.ax_torque_mean.legend()
        self.ax_torque_std.plot(self.data.part_date[self.current_start_num:self.current_end_num],
                                self.data.part_std[self.current_start_num:self.current_end_num],
                                label="ID {} std".format(self.spindle_id))
        if self.comp_data is not None:
            self.ax_torque_std.plot(self.comp_data.part_date[self.current_start_num:self.current_end_num],
                                    self.comp_data.part_std[self.current_start_num:self.current_end_num],
                                    label="ID {} Mean".format(self.comp_spindle_id))
        self.ax_torque_std.legend()
        self.ax_torque_hist.hist(self.data.part_mean[self.current_start_num:self.current_end_num],
                                 np.arange(12., 25., 0.2), histtype="stepfilled",
                                 label="ID {} Hist".format(self.spindle_id))
        if self.comp_data is not None:
            self.ax_torque_hist.hist(self.comp_data.part_mean[self.current_start_num:self.current_end_num],
                                     np.arange(12., 25., 0.2), histtype="stepfilled",
                                     label="ID {} Hist".format(self.comp_spindle_id))
        self.ax_torque_std.legend()
        self.figure_canvas_torque.draw()
        self.ui.actionClear_ALL.setEnabled(True)
        self.ui.actionClearTorque.setEnabled(True)

    def plot_torque_part(self):
        """
        以组数为横轴绘制扭矩图
        :return: 
        """
        self.ax_torque_mean.plot(range(self.current_start_num, self.current_end_num),
                                 self.data.part_mean[self.current_start_num:self.current_end_num],
                                 label="ID {} Mean".format(self.spindle_id))
        if self.comp_data is not None:
            self.ax_torque_mean.plot(range(self.current_start_num, self.current_end_num),
                                     self.comp_data.part_mean[self.current_start_num:self.current_end_num],
                                     label="ID {} Mean".format(self.comp_spindle_id))
        self.ax_torque_mean.legend()
        self.ax_torque_std.plot(range(self.current_start_num, self.current_end_num),
                                self.data.part_std[self.current_start_num:self.current_end_num],
                                label="ID {} std".format(self.spindle_id))
        if self.comp_data is not None:
            self.ax_torque_std.plot(range(self.current_start_num, self.current_end_num),
                                    self.comp_data.part_std[self.current_start_num:self.current_end_num],
                                    label="ID {} std".format(self.comp_spindle_id))
        self.ax_torque_std.legend()
        self.ax_torque_hist.hist(self.data.part_mean[self.current_start_num:self.current_end_num],
                                 np.arange(12., 25., 0.2), histtype="stepfilled",
                                 label="ID {} Hist".format(self.spindle_id))
        if self.comp_data is not None:
            self.ax_torque_hist.hist(self.comp_data.part_mean[self.current_start_num:self.current_end_num],
                                     np.arange(12., 25., 0.2), histtype="stepfilled",
                                     label="ID {} Hist".format(self.comp_spindle_id))
        self.ax_torque_std.legend()
        self.figure_canvas_torque.draw()
        self.ui.actionClear_ALL.setEnabled(True)
        self.ui.actionClearTorque.setEnabled(True)

    def plot_production(self):
        """
        绘制产量图
        :return: 
        """
        self.ax_production.plot(self.data.daily_production[self.current_start_time:self.current_end_time],
                                label="Daily Production")
        self.ax_production.legend()
        self.ax_qualification.fill_between(
            self.data.daily_production[self.current_start_time:self.current_end_time].index,
            self.data.daily_qualified_production[self.current_start_time:self.current_end_time] /
            self.data.daily_production[self.current_start_time:self.current_end_time], label="Qualification")
        self.ax_qualification.set_ylim(0.8, 1.0)
        self.ax_qualification.legend()
        self.figure_canvas_production.draw()
        self.ui.actionClear_ALL.setEnabled(True)

    def set_divide_time(self):
        divide, ok = QtWidgets.QInputDialog.getInt(self, self.tr("请输入"),
                                                   self.tr("每组数据中最大间隔时间（分钟）"),
                                                   cf.divide_time, 1, 1440)
        if ok:
            cf.divide_time = divide

    def set_series_num(self):
        series_num, ok = QtWidgets.QInputDialog.getInt(self, self.tr("请输入"),
                                                       self.tr("每组数据量（设置太大可能会导致无分组）"),
                                                       cf.series_num, 10, 100)
        if ok:
            cf.series_num = series_num

    def set_reverse_month(self):
        reverse, ok = QtWidgets.QInputDialog.getInt(self, self.tr("请输入"),
                                                    self.tr("默认回溯月数（在确认数据库读取时间段时，\n"
                                                            "默认的开始日期为当前日期之前的前几个月"),
                                                    cf.reverse_month, 1, 12)
        if ok:
            cf.reverse_month = reverse

    def set_default_latest_num(self):
        num, ok = QtWidgets.QInputDialog.getInt(self, self.tr("请输入"),
                                                    self.tr("默认最新读取数据量（设置读取最新数据时，\n"
                                                            "（每把拧紧枪）需要读取多少行数据"),
                                                    cf.default_latest_num, 100, 1000000)
        if ok:
            cf.default_latest_num = num

    def plot_specgram(self):
        from math import log2
        nfft = 2 << (1 + int(log2(len(self.data.part_mean))))
        plt.close()
        plt.specgram(self.data.part_mean, NFFT=nfft, Fs=cf.series_num, noverlap=10)
        plt.show()

    def plot_fft(self):
        fft = np.fft.rfft(self.data.part_mean)
        plt.close()
        plt.plot(abs(fft))
        plt.ylim(0.0, abs(fft[1]))
        plt.show()


class DateWindow(QtWidgets.QDialog):
    def __init__(self, parent, date_period):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.end_date.setDate(QDate.currentDate())
        self.ui.start_date.setDate(QDate.currentDate().addMonths(-cf.reverse_month))
        self.date_period = date_period

    def accept(self):
        self.date_period[0], self.date_period[1] = self.ui.start_date.date().toString(Qt.ISODate),\
                                                   self.ui.end_date.date().toString(Qt.ISODate)
        super().accept()

