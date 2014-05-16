# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_mw.ui'
#
# Created: Thu May  1 19:41:29 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 867)
        font = QtGui.QFont()
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/Window/Icon_Sci_Corpus.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonSentenceRemove = QtGui.QPushButton(self.widget)
        self.pushButtonSentenceRemove.setMaximumSize(
            QtCore.QSize(
                30,
                16777215))
        self.pushButtonSentenceRemove.setObjectName("pushButtonSentenceRemove")
        self.gridLayout_2.addWidget(self.pushButtonSentenceRemove, 4, 4, 1, 1)
        self.labelReference = QtGui.QLabel(self.widget)
        self.labelReference.setObjectName("labelReference")
        self.gridLayout_2.addWidget(self.labelReference, 4, 0, 1, 1)
        self.pushButtonSentenceUpdate = QtGui.QPushButton(self.widget)
        self.pushButtonSentenceUpdate.setMaximumSize(
            QtCore.QSize(
                85,
                16777215))
        self.pushButtonSentenceUpdate.setObjectName("pushButtonSentenceUpdate")
        self.gridLayout_2.addWidget(self.pushButtonSentenceUpdate, 4, 5, 1, 1)
        self.lineEditReference = QtGui.QLineEdit(self.widget)
        self.lineEditReference.setObjectName("lineEditReference")
        self.gridLayout_2.addWidget(self.lineEditReference, 4, 1, 1, 1)
        self.pushButtonSentenceAdd = QtGui.QPushButton(self.widget)
        self.pushButtonSentenceAdd.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonSentenceAdd.setObjectName("pushButtonSentenceAdd")
        self.gridLayout_2.addWidget(self.pushButtonSentenceAdd, 4, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 17))
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.textEditSentence = QtGui.QTextEdit(self.widget)
        self.textEditSentence.setMinimumSize(QtCore.QSize(0, 0))
        self.textEditSentence.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEditSentence.setObjectName("textEditSentence")
        self.gridLayout_2.addWidget(self.textEditSentence, 1, 0, 1, 6)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSection = QtGui.QMenu(self.menubar)
        self.menuSection.setObjectName("menuSection")
        self.menuSubSection = QtGui.QMenu(self.menubar)
        self.menuSubSection.setObjectName("menuSubSection")
        self.menuFunction = QtGui.QMenu(self.menubar)
        self.menuFunction.setObjectName("menuFunction")
        self.menuSentence = QtGui.QMenu(self.menubar)
        self.menuSentence.setObjectName("menuSentence")
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidgetSection = QtGui.QDockWidget(MainWindow)
        self.dockWidgetSection.setObjectName("dockWidgetSection")
        self.dockWidgetContentsSection = QtGui.QWidget()
        self.dockWidgetContentsSection.setObjectName(
            "dockWidgetContentsSection")
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContentsSection)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonSectionRemove = QtGui.QPushButton(
            self.dockWidgetContentsSection)
        self.pushButtonSectionRemove.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonSectionRemove.setObjectName("pushButtonSectionRemove")
        self.gridLayout.addWidget(self.pushButtonSectionRemove, 0, 2, 1, 1)
        self.lineEditSection = QtGui.QLineEdit(self.dockWidgetContentsSection)
        self.lineEditSection.setText("")
        self.lineEditSection.setObjectName("lineEditSection")
        self.gridLayout.addWidget(self.lineEditSection, 0, 0, 1, 1)
        self.pushButtonSectionAdd = QtGui.QPushButton(
            self.dockWidgetContentsSection)
        self.pushButtonSectionAdd.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonSectionAdd.setObjectName("pushButtonSectionAdd")
        self.gridLayout.addWidget(self.pushButtonSectionAdd, 0, 1, 1, 1)
        self.pushButtonSectionUpdate = QtGui.QPushButton(
            self.dockWidgetContentsSection)
        self.pushButtonSectionUpdate.setObjectName("pushButtonSectionUpdate")
        self.gridLayout.addWidget(self.pushButtonSectionUpdate, 0, 3, 1, 1)
        self.listWidgetSection = QtGui.QListWidget(
            self.dockWidgetContentsSection)
        self.listWidgetSection.setMinimumSize(QtCore.QSize(0, 100))
        self.listWidgetSection.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidgetSection.setInputMethodHints(
            QtCore.Qt.ImhPreferUppercase)
        self.listWidgetSection.setDragDropMode(
            QtGui.QAbstractItemView.DragDrop)
        self.listWidgetSection.setAlternatingRowColors(False)
        self.listWidgetSection.setSelectionMode(
            QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetSection.setMovement(QtGui.QListView.Free)
        self.listWidgetSection.setViewMode(QtGui.QListView.ListMode)
        self.listWidgetSection.setModelColumn(0)
        self.listWidgetSection.setUniformItemSizes(False)
        self.listWidgetSection.setSelectionRectVisible(True)
        self.listWidgetSection.setObjectName("listWidgetSection")
        self.gridLayout.addWidget(self.listWidgetSection, 1, 0, 1, 4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(
            40,
            20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.dockWidgetContentsSection)
        self.label.setStyleSheet("color: rgb(111, 111, 111);")
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.labelSelectedSection = QtGui.QLabel(
            self.dockWidgetContentsSection)
        self.labelSelectedSection.setStyleSheet("color: rgb(111, 111, 111);")
        self.labelSelectedSection.setObjectName("labelSelectedSection")
        self.horizontalLayout.addWidget(self.labelSelectedSection)
        self.label_3 = QtGui.QLabel(self.dockWidgetContentsSection)
        self.label_3.setStyleSheet("color: rgb(111, 111, 111);")
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.labelDisplayedSection = QtGui.QLabel(
            self.dockWidgetContentsSection)
        self.labelDisplayedSection.setStyleSheet("color: rgb(111, 111, 111);")
        self.labelDisplayedSection.setObjectName("labelDisplayedSection")
        self.horizontalLayout.addWidget(self.labelDisplayedSection)
        self.label_2 = QtGui.QLabel(self.dockWidgetContentsSection)
        self.label_2.setStyleSheet("color: rgb(111, 111, 111);")
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.labelTotalSection = QtGui.QLabel(self.dockWidgetContentsSection)
        self.labelTotalSection.setStyleSheet("color: rgb(111, 111, 111);")
        self.labelTotalSection.setObjectName("labelTotalSection")
        self.horizontalLayout.addWidget(self.labelTotalSection)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 3, 4)
        self.line_3 = QtGui.QFrame(self.dockWidgetContentsSection)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 6, 0, 1, 4)
        self.dockWidgetSection.setWidget(self.dockWidgetContentsSection)
        MainWindow.addDockWidget(
            QtCore.Qt.DockWidgetArea(4),
            self.dockWidgetSection)
        self.dockWidgetSubSection = QtGui.QDockWidget(MainWindow)
        self.dockWidgetSubSection.setObjectName("dockWidgetSubSection")
        self.dockWidgetContentsSubSection = QtGui.QWidget()
        self.dockWidgetContentsSubSection.setObjectName(
            "dockWidgetContentsSubSection")
        self.gridLayout_3 = QtGui.QGridLayout(
            self.dockWidgetContentsSubSection)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEditSubSection = QtGui.QLineEdit(
            self.dockWidgetContentsSubSection)
        self.lineEditSubSection.setObjectName("lineEditSubSection")
        self.gridLayout_3.addWidget(self.lineEditSubSection, 0, 0, 1, 1)
        self.pushButtonSubSectionAdd = QtGui.QPushButton(
            self.dockWidgetContentsSubSection)
        self.pushButtonSubSectionAdd.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonSubSectionAdd.setObjectName("pushButtonSubSectionAdd")
        self.gridLayout_3.addWidget(self.pushButtonSubSectionAdd, 0, 1, 1, 1)
        self.pushButtonSubSectionRemove = QtGui.QPushButton(
            self.dockWidgetContentsSubSection)
        self.pushButtonSubSectionRemove.setMaximumSize(
            QtCore.QSize(
                30,
                16777215))
        self.pushButtonSubSectionRemove.setObjectName(
            "pushButtonSubSectionRemove")
        self.gridLayout_3.addWidget(
            self.pushButtonSubSectionRemove,
            0,
            2,
            1,
            1)
        self.pushButtonSubSectionUpdate = QtGui.QPushButton(
            self.dockWidgetContentsSubSection)
        self.pushButtonSubSectionUpdate.setObjectName(
            "pushButtonSubSectionUpdate")
        self.gridLayout_3.addWidget(
            self.pushButtonSubSectionUpdate,
            0,
            3,
            1,
            1)
        self.listWidgetSubSection = QtGui.QListWidget(
            self.dockWidgetContentsSubSection)
        self.listWidgetSubSection.setMinimumSize(QtCore.QSize(0, 100))
        self.listWidgetSubSection.setMaximumSize(
            QtCore.QSize(
                16777215,
                16777215))
        self.listWidgetSubSection.setDragDropMode(
            QtGui.QAbstractItemView.DragOnly)
        self.listWidgetSubSection.setAlternatingRowColors(False)
        self.listWidgetSubSection.setSelectionMode(
            QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetSubSection.setMovement(QtGui.QListView.Free)
        self.listWidgetSubSection.setSelectionRectVisible(True)
        self.listWidgetSubSection.setObjectName("listWidgetSubSection")
        self.gridLayout_3.addWidget(self.listWidgetSubSection, 1, 0, 1, 4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(
            40,
            20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_7 = QtGui.QLabel(self.dockWidgetContentsSubSection)
        self.label_7.setStyleSheet("color: rgb(111, 111, 111);")
        self.label_7.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.labelSelectedSubSection = QtGui.QLabel(
            self.dockWidgetContentsSubSection)
        self.labelSelectedSubSection.setStyleSheet(
            "color: rgb(111, 111, 111);")
        self.labelSelectedSubSection.setObjectName("labelSelectedSubSection")
        self.horizontalLayout_2.addWidget(self.labelSelectedSubSection)
        self.label_9 = QtGui.QLabel(self.dockWidgetContentsSubSection)
        self.label_9.setStyleSheet("color: rgb(111, 111, 111);")
        self.label_9.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.labelDisplayedSubSection = QtGui.QLabel(
            self.dockWidgetContentsSubSection)
        self.labelDisplayedSubSection.setStyleSheet(
            "color: rgb(111, 111, 111);")
        self.labelDisplayedSubSection.setObjectName("labelDisplayedSubSection")
        self.horizontalLayout_2.addWidget(self.labelDisplayedSubSection)
        self.label_8 = QtGui.QLabel(self.dockWidgetContentsSubSection)
        self.label_8.setStyleSheet("color: rgb(111, 111, 111);")
        self.label_8.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.labelTotalSubSection = QtGui.QLabel(
            self.dockWidgetContentsSubSection)
        self.labelTotalSubSection.setStyleSheet("color: rgb(111, 111, 111);")
        self.labelTotalSubSection.setObjectName("labelTotalSubSection")
        self.horizontalLayout_2.addWidget(self.labelTotalSubSection)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 2, 4)
        self.line_2 = QtGui.QFrame(self.dockWidgetContentsSubSection)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 4, 0, 1, 4)
        self.dockWidgetSubSection.setWidget(self.dockWidgetContentsSubSection)
        MainWindow.addDockWidget(
            QtCore.Qt.DockWidgetArea(4),
            self.dockWidgetSubSection)
        self.dockWidgetFunction = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dockWidgetFunction.sizePolicy().hasHeightForWidth())
        self.dockWidgetFunction.setSizePolicy(sizePolicy)
        self.dockWidgetFunction.setObjectName("dockWidgetFunction")
        self.dockWidgetContentsFunction = QtGui.QWidget()
        self.dockWidgetContentsFunction.setObjectName(
            "dockWidgetContentsFunction")
        self.gridLayout_4 = QtGui.QGridLayout(self.dockWidgetContentsFunction)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEditFunction = QtGui.QLineEdit(
            self.dockWidgetContentsFunction)
        self.lineEditFunction.setObjectName("lineEditFunction")
        self.gridLayout_4.addWidget(self.lineEditFunction, 0, 0, 1, 1)
        self.pushButtonFunctionAdd = QtGui.QPushButton(
            self.dockWidgetContentsFunction)
        self.pushButtonFunctionAdd.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonFunctionAdd.setObjectName("pushButtonFunctionAdd")
        self.gridLayout_4.addWidget(self.pushButtonFunctionAdd, 0, 1, 1, 1)
        self.pushButtonFunctionRemove = QtGui.QPushButton(
            self.dockWidgetContentsFunction)
        self.pushButtonFunctionRemove.setMaximumSize(
            QtCore.QSize(
                30,
                16777215))
        self.pushButtonFunctionRemove.setObjectName("pushButtonFunctionRemove")
        self.gridLayout_4.addWidget(self.pushButtonFunctionRemove, 0, 2, 1, 1)
        self.pushButtonFunctionUpdate = QtGui.QPushButton(
            self.dockWidgetContentsFunction)
        self.pushButtonFunctionUpdate.setObjectName("pushButtonFunctionUpdate")
        self.gridLayout_4.addWidget(self.pushButtonFunctionUpdate, 0, 3, 1, 1)
        self.listWidgetFunction = QtGui.QListWidget(
            self.dockWidgetContentsFunction)
        self.listWidgetFunction.setMinimumSize(QtCore.QSize(0, 100))
        self.listWidgetFunction.setMidLineWidth(0)
        self.listWidgetFunction.setDragDropMode(
            QtGui.QAbstractItemView.DragOnly)
        self.listWidgetFunction.setAlternatingRowColors(False)
        self.listWidgetFunction.setSelectionMode(
            QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetFunction.setMovement(QtGui.QListView.Free)
        self.listWidgetFunction.setSelectionRectVisible(True)
        self.listWidgetFunction.setObjectName("listWidgetFunction")
        self.gridLayout_4.addWidget(self.listWidgetFunction, 1, 0, 1, 4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtGui.QSpacerItem(
            40,
            20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_14 = QtGui.QLabel(self.dockWidgetContentsFunction)
        self.label_14.setStyleSheet("color: rgb(111, 111, 111);")
        self.label_14.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.labelSelectedFunction = QtGui.QLabel(
            self.dockWidgetContentsFunction)
        self.labelSelectedFunction.setStyleSheet("color: rgb(111, 111, 111);")
        self.labelSelectedFunction.setObjectName("labelSelectedFunction")
        self.horizontalLayout_4.addWidget(self.labelSelectedFunction)
        self.label_15 = QtGui.QLabel(self.dockWidgetContentsFunction)
        self.label_15.setStyleSheet("color: rgb(111, 111, 111);")
        self.label_15.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.labelDisplayedFunction = QtGui.QLabel(
            self.dockWidgetContentsFunction)
        self.labelDisplayedFunction.setStyleSheet("color: rgb(111, 111, 111);")
        self.labelDisplayedFunction.setObjectName("labelDisplayedFunction")
        self.horizontalLayout_4.addWidget(self.labelDisplayedFunction)
        self.label_17 = QtGui.QLabel(self.dockWidgetContentsFunction)
        self.label_17.setStyleSheet("color: rgb(111, 111, 111);")
        self.label_17.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_4.addWidget(self.label_17)
        self.labelTotalFunction = QtGui.QLabel(self.dockWidgetContentsFunction)
        self.labelTotalFunction.setStyleSheet("color: rgb(111, 111, 111);")
        self.labelTotalFunction.setObjectName("labelTotalFunction")
        self.horizontalLayout_4.addWidget(self.labelTotalFunction)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 2, 0, 1, 4)
        self.line = QtGui.QFrame(self.dockWidgetContentsFunction)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 3, 0, 1, 4)
        self.dockWidgetFunction.setWidget(self.dockWidgetContentsFunction)
        MainWindow.addDockWidget(
            QtCore.Qt.DockWidgetArea(4),
            self.dockWidgetFunction)
        self.dockWidgetTableView = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dockWidgetTableView.sizePolicy().hasHeightForWidth())
        self.dockWidgetTableView.setSizePolicy(sizePolicy)
        self.dockWidgetTableView.setObjectName("dockWidgetTableView")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_5 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBoxReference = QtGui.QCheckBox(self.dockWidgetContents_2)
        self.checkBoxReference.setObjectName("checkBoxReference")
        self.gridLayout_5.addWidget(self.checkBoxReference, 0, 4, 1, 1)
        self.checkBoxStrip = QtGui.QCheckBox(self.dockWidgetContents_2)
        self.checkBoxStrip.setChecked(True)
        self.checkBoxStrip.setObjectName("checkBoxStrip")
        self.gridLayout_5.addWidget(self.checkBoxStrip, 0, 6, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(
            40,
            20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 7, 1, 1)
        self.checkBoxSection = QtGui.QCheckBox(self.dockWidgetContents_2)
        self.checkBoxSection.setObjectName("checkBoxSection")
        self.gridLayout_5.addWidget(self.checkBoxSection, 0, 0, 1, 1)
        self.checkBoxFunction = QtGui.QCheckBox(self.dockWidgetContents_2)
        self.checkBoxFunction.setObjectName("checkBoxFunction")
        self.gridLayout_5.addWidget(self.checkBoxFunction, 0, 2, 1, 1)
        self.checkBoxSubSection = QtGui.QCheckBox(self.dockWidgetContents_2)
        self.checkBoxSubSection.setObjectName("checkBoxSubSection")
        self.gridLayout_5.addWidget(self.checkBoxSubSection, 0, 1, 1, 1)
        self.checkBoxSentence = QtGui.QCheckBox(self.dockWidgetContents_2)
        self.checkBoxSentence.setChecked(True)
        self.checkBoxSentence.setObjectName("checkBoxSentence")
        self.gridLayout_5.addWidget(self.checkBoxSentence, 0, 3, 1, 1)
        self.line_4 = QtGui.QFrame(self.dockWidgetContents_2)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_5.addWidget(self.line_4, 0, 5, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_4.setStyleSheet("color: rgb(111, 111, 111);")
        self.label_4.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.labelSelectedSentence = QtGui.QLabel(self.dockWidgetContents_2)
        self.labelSelectedSentence.setStyleSheet("color: rgb(111, 111, 111);")
        self.labelSelectedSentence.setObjectName("labelSelectedSentence")
        self.horizontalLayout_3.addWidget(self.labelSelectedSentence)
        self.label_6 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_6.setStyleSheet("color: rgb(111, 111, 111);")
        self.label_6.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.labelDisplayedSentence = QtGui.QLabel(self.dockWidgetContents_2)
        self.labelDisplayedSentence.setStyleSheet("color: rgb(111, 111, 111);")
        self.labelDisplayedSentence.setObjectName("labelDisplayedSentence")
        self.horizontalLayout_3.addWidget(self.labelDisplayedSentence)
        self.label_11 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_11.setStyleSheet("color: rgb(111, 111, 111);")
        self.label_11.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.labelTotalSentence = QtGui.QLabel(self.dockWidgetContents_2)
        self.labelTotalSentence.setStyleSheet("color: rgb(111, 111, 111);")
        self.labelTotalSentence.setObjectName("labelTotalSentence")
        self.horizontalLayout_3.addWidget(self.labelTotalSentence)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 8, 1, 1)
        self.tableWidgetSentence = QtGui.QTableWidget(
            self.dockWidgetContents_2)
        self.tableWidgetSentence.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidgetSentence.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetSentence.setDragDropOverwriteMode(False)
        self.tableWidgetSentence.setAlternatingRowColors(True)
        self.tableWidgetSentence.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetSentence.setVerticalScrollMode(
            QtGui.QAbstractItemView.ScrollPerItem)
        self.tableWidgetSentence.setObjectName("tableWidgetSentence")
        self.tableWidgetSentence.setColumnCount(0)
        self.tableWidgetSentence.setRowCount(0)
        self.tableWidgetSentence.horizontalHeader(
        ).setCascadingSectionResizes(False)
        self.tableWidgetSentence.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidgetSentence.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetSentence.verticalHeader(
        ).setCascadingSectionResizes(False)
        self.tableWidgetSentence.verticalHeader().setSortIndicatorShown(True)
        self.tableWidgetSentence.verticalHeader().setStretchLastSection(False)
        self.gridLayout_5.addWidget(self.tableWidgetSentence, 2, 0, 1, 9)
        self.dockWidgetTableView.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(
            QtCore.Qt.DockWidgetArea(8),
            self.dockWidgetTableView)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidgetLogView = QtGui.QDockWidget(MainWindow)
        self.dockWidgetLogView.setObjectName("dockWidgetLogView")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_6 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButtonClearLog = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButtonClearLog.setMaximumSize(QtCore.QSize(85, 16777215))
        self.pushButtonClearLog.setObjectName("pushButtonClearLog")
        self.gridLayout_6.addWidget(self.pushButtonClearLog, 0, 0, 1, 1)
        self.textEditLogView = QtGui.QTextEdit(self.dockWidgetContents)
        self.textEditLogView.setEnabled(True)
        self.textEditLogView.setStyleSheet("color: rgb(85, 170, 255);\n"
                                           "background-color: rgb(0, 0, 0);")
        self.textEditLogView.setAutoFormatting(QtGui.QTextEdit.AutoBulletList)
        self.textEditLogView.setUndoRedoEnabled(False)
        self.textEditLogView.setReadOnly(True)
        self.textEditLogView.setObjectName("textEditLogView")
        self.gridLayout_6.addWidget(self.textEditLogView, 1, 0, 1, 1)
        self.dockWidgetLogView.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(
            QtCore.Qt.DockWidgetArea(8),
            self.dockWidgetLogView)
        self.actionOpen = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/File/document-open-7.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/File/document-save-3.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/File/document-save-as-3.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon3)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionClose = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/File/document-close-4.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.actionClose.setIcon(icon4)
        self.actionClose.setObjectName("actionClose")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionTips = QtGui.QAction(MainWindow)
        self.actionTips.setObjectName("actionTips")
        self.actionAddSection = QtGui.QAction(MainWindow)
        self.actionAddSection.setObjectName("actionAddSection")
        self.actionRemoveSection = QtGui.QAction(MainWindow)
        self.actionRemoveSection.setObjectName("actionRemoveSection")
        self.actionUpdateSection = QtGui.QAction(MainWindow)
        self.actionUpdateSection.setObjectName("actionUpdateSection")
        self.actionAddSubSection = QtGui.QAction(MainWindow)
        self.actionAddSubSection.setObjectName("actionAddSubSection")
        self.actionRemoveSubSection = QtGui.QAction(MainWindow)
        self.actionRemoveSubSection.setObjectName("actionRemoveSubSection")
        self.actionUpdateSubSection = QtGui.QAction(MainWindow)
        self.actionUpdateSubSection.setObjectName("actionUpdateSubSection")
        self.actionAddFunction = QtGui.QAction(MainWindow)
        self.actionAddFunction.setObjectName("actionAddFunction")
        self.actionRemoveFunction = QtGui.QAction(MainWindow)
        self.actionRemoveFunction.setObjectName("actionRemoveFunction")
        self.actionUpdateFunction = QtGui.QAction(MainWindow)
        self.actionUpdateFunction.setObjectName("actionUpdateFunction")
        self.actionAddSentence = QtGui.QAction(MainWindow)
        self.actionAddSentence.setObjectName("actionAddSentence")
        self.actionRemoveSentence = QtGui.QAction(MainWindow)
        self.actionRemoveSentence.setObjectName("actionRemoveSentence")
        self.actionUpdateSentence = QtGui.QAction(MainWindow)
        self.actionUpdateSentence.setObjectName("actionUpdateSentence")
        self.actionImport = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/File/document-import-2.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.actionImport.setIcon(icon5)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/File/document-export-4.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.actionExport.setIcon(icon6)
        self.actionExport.setObjectName("actionExport")
        self.actionTipsSection = QtGui.QAction(MainWindow)
        self.actionTipsSection.setObjectName("actionTipsSection")
        self.actionTipsSubSection = QtGui.QAction(MainWindow)
        self.actionTipsSubSection.setObjectName("actionTipsSubSection")
        self.actionTipsFunction = QtGui.QAction(MainWindow)
        self.actionTipsFunction.setObjectName("actionTipsFunction")
        self.actionTipsSentence = QtGui.QAction(MainWindow)
        self.actionTipsSentence.setObjectName("actionTipsSentence")
        self.actionStripOptions = QtGui.QAction(MainWindow)
        self.actionStripOptions.setObjectName("actionStripOptions")
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionTips)
        self.menuHelp.addAction(self.actionAbout)
        self.menuSection.addAction(self.actionAddSection)
        self.menuSection.addAction(self.actionRemoveSection)
        self.menuSection.addAction(self.actionUpdateSection)
        self.menuSection.addSeparator()
        self.menuSection.addAction(self.actionTipsSection)
        self.menuSubSection.addAction(self.actionAddSubSection)
        self.menuSubSection.addAction(self.actionRemoveSubSection)
        self.menuSubSection.addAction(self.actionUpdateSubSection)
        self.menuSubSection.addSeparator()
        self.menuSubSection.addAction(self.actionTipsSubSection)
        self.menuFunction.addAction(self.actionAddFunction)
        self.menuFunction.addAction(self.actionRemoveFunction)
        self.menuFunction.addAction(self.actionUpdateFunction)
        self.menuFunction.addSeparator()
        self.menuFunction.addAction(self.actionTipsFunction)
        self.menuSentence.addAction(self.actionAddSentence)
        self.menuSentence.addAction(self.actionRemoveSentence)
        self.menuSentence.addAction(self.actionUpdateSentence)
        self.menuSentence.addSeparator()
        self.menuSentence.addAction(self.actionTipsSentence)
        self.menuSettings.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSection.menuAction())
        self.menubar.addAction(self.menuSubSection.menuAction())
        self.menubar.addAction(self.menuFunction.menuAction())
        self.menubar.addAction(self.menuSentence.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSaveAs)
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(
            self.pushButtonClearLog,
            QtCore.SIGNAL("clicked(bool)"),
            self.textEditLogView.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "Sci Corpus ",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSentenceRemove.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "-",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelReference.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Reference",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSentenceUpdate.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Update",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSentenceAdd.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "+",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Sentence",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.textEditSentence.setHtml(
            QtGui.QApplication.translate(
                "MainWindow",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "File",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "Help",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.menuSection.setTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "Section",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.menuSubSection.setTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "Sub Section",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.menuFunction.setTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "Function",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.menuSentence.setTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "Sentence",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "Settings",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetSection.setWindowTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "  Section",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSectionRemove.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "-",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSectionAdd.setStatusTip(
            QtGui.QApplication.translate(
                "MainWindow",
                "Add a new  section",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSectionAdd.setWhatsThis(
            QtGui.QApplication.translate(
                "MainWindow",
                "<html><head/><body><p>This function add a new section when you write it in line edit field and than press add button.</p></body></html>",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSectionAdd.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "+",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSectionUpdate.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Update",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Selected:",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelSelectedSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "#",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Displayed: ",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelDisplayedSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "#",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Total:",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelTotalSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "#",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetSubSection.setWindowTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "  Sub Section",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSubSectionAdd.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "+",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSubSectionRemove.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "-",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSubSectionUpdate.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Update",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Selected: ",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelSelectedSubSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "#",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Displayed:",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelDisplayedSubSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "#",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Total:",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelTotalSubSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "#",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetFunction.setWindowTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "  Function",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFunctionAdd.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "+",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFunctionRemove.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "-",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFunctionUpdate.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Update",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Selected: ",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelSelectedFunction.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "#",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Displayed: ",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelDisplayedFunction.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "#",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Total: ",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelTotalFunction.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "#",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetTableView.setWindowTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "  Table View",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.checkBoxReference.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Reference",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.checkBoxStrip.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Strip Sentence",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.checkBoxSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Section",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.checkBoxFunction.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Function",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.checkBoxSubSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Sub Section",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.checkBoxSentence.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Sentence",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Selected: ",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelSelectedSentence.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "#",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Displayed: ",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelDisplayedSentence.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "#",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Total:",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelTotalSentence.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "#",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetSentence.setSortingEnabled(True)
        self.toolBar.setWindowTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "toolBar",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetLogView.setWindowTitle(
            QtGui.QApplication.translate(
                "MainWindow",
                "  Log View",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonClearLog.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Clear",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Open",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Save",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Save As",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Print to PDF",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Close",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Quit",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "About",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionTips.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Tips",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionAddSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Add",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Remove",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Update",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionAddSubSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Add",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveSubSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Remove",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateSubSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Update",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionAddFunction.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Add",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveFunction.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Remove",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateFunction.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Update",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionAddSentence.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Add",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveSentence.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Remove",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateSentence.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Update",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Import ...",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Export ...",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionTipsSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Tips",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionTipsSubSection.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Tips",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionTipsFunction.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Tips",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionTipsSentence.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Tips",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionStripOptions.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Strip Options",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Preferences",
                None,
                QtGui.QApplication.UnicodeUTF8))

from sci_corpus.ui import sci_corpus_resource_rc
