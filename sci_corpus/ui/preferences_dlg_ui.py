# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'strip_options_dlg.ui'
#
# Created: Mon Apr 28 15:19:45 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(492, 331)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEditReplaceBy = QtGui.QLineEdit(Dialog)
        self.lineEditReplaceBy.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEditReplaceBy.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditReplaceBy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditReplaceBy.setObjectName("lineEditReplaceBy")
        self.gridLayout_2.addWidget(self.lineEditReplaceBy, 1, 3, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 2)
        self.label = QtGui.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.comboBoxMarker = QtGui.QComboBox(Dialog)
        self.comboBoxMarker.setObjectName("comboBoxMarker")
        self.comboBoxMarker.addItem("")
        self.comboBoxMarker.addItem("")
        self.comboBoxMarker.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxMarker, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 90))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonInternally = QtGui.QRadioButton(self.groupBox)
        self.radioButtonInternally.setChecked(True)
        self.radioButtonInternally.setObjectName("radioButtonInternally")
        self.horizontalLayout.addWidget(self.radioButtonInternally)
        self.radioButtonExternally = QtGui.QRadioButton(self.groupBox)
        self.radioButtonExternally.setObjectName("radioButtonExternally")
        self.horizontalLayout.addWidget(self.radioButtonExternally)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 5)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 5)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 4, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 5, 0, 1, 5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Strip Sentence Options", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditReplaceBy.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Select your marker</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Marker:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMarker.setItemText(0, QtGui.QApplication.translate("Dialog", "{{}}", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMarker.setItemText(1, QtGui.QApplication.translate("Dialog", "{}", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMarker.setItemText(2, QtGui.QApplication.translate("Dialog", "[ ]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Replace By:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Replace text", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonInternally.setText(QtGui.QApplication.translate("Dialog", "Internally", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonExternally.setText(QtGui.QApplication.translate("Dialog", "Externally", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Please, be carefully! </span></p><p><span style=\" font-size:10pt;\">Once you have choosen your pattern, you are not encoraged </span></p><p><span style=\" font-size:10pt;\">to change anymore in the same database file.</span></p><p><span style=\" font-size:10pt;\">This strip just works in vizualization mode, your database will NOT be changed.</span></p><p><span style=\" font-size:10pt;\">You will not lost your replaced sub sentences.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

