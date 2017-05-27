#!/usr/bin/python  
# -*- coding: utf-8 -*-


class Configuration(object):
    divide_time = 5
    series_num = 50
    reverse_month = 1
    default_latest_num = 5000
    qs_count = {12: 0, 16: 0}
    qs_result = {12: "摩擦系数大，零件强度高，转速过快过冲",
                 16: "摩擦系数小，零件强度低，AW方式匹配差，"
                 "油、蜡、胶水存在于螺纹面或支撑面，零件间隙：焊接间隙、匹配间隙"}
