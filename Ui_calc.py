# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 322, 378))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.output_lb = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.output_lb.setFont(font)
        self.output_lb.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.output_lb.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.output_lb.setMidLineWidth(2)
        self.output_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.output_lb.setObjectName("output_lb")
        self.verticalLayout.addWidget(self.output_lb)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.percent_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percent_btn.setFont(font)
        self.percent_btn.setObjectName("percent_btn")
        self.horizontalLayout.addWidget(self.percent_btn)
        self.clear_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.clear_btn.setFont(font)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        self.backspace_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.backspace_btn.setFont(font)
        self.backspace_btn.setObjectName("backspace_btn")
        self.horizontalLayout.addWidget(self.backspace_btn)
        self.divide_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divide_btn.setFont(font)
        self.divide_btn.setObjectName("divide_btn")
        self.horizontalLayout.addWidget(self.divide_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.seven_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.seven_btn.setFont(font)
        self.seven_btn.setObjectName("seven_btn")
        self.horizontalLayout_2.addWidget(self.seven_btn)
        self.eight__btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eight__btn.setFont(font)
        self.eight__btn.setObjectName("eight__btn")
        self.horizontalLayout_2.addWidget(self.eight__btn)
        self.nine_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nine_btn.setFont(font)
        self.nine_btn.setObjectName("nine_btn")
        self.horizontalLayout_2.addWidget(self.nine_btn)
        self.multiply_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiply_btn.setFont(font)
        self.multiply_btn.setObjectName("multiply_btn")
        self.horizontalLayout_2.addWidget(self.multiply_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.four_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.four_btn.setFont(font)
        self.four_btn.setObjectName("four_btn")
        self.horizontalLayout_3.addWidget(self.four_btn)
        self.five_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.five_btn.setFont(font)
        self.five_btn.setObjectName("five_btn")
        self.horizontalLayout_3.addWidget(self.five_btn)
        self.six_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.six_btn.setFont(font)
        self.six_btn.setObjectName("six_btn")
        self.horizontalLayout_3.addWidget(self.six_btn)
        self.minus_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minus_btn.setFont(font)
        self.minus_btn.setObjectName("minus_btn")
        self.horizontalLayout_3.addWidget(self.minus_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.one_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.one_btn.setFont(font)
        self.one_btn.setObjectName("one_btn")
        self.horizontalLayout_4.addWidget(self.one_btn)
        self.two_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.two_btn.setFont(font)
        self.two_btn.setObjectName("two_btn")
        self.horizontalLayout_4.addWidget(self.two_btn)
        self.three_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.three_btn.setFont(font)
        self.three_btn.setObjectName("three_btn")
        self.horizontalLayout_4.addWidget(self.three_btn)
        self.plus_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plus_btn.setFont(font)
        self.plus_btn.setObjectName("plus_btn")
        self.horizontalLayout_4.addWidget(self.plus_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.plus_minus_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plus_minus_btn.setFont(font)
        self.plus_minus_btn.setObjectName("plus_minus_btn")
        self.horizontalLayout_5.addWidget(self.plus_minus_btn)
        self.zero_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zero_btn.setFont(font)
        self.zero_btn.setObjectName("zero_btn")
        self.horizontalLayout_5.addWidget(self.zero_btn)
        self.decimal_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimal_btn.setFont(font)
        self.decimal_btn.setObjectName("decimal_btn")
        self.horizontalLayout_5.addWidget(self.decimal_btn)
        self.equals_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equals_btn.setFont(font)
        self.equals_btn.setObjectName("equals_btn")
        self.horizontalLayout_5.addWidget(self.equals_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 341, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.output_lb.setText(_translate("MainWindow", "0"))
        self.percent_btn.setText(_translate("MainWindow", "%"))
        self.clear_btn.setText(_translate("MainWindow", "C"))
        self.backspace_btn.setText(_translate("MainWindow", "<<"))
        self.divide_btn.setText(_translate("MainWindow", "/"))
        self.seven_btn.setText(_translate("MainWindow", "7"))
        self.eight__btn.setText(_translate("MainWindow", "8"))
        self.nine_btn.setText(_translate("MainWindow", "9"))
        self.multiply_btn.setText(_translate("MainWindow", "x"))
        self.four_btn.setText(_translate("MainWindow", "4"))
        self.five_btn.setText(_translate("MainWindow", "5"))
        self.six_btn.setText(_translate("MainWindow", "6"))
        self.minus_btn.setText(_translate("MainWindow", "-"))
        self.one_btn.setText(_translate("MainWindow", "1"))
        self.two_btn.setText(_translate("MainWindow", "2"))
        self.three_btn.setText(_translate("MainWindow", "3"))
        self.plus_btn.setText(_translate("MainWindow", "+"))
        self.plus_minus_btn.setText(_translate("MainWindow", "+/-"))
        self.zero_btn.setText(_translate("MainWindow", "0"))
        self.decimal_btn.setText(_translate("MainWindow", "."))
        self.equals_btn.setText(_translate("MainWindow", "="))