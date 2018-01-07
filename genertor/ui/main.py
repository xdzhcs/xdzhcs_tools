# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'java_model_generator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QWidget
import genertor.ui.java_model_generator  as mg
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    ui = mg.Ui_Generator_Form()

    ui.setupUi(w)
    w.show()
    w.setWindowTitle('bean 生成器')
    sys.exit(app.exec_())