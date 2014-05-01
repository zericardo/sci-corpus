# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_dlg.ui'
#
# Created: Thu May  1 10:44:03 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.setEnabled(True)
        Dialog.resize(530, 240)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(530, 240))
        Dialog.setMaximumSize(QtCore.QSize(530, 240))
        Dialog.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Window/Icon_Sci_Corpus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 2, 1, 1)
        self.labelYear = QtGui.QLabel(Dialog)
        self.labelYear.setMaximumSize(QtCore.QSize(30, 16777215))
        self.labelYear.setStyleSheet("color: rgb(80, 80, 80);\n"
"font: \"URW Gothic L\";")
        self.labelYear.setObjectName("labelYear")
        self.gridLayout.addWidget(self.labelYear, 0, 3, 1, 1)
        self.labelIcon = QtGui.QLabel(Dialog)
        self.labelIcon.setEnabled(True)
        self.labelIcon.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelIcon.setText("")
        self.labelIcon.setPixmap(QtGui.QPixmap(":/Window/Logo_Sci_Corpus_Without_Version.png"))
        self.labelIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIcon.setObjectName("labelIcon")
        self.gridLayout.addWidget(self.labelIcon, 2, 0, 1, 4)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 25)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 4)
        self.labelInformationProgress = QtGui.QLabel(Dialog)
        self.labelInformationProgress.setStyleSheet("color: rgb(100, 100, 100);\n"
"")
        self.labelInformationProgress.setObjectName("labelInformationProgress")
        self.gridLayout.addWidget(self.labelInformationProgress, 4, 0, 1, 4)
        self.labelProducedBy = QtGui.QLabel(Dialog)
        self.labelProducedBy.setStyleSheet("color: rgb(100, 100, 100);\n"
"")
        self.labelProducedBy.setTextFormat(QtCore.Qt.AutoText)
        self.labelProducedBy.setObjectName("labelProducedBy")
        self.gridLayout.addWidget(self.labelProducedBy, 5, 0, 1, 4)
        self.labelVersion = QtGui.QLabel(Dialog)
        self.labelVersion.setStyleSheet("color: rgb(80, 80, 80);\n"
"font: \"URW Gothic L\";")
        self.labelVersion.setTextFormat(QtCore.Qt.AutoText)
        self.labelVersion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelVersion.setObjectName("labelVersion")
        self.gridLayout.addWidget(self.labelVersion, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.labelYear.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:8pt;\">2014</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelInformationProgress.setText(QtGui.QApplication.translate("Dialog", "Progress information ...", None, QtGui.QApplication.UnicodeUTF8))
        self.labelProducedBy.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Produced by: <br>Daniel C. Pizetta - José R.F. Ronqui - Tiago Campos<br>Institute of Physics of Sao Carlos - IFSC -- University of Sao Paulo - USP</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelVersion.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:8pt;\">V.1.0 </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import ui.sci_corpus_resource_rc
