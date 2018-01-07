# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'java_model_generator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Generator_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 564)
        self.content_text_edit = QtWidgets.QPlainTextEdit(Form)
        self.content_text_edit.setGeometry(QtCore.QRect(20, 150, 711, 401))
        self.content_text_edit.setObjectName("content_text_edit")
        self.create_btn = QtWidgets.QPushButton(Form)
        self.create_btn.setGeometry(QtCore.QRect(630, 20, 75, 23))
        self.create_btn.setObjectName("create_btn")
        self.cancel_btn = QtWidgets.QPushButton(Form)
        self.cancel_btn.setGeometry(QtCore.QRect(630, 60, 75, 23))
        self.cancel_btn.setObjectName("cancel_btn")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 20, 471, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table_name_label = QtWidgets.QLabel(self.widget)
        self.table_name_label.setObjectName("table_name_label")
        self.horizontalLayout.addWidget(self.table_name_label)
        self.table_name_edit = QtWidgets.QLineEdit(self.widget)
        self.table_name_edit.setObjectName("table_name_edit")
        self.horizontalLayout.addWidget(self.table_name_edit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.create_btn.setText(_translate("Form", "生成"))
        self.cancel_btn.setText(_translate("Form", "取消"))
        self.table_name_label.setText(_translate("Form", "表名"))

