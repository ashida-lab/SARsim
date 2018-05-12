# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SARsim_param.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_param(object):
    def setupUi(self, param):
        param.setObjectName("param")
        param.resize(262, 410)
        param.setWindowOpacity(0.95)
        self.textBrowser = QtWidgets.QTextBrowser(param)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 241, 331))
        self.textBrowser.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textBrowser.setSource(QtCore.QUrl("param.txt"))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(param)
        self.label_2.setGeometry(QtCore.QRect(10, 8, 241, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("top.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(param)
        self.label_3.setGeometry(QtCore.QRect(10, 372, 241, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("bottom.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(param)
        QtCore.QMetaObject.connectSlotsByName(param)

    def retranslateUi(self, param):
        _translate = QtCore.QCoreApplication.translate
        param.setWindowTitle(_translate("param", "Param"))

