# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Fri Dec 20 12:28:12 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/images/bee_temp_grey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn = QtWidgets.QPushButton(self.centralwidget)
        self.home_btn.setObjectName("home_btn")
        self.verticalLayout.addWidget(self.home_btn)
        self.market_btn = QtWidgets.QPushButton(self.centralwidget)
        self.market_btn.setObjectName("market_btn")
        self.verticalLayout.addWidget(self.market_btn)
        self.kline_btn = QtWidgets.QPushButton(self.centralwidget)
        self.kline_btn.setObjectName("kline_btn")
        self.verticalLayout.addWidget(self.kline_btn)
        self.strategy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.strategy_btn.setObjectName("strategy_btn")
        self.verticalLayout.addWidget(self.strategy_btn)
        self.backtrack_btn = QtWidgets.QPushButton(self.centralwidget)
        self.backtrack_btn.setObjectName("backtrack_btn")
        self.verticalLayout.addWidget(self.backtrack_btn)
        self.order_btn = QtWidgets.QPushButton(self.centralwidget)
        self.order_btn.setObjectName("order_btn")
        self.verticalLayout.addWidget(self.order_btn)
        self.setting_btn = QtWidgets.QPushButton(self.centralwidget)
        self.setting_btn.setObjectName("setting_btn")
        self.verticalLayout.addWidget(self.setting_btn)
        self.log_btn = QtWidgets.QPushButton(self.centralwidget)
        self.log_btn.setObjectName("log_btn")
        self.verticalLayout.addWidget(self.log_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pre_page_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pre_page_btn.setObjectName("pre_page_btn")
        self.verticalLayout.addWidget(self.pre_page_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_2.setStretch(2, 9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1016, 26))
        self.menuBar.setObjectName("menuBar")
        self.menux = QtWidgets.QMenu(self.menuBar)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menu/icon/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menux.setIcon(icon1)
        self.menux.setObjectName("menux")
        MainWindow.setMenuBar(self.menuBar)
        self.quit_action = QtWidgets.QAction(MainWindow)
        self.quit_action.setObjectName("quit_action")
        self.menux.addAction(self.quit_action)
        self.menuBar.addAction(self.menux.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.home_btn.setText(QtWidgets.QApplication.translate("MainWindow", "首页", None, -1))
        self.market_btn.setText(QtWidgets.QApplication.translate("MainWindow", "行情", None, -1))
        self.kline_btn.setText(QtWidgets.QApplication.translate("MainWindow", "K线", None, -1))
        self.strategy_btn.setText(QtWidgets.QApplication.translate("MainWindow", "策略", None, -1))
        self.backtrack_btn.setText(QtWidgets.QApplication.translate("MainWindow", "回测", None, -1))
        self.order_btn.setText(QtWidgets.QApplication.translate("MainWindow", "下单", None, -1))
        self.setting_btn.setText(QtWidgets.QApplication.translate("MainWindow", "设置", None, -1))
        self.log_btn.setText(QtWidgets.QApplication.translate("MainWindow", "日志", None, -1))
        self.pre_page_btn.setText(QtWidgets.QApplication.translate("MainWindow", "←", None, -1))
        self.quit_action.setText(QtWidgets.QApplication.translate("MainWindow", "退出应用", None, -1))

import app.resource.mainwindow_rc
