# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_dlg.ui'
#
# Created: Wed Apr 30 23:12:15 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.setEnabled(True)
        Dialog.resize(530, 264)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Window/Icon_Sci_Corpus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.labelVersion = QtGui.QLabel(Dialog)
        self.labelVersion.setStyleSheet("color: rgb(80, 80, 80);\n"
"font: 63 20pt \"URW Gothic L\";")
        self.labelVersion.setTextFormat(QtCore.Qt.AutoText)
        self.labelVersion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelVersion.setObjectName("labelVersion")
        self.gridLayout.addWidget(self.labelVersion, 0, 0, 1, 1)
        self.labelProducedBy = QtGui.QLabel(Dialog)
        self.labelProducedBy.setStyleSheet("color: rgb(132, 132, 132);")
        self.labelProducedBy.setObjectName("labelProducedBy")
        self.gridLayout.addWidget(self.labelProducedBy, 4, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 1)
        self.labelIcon = QtGui.QLabel(Dialog)
        self.labelIcon.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelIcon.setText("")
        self.labelIcon.setPixmap(QtGui.QPixmap(":/Window/Logo_Sci_Corpus_Without_Version.png"))
        self.labelIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIcon.setObjectName("labelIcon")
        self.gridLayout.addWidget(self.labelIcon, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.labelVersion.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:8pt;\">V.1.0 </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelProducedBy.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Produced by: </span></p><p align=\"center\"><span style=\" font-size:8pt;\">Daniel C. Pizetta, José R.F. Ronqui and Tiago Campos</span></p><p align=\"center\"><span style=\" font-size:8pt;\">Institute of Physics of Sao Carlos - IFSC</span></p><p align=\"center\"><span style=\" font-size:8pt;\">University of Sao Paulo - USP</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import sci_corpus_resource_rc
