# -*- coding: utf-8 -*-
"""Created on May 18, 2012.

@author: Daniel Pizetta <daniel.pizetta@usp.br>

"""

from PySide.QtCore import *
from PySide.QtGui import *
from sci_corpus.ui import list_editor_dlg


class ListEditor(QDialog):

    """Editor for parameter list."""

    def __init__(self, name, list, parent=None):
        super(ListEditor, self).__init__(parent)
        self.ui = list_editor_dlg.Ui_Dialog()
        self.ui.setupUi(self)

        self.list = list
        self.item = None
        self.setWindowTitle('List Editor: ' + str(name))
        self.ui.listWidget.insertItem(0, QListWidgetItem('New'))
        self.ui.listWidget.itemDoubleClicked.connect(
            self.openPersistentEditorItem)
        self.ui.listWidget.itemChanged.connect(self.closePersistentEditorItem)
        self.ui.listWidget.setMovement(QListView.Free)
        self.ui.pushButtonAdd.clicked.connect(lambda: self.add())
        self.ui.pushButtonRemove.clicked.connect(lambda: self.remove())
        self.populateList()

    def openPersistentEditorItem(self, item):
        self.item = item
        self.ui.listWidget.openPersistentEditor(self.item)

    def closePersistentEditorItem(self):
        if self.item is not None:
            self.ui.listWidget.closePersistentEditor(self.item)

    def accept(self):
        self.saveValues()
        QDialog.accept(self)

    def reject(self):
        QDialog.reject(self)

    def add(self):
        self.ui.listWidget.insertItem(
            self.ui.listWidget.currentRow() + 1,
            QListWidgetItem('New'))

    def remove(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def populateList(self):
        if self.list != []:
            self.ui.listWidget.clear()
        for row, value in enumerate(self.list):
            item = QListWidgetItem(str(value))
            self.ui.listWidget.addItem(item)

    def savedValues(self):
        return self.list

    def saveValues(self):
        self.list = []
        for row in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(row)
            self.list.append(item.text())
