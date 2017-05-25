# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 681)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(False)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.figure = QtWidgets.QTabWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.figure.sizePolicy().hasHeightForWidth())
        self.figure.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.figure.setFont(font)
        self.figure.setObjectName("figure")
        self.figure_production = QtWidgets.QWidget()
        self.figure_production.setObjectName("figure_production")
        self.figure.addTab(self.figure_production, "")
        self.figure_torque = QtWidgets.QWidget()
        self.figure_torque.setObjectName("figure_torque")
        self.figure.addTab(self.figure_torque, "")
        self.horizontalLayout.addWidget(self.figure)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.label_spindle = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_spindle.sizePolicy().hasHeightForWidth())
        self.label_spindle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_spindle.setFont(font)
        self.label_spindle.setObjectName("label_spindle")
        self.verticalLayout_4.addWidget(self.label_spindle)
        self.line_9 = QtWidgets.QFrame(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.line_9.setFont(font)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_4.addWidget(self.line_9)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.line_5 = QtWidgets.QFrame(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.line_5.setFont(font)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_4.addWidget(self.line_5)
        self.label_total_production = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_total_production.setFont(font)
        self.label_total_production.setObjectName("label_total_production")
        self.verticalLayout_4.addWidget(self.label_total_production)
        self.label_total_qualification = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_total_qualification.setFont(font)
        self.label_total_qualification.setObjectName("label_total_qualification")
        self.verticalLayout_4.addWidget(self.label_total_qualification)
        self.label_total_mean = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_total_mean.setFont(font)
        self.label_total_mean.setObjectName("label_total_mean")
        self.verticalLayout_4.addWidget(self.label_total_mean)
        self.label_total_std = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_total_std.setFont(font)
        self.label_total_std.setObjectName("label_total_std")
        self.verticalLayout_4.addWidget(self.label_total_std)
        self.line_7 = QtWidgets.QFrame(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.line_7.setFont(font)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_4.addWidget(self.line_7)
        self.label = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.spindle = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.spindle.setFont(font)
        self.spindle.setObjectName("spindle")
        self.verticalLayout_5.addWidget(self.spindle)
        self.line_10 = QtWidgets.QFrame(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.line_10.setFont(font)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_5.addWidget(self.line_10)
        self.label_total_start = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_total_start.setFont(font)
        self.label_total_start.setObjectName("label_total_start")
        self.verticalLayout_5.addWidget(self.label_total_start)
        self.label_total_end = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_total_end.setFont(font)
        self.label_total_end.setObjectName("label_total_end")
        self.verticalLayout_5.addWidget(self.label_total_end)
        self.label_total_num = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_total_num.setFont(font)
        self.label_total_num.setObjectName("label_total_num")
        self.verticalLayout_5.addWidget(self.label_total_num)
        self.line_6 = QtWidgets.QFrame(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.line_6.setFont(font)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_5.addWidget(self.line_6)
        self.total_production = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.total_production.setFont(font)
        self.total_production.setObjectName("total_production")
        self.verticalLayout_5.addWidget(self.total_production)
        self.total_qualification = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.total_qualification.setFont(font)
        self.total_qualification.setObjectName("total_qualification")
        self.verticalLayout_5.addWidget(self.total_qualification)
        self.total_mean = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.total_mean.setFont(font)
        self.total_mean.setObjectName("total_mean")
        self.verticalLayout_5.addWidget(self.total_mean)
        self.total_std = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.total_std.setFont(font)
        self.total_std.setObjectName("total_std")
        self.verticalLayout_5.addWidget(self.total_std)
        self.line_8 = QtWidgets.QFrame(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.line_8.setFont(font)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_5.addWidget(self.line_8)
        self.label_comp_spindle_id = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_comp_spindle_id.setFont(font)
        self.label_comp_spindle_id.setObjectName("label_comp_spindle_id")
        self.verticalLayout_5.addWidget(self.label_comp_spindle_id)
        self.label_correlation = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_correlation.setFont(font)
        self.label_correlation.setObjectName("label_correlation")
        self.verticalLayout_5.addWidget(self.label_correlation)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_current_start_time = QtWidgets.QLabel(self.tabWidgetPage1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_current_start_time.setFont(font)
        self.label_current_start_time.setObjectName("label_current_start_time")
        self.verticalLayout_2.addWidget(self.label_current_start_time)
        self.current_start_time = QtWidgets.QLabel(self.tabWidgetPage1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.current_start_time.setFont(font)
        self.current_start_time.setObjectName("current_start_time")
        self.verticalLayout_2.addWidget(self.current_start_time)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_current_end_time = QtWidgets.QLabel(self.tabWidgetPage1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_current_end_time.setFont(font)
        self.label_current_end_time.setObjectName("label_current_end_time")
        self.verticalLayout_2.addWidget(self.label_current_end_time)
        self.current_end_time = QtWidgets.QLabel(self.tabWidgetPage1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.current_end_time.setFont(font)
        self.current_end_time.setObjectName("current_end_time")
        self.verticalLayout_2.addWidget(self.current_end_time)
        self.button_detial_time = QtWidgets.QPushButton(self.tabWidgetPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_detial_time.sizePolicy().hasHeightForWidth())
        self.button_detial_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.button_detial_time.setFont(font)
        self.button_detial_time.setObjectName("button_detial_time")
        self.verticalLayout_2.addWidget(self.button_detial_time)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.line_4 = QtWidgets.QFrame(self.tabWidgetPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.line_4.setFont(font)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_start_time = QtWidgets.QLabel(self.tabWidgetPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_start_time.sizePolicy().hasHeightForWidth())
        self.label_start_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_start_time.setFont(font)
        self.label_start_time.setObjectName("label_start_time")
        self.verticalLayout_2.addWidget(self.label_start_time)
        self.start_time = QtWidgets.QDateEdit(self.tabWidgetPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_time.sizePolicy().hasHeightForWidth())
        self.start_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.start_time.setFont(font)
        self.start_time.setCalendarPopup(True)
        self.start_time.setObjectName("start_time")
        self.verticalLayout_2.addWidget(self.start_time)
        self.label_end_time = QtWidgets.QLabel(self.tabWidgetPage1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_end_time.setFont(font)
        self.label_end_time.setObjectName("label_end_time")
        self.verticalLayout_2.addWidget(self.label_end_time)
        self.end_time = QtWidgets.QDateEdit(self.tabWidgetPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_time.sizePolicy().hasHeightForWidth())
        self.end_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.end_time.setFont(font)
        self.end_time.setCalendarPopup(True)
        self.end_time.setObjectName("end_time")
        self.verticalLayout_2.addWidget(self.end_time)
        self.button_time = QtWidgets.QPushButton(self.tabWidgetPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_time.sizePolicy().hasHeightForWidth())
        self.button_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.button_time.setFont(font)
        self.button_time.setObjectName("button_time")
        self.verticalLayout_2.addWidget(self.button_time)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_current_start_num = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_current_start_num.setObjectName("label_current_start_num")
        self.verticalLayout_3.addWidget(self.label_current_start_num)
        self.current_start_num = QtWidgets.QLabel(self.tabWidgetPage2)
        self.current_start_num.setObjectName("current_start_num")
        self.verticalLayout_3.addWidget(self.current_start_num)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem5)
        self.label_current_end_num = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_current_end_num.setObjectName("label_current_end_num")
        self.verticalLayout_3.addWidget(self.label_current_end_num)
        self.current_end_num = QtWidgets.QLabel(self.tabWidgetPage2)
        self.current_end_num.setObjectName("current_end_num")
        self.verticalLayout_3.addWidget(self.current_end_num)
        self.button_detial_num = QtWidgets.QPushButton(self.tabWidgetPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_detial_num.sizePolicy().hasHeightForWidth())
        self.button_detial_num.setSizePolicy(sizePolicy)
        self.button_detial_num.setObjectName("button_detial_num")
        self.verticalLayout_3.addWidget(self.button_detial_num)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.line_3 = QtWidgets.QFrame(self.tabWidgetPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.label_start_num = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_start_num.setObjectName("label_start_num")
        self.verticalLayout_3.addWidget(self.label_start_num)
        self.start_num = QtWidgets.QSpinBox(self.tabWidgetPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_num.sizePolicy().hasHeightForWidth())
        self.start_num.setSizePolicy(sizePolicy)
        self.start_num.setObjectName("start_num")
        self.verticalLayout_3.addWidget(self.start_num)
        self.label_end_num = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_end_num.setObjectName("label_end_num")
        self.verticalLayout_3.addWidget(self.label_end_num)
        self.end_num = QtWidgets.QSpinBox(self.tabWidgetPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_num.sizePolicy().hasHeightForWidth())
        self.end_num.setSizePolicy(sizePolicy)
        self.end_num.setObjectName("end_num")
        self.verticalLayout_3.addWidget(self.end_num)
        self.button_num = QtWidgets.QPushButton(self.tabWidgetPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_num.sizePolicy().hasHeightForWidth())
        self.button_num.setSizePolicy(sizePolicy)
        self.button_num.setObjectName("button_num")
        self.verticalLayout_3.addWidget(self.button_num)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout.setStretch(0, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 610, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBar.sizePolicy().hasHeightForWidth())
        self.menuBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuFile.sizePolicy().hasHeightForWidth())
        self.menuFile.setSizePolicy(sizePolicy)
        self.menuFile.setObjectName("menuFile")
        self.menuPlot = QtWidgets.QMenu(self.menuBar)
        self.menuPlot.setObjectName("menuPlot")
        self.menuspc_figure = QtWidgets.QMenu(self.menuPlot)
        self.menuspc_figure.setEnabled(False)
        self.menuspc_figure.setObjectName("menuspc_figure")
        self.menuPlotFrequence = QtWidgets.QMenu(self.menuPlot)
        self.menuPlotFrequence.setEnabled(False)
        self.menuPlotFrequence.setObjectName("menuPlotFrequence")
        self.menuSetting = QtWidgets.QMenu(self.menuBar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuChangeVarities = QtWidgets.QMenu(self.menuSetting)
        self.menuChangeVarities.setObjectName("menuChangeVarities")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionChange_Spindle_ID = QtWidgets.QAction(MainWindow)
        self.actionChange_Spindle_ID.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionChange_Spindle_ID.setFont(font)
        self.actionChange_Spindle_ID.setObjectName("actionChange_Spindle_ID")
        self.actionClear_ALL = QtWidgets.QAction(MainWindow)
        self.actionClear_ALL.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionClear_ALL.setFont(font)
        self.actionClear_ALL.setObjectName("actionClear_ALL")
        self.actionClearTorque = QtWidgets.QAction(MainWindow)
        self.actionClearTorque.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionClearTorque.setFont(font)
        self.actionClearTorque.setObjectName("actionClearTorque")
        self.actionspc_xr = QtWidgets.QAction(MainWindow)
        self.actionspc_xr.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionspc_xr.setFont(font)
        self.actionspc_xr.setObjectName("actionspc_xr")
        self.actionAddSpindle = QtWidgets.QAction(MainWindow)
        self.actionAddSpindle.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionAddSpindle.setFont(font)
        self.actionAddSpindle.setObjectName("actionAddSpindle")
        self.actionPartNum = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionPartNum.setFont(font)
        self.actionPartNum.setObjectName("actionPartNum")
        self.actionDefaultReadTime = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionDefaultReadTime.setFont(font)
        self.actionDefaultReadTime.setObjectName("actionDefaultReadTime")
        self.actionReverseTime = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionReverseTime.setFont(font)
        self.actionReverseTime.setObjectName("actionReverseTime")
        self.actionPlotSpecgram = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionPlotSpecgram.setFont(font)
        self.actionPlotSpecgram.setObjectName("actionPlotSpecgram")
        self.actionPlotFFT = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionPlotFFT.setFont(font)
        self.actionPlotFFT.setObjectName("actionPlotFFT")
        self.actionOpenComp = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionOpenComp.setFont(font)
        self.actionOpenComp.setObjectName("actionOpenComp")
        self.actionDefaultLatestNum = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionDefaultLatestNum.setFont(font)
        self.actionDefaultLatestNum.setObjectName("actionDefaultLatestNum")
        self.actionSpindleFatigue = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        self.actionSpindleFatigue.setFont(font)
        self.actionSpindleFatigue.setObjectName("actionSpindleFatigue")
        self.actionOpenMonitor = QtWidgets.QAction(MainWindow)
        self.actionOpenMonitor.setCheckable(True)
        self.actionOpenMonitor.setObjectName("actionOpenMonitor")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpenComp)
        self.menuFile.addAction(self.actionSpindleFatigue)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuspc_figure.addAction(self.actionspc_xr)
        self.menuPlotFrequence.addAction(self.actionPlotSpecgram)
        self.menuPlotFrequence.addAction(self.actionPlotFFT)
        self.menuPlot.addAction(self.actionClearTorque)
        self.menuPlot.addAction(self.actionClear_ALL)
        self.menuPlot.addSeparator()
        self.menuPlot.addAction(self.menuspc_figure.menuAction())
        self.menuPlot.addAction(self.menuPlotFrequence.menuAction())
        self.menuChangeVarities.addSeparator()
        self.menuChangeVarities.addAction(self.actionPartNum)
        self.menuChangeVarities.addAction(self.actionDefaultLatestNum)
        self.menuChangeVarities.addAction(self.actionReverseTime)
        self.menuChangeVarities.addAction(self.actionDefaultReadTime)
        self.menuSetting.addAction(self.actionChange_Spindle_ID)
        self.menuSetting.addAction(self.actionAddSpindle)
        self.menuSetting.addAction(self.menuChangeVarities.menuAction())
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPlot.menuAction())
        self.menuBar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        self.figure.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.start_num, self.end_time)
        MainWindow.setTabOrder(self.end_time, self.figure)
        MainWindow.setTabOrder(self.figure, self.end_num)
        MainWindow.setTabOrder(self.end_num, self.start_time)
        MainWindow.setTabOrder(self.start_time, self.button_time)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "拧紧枪数据库处理"))
        self.figure.setTabText(self.figure.indexOf(self.figure_production), _translate("MainWindow", "生产统计数据"))
        self.figure.setTabText(self.figure.indexOf(self.figure_torque), _translate("MainWindow", "扭矩统计数据"))
        self.label_spindle.setText(_translate("MainWindow", "拧紧枪编号"))
        self.label_5.setText(_translate("MainWindow", "数据开始时间"))
        self.label_6.setText(_translate("MainWindow", "数据结束时间"))
        self.label_7.setText(_translate("MainWindow", "数据总数"))
        self.label_total_production.setText(_translate("MainWindow", "生产量"))
        self.label_total_qualification.setText(_translate("MainWindow", "合格率"))
        self.label_total_mean.setText(_translate("MainWindow", "扭矩均值"))
        self.label_total_std.setText(_translate("MainWindow", "扭矩标准差"))
        self.label.setText(_translate("MainWindow", "对比拧紧枪编号"))
        self.label_3.setText(_translate("MainWindow", "相关度"))
        self.spindle.setText(_translate("MainWindow", "NaN"))
        self.label_total_start.setText(_translate("MainWindow", "NaN"))
        self.label_total_end.setText(_translate("MainWindow", "NaN "))
        self.label_total_num.setText(_translate("MainWindow", "NaN"))
        self.total_production.setText(_translate("MainWindow", "NaN"))
        self.total_qualification.setText(_translate("MainWindow", "NaN"))
        self.total_mean.setText(_translate("MainWindow", "NaN"))
        self.total_std.setText(_translate("MainWindow", "NaN"))
        self.label_comp_spindle_id.setText(_translate("MainWindow", "NaN"))
        self.label_correlation.setText(_translate("MainWindow", "NaN"))
        self.label_current_start_time.setText(_translate("MainWindow", "当前开始时间"))
        self.current_start_time.setText(_translate("MainWindow", "NaT"))
        self.label_current_end_time.setText(_translate("MainWindow", "当前结束时间"))
        self.current_end_time.setText(_translate("MainWindow", "NaT"))
        self.button_detial_time.setText(_translate("MainWindow", "显示详细图像"))
        self.label_start_time.setText(_translate("MainWindow", "开始时间"))
        self.label_end_time.setText(_translate("MainWindow", "结束时间"))
        self.button_time.setText(_translate("MainWindow", "刷新图像"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "时间分割"))
        self.label_current_start_num.setText(_translate("MainWindow", "当前开始组号"))
        self.current_start_num.setText(_translate("MainWindow", "NaT"))
        self.label_current_end_num.setText(_translate("MainWindow", "当前结束组号"))
        self.current_end_num.setText(_translate("MainWindow", "NaT"))
        self.button_detial_num.setText(_translate("MainWindow", "显示详细图像"))
        self.label_start_num.setText(_translate("MainWindow", "区域绘图开始组数"))
        self.label_end_num.setText(_translate("MainWindow", "区域绘图结束组数"))
        self.button_num.setText(_translate("MainWindow", "刷新图像"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "组号分割"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.menuPlot.setTitle(_translate("MainWindow", "图像"))
        self.menuspc_figure.setTitle(_translate("MainWindow", "绘制SPC图"))
        self.menuPlotFrequence.setTitle(_translate("MainWindow", "频域分析"))
        self.menuSetting.setTitle(_translate("MainWindow", "设置"))
        self.menuChangeVarities.setTitle(_translate("MainWindow", "调整变量"))
        self.actionOpen.setText(_translate("MainWindow", "打开数据库"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionChange_Spindle_ID.setText(_translate("MainWindow", "设置拧紧枪ID"))
        self.actionClear_ALL.setText(_translate("MainWindow", "清除所有图像"))
        self.actionClearTorque.setText(_translate("MainWindow", "清除扭矩图像"))
        self.actionspc_xr.setText(_translate("MainWindow", "SPC XR"))
        self.actionAddSpindle.setText(_translate("MainWindow", "设置对比拧紧枪"))
        self.actionPartNum.setText(_translate("MainWindow", "分组数目"))
        self.actionDefaultReadTime.setText(_translate("MainWindow", "中断时间"))
        self.actionReverseTime.setText(_translate("MainWindow", "默认回溯月数"))
        self.actionPlotSpecgram.setText(_translate("MainWindow", "Specgram"))
        self.actionPlotFFT.setText(_translate("MainWindow", "FFT"))
        self.actionOpenComp.setText(_translate("MainWindow", "拧紧枪对比"))
        self.actionDefaultLatestNum.setText(_translate("MainWindow", "默认读取最新数据量"))
        self.actionSpindleFatigue.setText(_translate("MainWindow", "疲劳监控"))
        self.actionOpenMonitor.setText(_translate("MainWindow", "实时监控模式"))

