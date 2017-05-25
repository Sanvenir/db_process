#!/usr/bin/python  
# -*- coding: utf-8 -*-

import pypyodbc

from pandas import Series
from db_process.config import Configuration as cf

sentences = None
with open(r"config\sql.txt", "r") as f:
    sentences = f.readlines()
print(sentences)

from PyQt5.QtWidgets import QApplication


class DataBase(object):
    def __init__(self, path, table):
        """
        读取数据库文件
        :param path: 数据库文件绝对路径
        :param table: 数据表名称
        """
        try:
            self.conn = pypyodbc.connect(
                r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
                r"Dbq={};".format(path))
            pypyodbc.lowercase = False
            self.cur = self.conn.cursor()
            self.table = table
        except pypyodbc.Error as err:
            raise err

    def __del__(self):
        self.cur.close()
        self.conn.close()


class ScrewingDataBase(DataBase):
    def __init__(self, path, table):
        """
        读取拧紧枪数据库文件
        :param path: 数据库文件绝对路径
        :param table: 数据表名称
        """
        super().__init__(path, table)

    def fetch_new_all(self, spindle_id):
        """
        获取最新数据
        :param spindle_id:指定拧紧枪号
        :return: 
        """
        self.cur.execute(sentences[0].format(cf.default_latest_num, self.table, spindle_id))
        return Series(dict(self.cur.fetchall()))

    def fetch_new_normal(self, record, spindle_id):
        """
        获取最新数据
        :param record:读取字段名
        :param spindle_id:指定拧紧枪号
        :return: 
        """
        self.cur.execute(sentences[1].format(cf.default_latest_num, record, self.table, spindle_id))
        return Series(dict(self.cur.fetchall()))

    def fetch_normal_record(self, record, spindle_id):
        """
        获取合格数据(ok=-1)的指定字段名数据，并返回Series
        :param record: 读取字段名
        :param spindle_id: 指定拧紧枪号
        :return: Series数据，index为日期，内容为指定字段名的变量
        """
        self.cur.execute(sentences[2].format(record, self.table, spindle_id))
        return Series(dict(self.cur.fetchall()))

    def fetch_all_record(self, spindle_id):
        """
        获取全部数据
        :param spindle_id:指定拧紧枪号 
        :return: Series数据，index为日期，内容为对应的QSCode
        """
        self.cur.execute(sentences[3].format(self.table, spindle_id))
        return Series(dict(self.cur.fetchall()))

    def fetch_date_all(self, spindle_id, start_date, end_date):
        self.cur.execute(sentences[4].format(self.table, spindle_id, start_date, end_date))
        return Series(dict(self.cur.fetchall()))

    def fetch_date_normal(self, record, spindle_id, start_date, end_date):
        self.cur.execute(sentences[5].format(record, self.table, spindle_id, start_date, end_date))
        return Series(dict(self.cur.fetchall()))


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
        self.cur.execute(sentences[6] .format(self.table, start_date, spindle_id))
        self.text_out("开始读取")
        return Series(dict(self.cur.fetchall()))

    def fetch_new_record(self, spindle_id):
        self.text_out("开始查询")
        self.cur.execute(sentences[7].format(cf.default_latest_num, self.table, spindle_id))
        self.text_out("开始读取")
        return Series(dict(self.cur.fetchall()))


class CompDataBase(DataBase):
    def __init__(self, path, table, text_out=print):
        """
        读取拧紧枪数据库文件
        :param path: 数据库文件绝对路径
        :param table: 数据表名称
        """
        super().__init__(path, table)
        self.text_out = text_out

    def fetch_record(self, spindle_id, data):
        """
        获取数据库数据
        :param spindle_id: 所需获取的拧紧枪号集合, 如果为None则读取全部数据
        :param data: 将数据存入该字典中，关键字为拧紧枪号，内容为每个拧紧枪的SingleDataProcess
        :return: 选取数据的开始时间与结束时间
        """
        self.cur.execute(sentences[8].format(self.table, cf.default_latest_num * 22))
        self.text_out("读取数据中……")
        row = self.cur.fetchone()
        if row is None:
            raise IndexError("没有数据")
        end_date = row[1]
        start_date = None
        count = 500
        while row is not None:
            if spindle_id is not None and row[0] not in spindle_id:
                row = self.cur.fetchone()
                continue
            start_date = row[1]
            count -= 1
            if not count:
                self.text_out("读取数据{}".format(row[1]))
                count = 2000
            if row[3] == 1:
                data[row[0]].total_normal_data[start_date] = row[2]
            data[row[0]].total_data[start_date] = row[3]
            row = self.cur.fetchone()
        for key in data.keys():
            self.text_out("序列化{}号拧紧枪数据……".format(key))
            data[key].serieslize()

        self.text_out("完成")
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
        self.cur.execute(sentences[9].format(self.table, start_date, end_date))
        print("读取数据中……")
        row = self.cur.fetchone()
        if row is None:
            raise IndexError("选定范围内没有数据")
        start_date = row[1]
        while row is not None:
            if row[0] not in spindle_id:
                row = self.cur.fetchone()
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
