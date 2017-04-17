#!/usr/bin/python  
# -*- coding: utf-8 -*-

import pypyodbc

from pandas import Series


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

    def fetch_normal_record(self, record, spindle_id):
        """
        获取合格数据(ok=-1)的指定字段名数据，并返回Series
        :param record: 读取字段名
        :param spindle_id: 指定拧紧枪号
        :return: Series数据，index为日期，内容为指定字段名的变量
        """
        self.cur.execute("""
        SELECT Date, {}
        From {}
        WHERE OK=-1 AND SpindleID={}""".format(record, self.table, spindle_id))
        return Series(dict(self.cur.fetchall()))

    def fetch_all_record(self, spindle_id):
        """
        获取全部数据
        :param spindle_id:指定拧紧枪号 
        :return: Series数据，index为日期，内容为对应的QSCode
        """
        self.cur.execute("""
        SELECT Date, QSCode
        From {}
        WHERE SpindleID={}""".format(self.table, spindle_id))
        return Series(dict(self.cur.fetchall()))


if __name__ == "__main__":
    path = input("将数据库文件拖曳至此：").strip('"')
    table = input("数据表名称：")
    while True:
        spindle_id = input("拧紧枪id(1-22)：")
        data = ScrewingDataBase(path, table)
        total_data = data.fetch_all_record(spindle_id)
        for i, ele in enumerate(total_data):
            if ele == 16 and 0 < i < len(total_data) - 1:
                print("{} 下一工件生产时间距离：{}".format(total_data.index[i], total_data.index[i + 1] - total_data.index[i]))
