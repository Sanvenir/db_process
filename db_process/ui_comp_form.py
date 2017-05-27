# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/comp_form.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonByTime = QtWidgets.QRadioButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonByTime.sizePolicy().hasHeightForWidth())
        self.radioButtonByTime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.radioButtonByTime.setFont(font)
        self.radioButtonByTime.setChecked(True)
        self.radioButtonByTime.setObjectName("radioButtonByTime")
        self.verticalLayout.addWidget(self.radioButtonByTime)
        self.radioButtonByCount = QtWidgets.QRadioButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonByCount.sizePolicy().hasHeightForWidth())
        self.radioButtonByCount.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.radioButtonByCount.setFont(font)
        self.radioButtonByCount.setObjectName("radioButtonByCount")
        self.verticalLayout.addWidget(self.radioButtonByCount)
        self.line = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.groupBoxQualification = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.groupBoxQualification.setFont(font)
        self.groupBoxQualification.setObjectName("groupBoxQualification")
        self.verticalLayout.addWidget(self.groupBoxQualification)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_torque_var = QtWidgets.QWidget()
        self.tab_torque_var.setObjectName("tab_torque_var")
        self.tabWidget.addTab(self.tab_torque_var, "")
        self.tab_torque_dis = QtWidgets.QWidget()
        self.tab_torque_dis.setObjectName("tab_torque_dis")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_torque_dis)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBoxSpindleID = QtWidgets.QGroupBox(self.tab_torque_dis)
        self.groupBoxSpindleID.setObjectName("groupBoxSpindleID")
        self.horizontalLayout_2.addWidget(self.groupBoxSpindleID)
        self.groupBoxMean = QtWidgets.QGroupBox(self.tab_torque_dis)
        self.groupBoxMean.setObjectName("groupBoxMean")
        self.horizontalLayout_2.addWidget(self.groupBoxMean)
        self.groupBoxStd = QtWidgets.QGroupBox(self.tab_torque_dis)
        self.groupBoxStd.setObjectName("groupBoxStd")
        self.horizontalLayout_2.addWidget(self.groupBoxStd)
        self.groupBoxKurt = QtWidgets.QGroupBox(self.tab_torque_dis)
        self.groupBoxKurt.setObjectName("groupBoxKurt")
        self.horizontalLayout_2.addWidget(self.groupBoxKurt)
        self.groupBoxSkew = QtWidgets.QGroupBox(self.tab_torque_dis)
        self.groupBoxSkew.setObjectName("groupBoxSkew")
        self.horizontalLayout_2.addWidget(self.groupBoxSkew)
        self.tabWidget.addTab(self.tab_torque_dis, "")
        self.tab_qs_static = QtWidgets.QWidget()
        self.tab_qs_static.setObjectName("tab_qs_static")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_qs_static)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBoxQSButton = QtWidgets.QGroupBox(self.tab_qs_static)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxQSButton.sizePolicy().hasHeightForWidth())
        self.groupBoxQSButton.setSizePolicy(sizePolicy)
        self.groupBoxQSButton.setObjectName("groupBoxQSButton")
        self.horizontalLayout_5.addWidget(self.groupBoxQSButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayoutStaticFigure = QtWidgets.QVBoxLayout()
        self.verticalLayoutStaticFigure.setObjectName("verticalLayoutStaticFigure")
        self.horizontalLayout_4.addLayout(self.verticalLayoutStaticFigure)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.tab_qs_static)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.textBrowserStatic = QtWidgets.QTextBrowser(self.tab_qs_static)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowserStatic.sizePolicy().hasHeightForWidth())
        self.textBrowserStatic.setSizePolicy(sizePolicy)
        self.textBrowserStatic.setObjectName("textBrowserStatic")
        self.horizontalLayout_3.addWidget(self.textBrowserStatic)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_qs_static, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButtonByTime.setText(_translate("Form", "按时间绘图"))
        self.radioButtonByCount.setText(_translate("Form", "按序号绘图"))
        self.groupBoxQualification.setTitle(_translate("Form", "合格率"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_torque_var), _translate("Form", "扭矩变化"))
        self.groupBoxSpindleID.setTitle(_translate("Form", "拧紧枪号"))
        self.groupBoxMean.setTitle(_translate("Form", "均值"))
        self.groupBoxStd.setTitle(_translate("Form", "标准差"))
        self.groupBoxKurt.setTitle(_translate("Form", "峰度"))
        self.groupBoxSkew.setTitle(_translate("Form", "偏度"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_torque_dis), _translate("Form", "扭矩分布"))
        self.groupBoxQSButton.setTitle(_translate("Form", "拧紧枪故障统计图"))
        self.label.setText(_translate("Form", "当前状态"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_qs_static), _translate("Form", "故障统计"))

