# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SARsim_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(1144, 771)
        dialog.setWindowOpacity(0.95)
        self.raytraceView = PlotWidget(dialog)
        self.raytraceView.setGeometry(QtCore.QRect(40, 40, 512, 512))
        self.raytraceView.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.raytraceView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.raytraceView.setObjectName("raytraceView")
        self.sarView = PlotWidget(dialog)
        self.sarView.setGeometry(QtCore.QRect(590, 40, 512, 512))
        self.sarView.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.sarView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sarView.setObjectName("sarView")
        self.openButton = QtWidgets.QPushButton(dialog)
        self.openButton.setGeometry(QtCore.QRect(40, 580, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.openButton.setFont(font)
        self.openButton.setStyleSheet("")
        self.openButton.setObjectName("openButton")
        self.offnadSpinBox = QtWidgets.QDoubleSpinBox(dialog)
        self.offnadSpinBox.setGeometry(QtCore.QRect(110, 640, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.offnadSpinBox.setFont(font)
        self.offnadSpinBox.setMinimum(30.0)
        self.offnadSpinBox.setMaximum(70.0)
        self.offnadSpinBox.setSingleStep(5.0)
        self.offnadSpinBox.setObjectName("offnadSpinBox")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 640, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(270, 580, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.offnadSlider = QtWidgets.QSlider(dialog)
        self.offnadSlider.setGeometry(QtCore.QRect(250, 640, 411, 31))
        self.offnadSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #6ee, stop: 1 #bff);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bee, stop: 1 #5bf);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #555;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.offnadSlider.setMinimum(30)
        self.offnadSlider.setMaximum(70)
        self.offnadSlider.setSingleStep(5)
        self.offnadSlider.setProperty("value", 30)
        self.offnadSlider.setOrientation(QtCore.Qt.Horizontal)
        self.offnadSlider.setObjectName("offnadSlider")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 700, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.rotateSlider = QtWidgets.QSlider(dialog)
        self.rotateSlider.setGeometry(QtCore.QRect(250, 700, 411, 31))
        self.rotateSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #6ee, stop: 1 #bff);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bee, stop: 1 #5bf);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #555;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.rotateSlider.setMinimum(0)
        self.rotateSlider.setMaximum(360)
        self.rotateSlider.setSingleStep(5)
        self.rotateSlider.setProperty("value", 0)
        self.rotateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rotateSlider.setObjectName("rotateSlider")
        self.rotateSpinBox = QtWidgets.QDoubleSpinBox(dialog)
        self.rotateSpinBox.setGeometry(QtCore.QRect(110, 700, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rotateSpinBox.setFont(font)
        self.rotateSpinBox.setMinimum(-5.0)
        self.rotateSpinBox.setMaximum(360.0)
        self.rotateSpinBox.setSingleStep(5.0)
        self.rotateSpinBox.setProperty("value", 0.0)
        self.rotateSpinBox.setObjectName("rotateSpinBox")
        self.runSARButton = QtWidgets.QPushButton(dialog)
        self.runSARButton.setGeometry(QtCore.QRect(910, 700, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.runSARButton.setFont(font)
        self.runSARButton.setObjectName("runSARButton")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(750, 640, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.scale1SpinBox = QtWidgets.QDoubleSpinBox(dialog)
        self.scale1SpinBox.setGeometry(QtCore.QRect(820, 640, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.scale1SpinBox.setFont(font)
        self.scale1SpinBox.setDecimals(1)
        self.scale1SpinBox.setMinimum(0.0)
        self.scale1SpinBox.setMaximum(1000.0)
        self.scale1SpinBox.setSingleStep(5.0)
        self.scale1SpinBox.setProperty("value", 80.0)
        self.scale1SpinBox.setObjectName("scale1SpinBox")
        self.label_7 = QtWidgets.QLabel(dialog)
        self.label_7.setGeometry(QtCore.QRect(80, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(dialog)
        self.label_8.setGeometry(QtCore.QRect(630, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.sarUpView = PlotWidget(dialog)
        self.sarUpView.setGeometry(QtCore.QRect(591, 41, 181, 181))
        self.sarUpView.setFrameShape(QtWidgets.QFrame.Box)
        self.sarUpView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sarUpView.setLineWidth(2)
        self.sarUpView.setObjectName("sarUpView")
        self.runRayTraceButton = QtWidgets.QPushButton(dialog)
        self.runRayTraceButton.setGeometry(QtCore.QRect(710, 700, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.runRayTraceButton.setFont(font)
        self.runRayTraceButton.setObjectName("runRayTraceButton")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(555, 245, 31, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("arrow.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(910, 740, 231, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ashida.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.stepLabel = QtWidgets.QLabel(dialog)
        self.stepLabel.setGeometry(QtCore.QRect(960, 580, 121, 111))
        self.stepLabel.setText("")
        self.stepLabel.setPixmap(QtGui.QPixmap("step0.png"))
        self.stepLabel.setScaledContents(True)
        self.stepLabel.setObjectName("stepLabel")
        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(1068, 518, 60, 60))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("edge2.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(dialog)
        self.label_9.setGeometry(QtCore.QRect(518, 518, 60, 60))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("edge2.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(dialog)
        self.label_10.setGeometry(QtCore.QRect(15, 15, 60, 60))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("edge1.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(dialog)
        self.label_11.setGeometry(QtCore.QRect(565, 15, 60, 60))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("edge1.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(dialog)
        self.label_12.setGeometry(QtCore.QRect(0, 710, 31, 60))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("edge3.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(dialog)
        self.label_13.setGeometry(QtCore.QRect(0, 580, 1141, 191))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("line2.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(dialog)
        self.label_14.setGeometry(QtCore.QRect(170, 15, 381, 21))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("bar.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(dialog)
        self.label_15.setGeometry(QtCore.QRect(720, 15, 381, 21))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("bar.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(dialog)
        self.label_16.setGeometry(QtCore.QRect(0, 80, 41, 621))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("line.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(dialog)
        self.label_17.setGeometry(QtCore.QRect(1100, 40, 41, 471))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("line.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_13.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_12.raise_()
        self.label_11.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.label_6.raise_()
        self.raytraceView.raise_()
        self.sarView.raise_()
        self.openButton.raise_()
        self.offnadSpinBox.raise_()
        self.label_3.raise_()
        self.offnadSlider.raise_()
        self.rotateSlider.raise_()
        self.rotateSpinBox.raise_()
        self.runSARButton.raise_()
        self.label_5.raise_()
        self.scale1SpinBox.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.sarUpView.raise_()
        self.runRayTraceButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.stepLabel.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.label_14.raise_()
        self.label_15.raise_()

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "SAR simulator"))
        self.openButton.setText(_translate("dialog", "1.Open"))
        self.label_3.setText(_translate("dialog", "Offnadir"))
        self.lineEdit.setText(_translate("dialog", "c130.obj"))
        self.label_4.setText(_translate("dialog", "Rotate"))
        self.runSARButton.setText(_translate("dialog", "3.Run SAR"))
        self.label_5.setText(_translate("dialog", "Scale"))
        self.label_7.setText(_translate("dialog", "Ray Trace"))
        self.label_8.setText(_translate("dialog", "SAR"))
        self.runRayTraceButton.setText(_translate("dialog", "2.Run Ray Trace"))

from pyqtgraph import PlotWidget
