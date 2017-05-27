#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MyFigureCanvas(FigureCanvas):
    def __init__(self, *args):
        super().__init__(*args)
        self.mouse_double_click_func = None

    def set_mouse_double_click(self, func):
        self.mouse_double_click_func = func

    def mouseDoubleClickEvent(self, event):
        super().mouseDoubleClickEvent(event)
        if self.mouse_double_click_func:
            self.mouse_double_click_func()
