#!/usr/bin/python  
# -*- coding: utf-8 -*-

import pymssql

from pandas import Series
from db_process.config import Configuration as cf

sentences = None
with open(r"config\mssql.txt", "r") as f:
    sentences = f.readlines()

login = None
with open(r"config\login.txt", "r") as f:
    login = f.readlines()


class DataBase(object):
    def __init__(self):
        """
        读取数据库文件
        """
        try:
            self.conn = pymssql.connect(server=login[0], user=login[1], password=login[2], database=login[3])
            self.cur = self.conn.cursor()
        except pymssql.Error as err:
            raise err

    def __del__(self):
        self.cur.close()
        self.conn.close()


class ScrewingDataBase(DataBase):
    def __init__(self):
        """
        读取拧紧枪数据库文件
        :param path: 数据库文件绝对路径
        :param table: 数据表名称
        """
        super().__init__()

    def fetch_new_all(self, spindle_id):
        """
        获取最新数据
        :param spindle_id:指定拧紧枪号
        :return: 
        """
        self.cur.execute(sentences[0].format(cf.default_latest_num, spindle_id))
        return Series(dict(self.cur.fetchall()))

    def fetch_new_normal(self, record, spindle_id):
        """
        获取最新数据
        :param record:读取字段名
        :param spindle_id:指定拧紧枪号
        :return: 
        """
        self.cur.execute(sentences[1].format(cf.default_latest_num, record, spindle_id))
        return Series(dict(self.cur.fetchall()))


class FatigueDataBase(DataBase):
    def __init__(self, text_out=print):
        """
        读取拧紧枪数据库文件
        """
        super().__init__()
        self.text_out = text_out

    def fetch_new_record(self, spindle_id):
        self.text_out("开始查询")
        self.cur.execute(sentences[7].format(cf.default_latest_num, spindle_id))
        self.text_out("开始读取")
        return Series(dict(self.cur.fetchall()))


class CompDataBase(DataBase):
    def __init__(self, text_out=print):
        """
        读取拧紧枪数据库文件
        """
        super().__init__()
        self.text_out = text_out

    def fetch_record(self, spindle_id, data):
        """
        获取数据库数据
        :param spindle_id: 所需获取的拧紧枪号集合, 如果为None则读取全部数据
        :param data: 将数据存入该字典中，关键字为拧紧枪号，内容为每个拧紧枪的SingleDataProcess
        :return: 选取数据的开始时间与结束时间
        """
        self.cur.execute(sentences[8].format(cf.default_latest_num * 22))
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
