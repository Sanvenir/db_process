#!/usr/bin/python  
# -*- coding: utf-8 -*-  
from pandas import Series
from numpy import timedelta64 as td

from db_process.database_mssql import ScrewingDataBase

from db_process.config import Configuration as cf


class ScrewingDataProcess(object):
    def __init__(self, spindle_id, data_period=None, text_out=print, fetch_new_data=True):
        """
        获取数据库中的全部数据和全部合格数据，并生成相应的处理序列
        :param spindle_id: 查询的拧紧枪号
        :param data_period: 读取时间段
        :param text_out: 输出状态的函数，默认为print，期望是窗口statusBar的setText函数
        :param convert: 值为真时，转换db_file, db_table属性，db_file变为已存在的total_data序列，db_table变为已存在的
            total_normal_data序列
        :return: 数据时间段
        """
        self.text_out = text_out
        db = ScrewingDataBase()
        from datetime import timedelta
        self.text_out("正在获取{}号拧紧枪所有数据".format(spindle_id))
        # 全部数据，内容为QSCode，index为日期
        total_data = db.fetch_new_all(spindle_id)
        self.total_data = total_data[total_data.first_valid_index().date() + timedelta(1):]

        self.text_out("正在获取{}号拧紧枪合格数据".format(spindle_id))
        # 正常数据，内容为扭矩值，index为日期
        total_normal_data = db.fetch_new_normal('TorqueAct', spindle_id)
        self.total_normal_data = total_normal_data[total_data.first_valid_index().date() + timedelta(1):]

        if self.total_normal_data.empty:
            raise AttributeError("该表或该数据段内没有正常数据")

        # 将全部正常数据以SERIES_NUM为一组划分为多组，同时保证每一组内的点都是连续生产的
        self.part_series = self._dividing_total_data()

        self.text_out("生成处理数列")

        # 获取每日产量数据
        self.daily_production = self.total_data.resample('D').apply(self._count_function)
        # 获取每日合格产量数据
        self.daily_qualified_production = self.total_normal_data.resample('D').apply(self._count_function)

        # 获取分组数据中每一组的开始日期
        self.part_date = [part.first_valid_index() for part in self.part_series]
        # 获取分组数据中每一组的平均值
        self.part_mean = [part.mean() for part in self.part_series]
        # 获取分组数据中每一组的标准差
        self.part_std = [part.std() for part in self.part_series]

    @staticmethod
    def _count_function(array_like):
        if len(array_like):
            return len(array_like)

    def _dividing_total_data(self):
        """
        分组函数，仅限内部一次使用
        :return: 分组列表
        """
        tmp1 = tmp2 = self.total_normal_data.index[0]
        time_parts = []
        part_series = []

        self.text_out("正在生成处理数列")

        # 将全部数据中分组为连续生产(生产间隔不大于DIVIDE_TIME)的若干大组
        for date in self.total_normal_data.index:
            if date - tmp1 > td(cf.divide_time, 'm'):
                time_parts.append(self.total_normal_data[tmp2:date])
                tmp2 = date
            tmp1 = date

        # 将每一大组中每SERIES_NUM的数据分为小组，将所有大组的每一小组添加到返回列表之中
        for data_series in time_parts:
            start_num, end_num = 0, cf.series_num
            while end_num < len(data_series):
                part_series.append(Series(data_series[start_num:end_num]))
                start_num = end_num
                end_num += cf.series_num

        return part_series

