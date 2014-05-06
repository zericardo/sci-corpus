#! python
# -*- coding: utf-8 -*-

"""
Preference dialog.

Author: Daniel Pizetta <daniel.pizetta@usp.br>
Date: 01/05/2014

"""

from PySide.QtGui import QDialog, QFileDialog
import ui.preferences_dlg_ui
import os


class PreferencesDialog(QDialog):

    """Preferences dialog."""

    def __init__(self, preferences, parent=None):
        """Contructor."""
        super(PreferencesDialog, self).__init__(parent)
        self.ui = ui.preferences_dlg_ui.Ui_Preferences()
        self.ui.setupUi(self)
        self.preferences = preferences

        self.ui.pushButtonOk.clicked.connect(self.accept)
        self.ui.pushButtonCancel.clicked.connect(self.reject)
        self.ui.pushButtonWorkspace.clicked.connect(self.searchWorkspace)

        index = self.ui.comboBoxTheme.findText(self.preferences['theme'])
        self.ui.comboBoxTheme.setCurrentIndex(index)
        index = self.ui.comboBoxMarker.findText(self.preferences['marker'])
        self.ui.comboBoxMarker.setCurrentIndex(index)
        index = self.ui.comboBoxReplace.findText(
            self.preferences['replace_where'])
        self.ui.comboBoxReplace.setCurrentIndex(index)
        self.ui.lineEditReplaceBy.setText(str(self.preferences['replace_by']))
        self.ui.lineEditWorkspace.setText(str(self.preferences['workspace']))
        self.ui.checkBoxOpenLast.setChecked(self.preferences['open_last'])
        self.ui.checkBoxCreateDir.setChecked(True)
        self.ui.checkBoxCreateDir.clicked.connect(self.createDir)

        self.createDir()

    def createDir(self):
        """Create a directory for workspace."""
        create = self.ui.checkBoxCreateDir.isChecked()
        path = self.ui.lineEditWorkspace.text()
        if create:
            path = os.path.join(os.path.abspath(path), "Sci Corpus")
        else:
            path = os.path.splitext(os.path.dirname(path))[0]
        self.ui.lineEditWorkspace.setText(path)

    def searchWorkspace(self):
        """Seach a workspace."""
        path = QFileDialog.getExistingDirectory(
            self,
            self.tr('Choose a workspace for your Sci Corpus'),
            self.tr(
                self.preferences['workspace']))
        if path != '':
            self.createDir()
            self.preferences['workspace'] = os.path.abspath(path)
            self.ui.lineEditWorkspace.setText(os.path.abspath(path))

    def accept(self):
        """Accept event."""
        self.preferences['theme'] = self.ui.comboBoxTheme.currentText()
        self.preferences['marker'] = str(self.ui.comboBoxMarker.currentText())
        self.preferences['replace_where'] = str(
            self.ui.comboBoxReplace.currentText())
        self.preferences['replace_by'] = str(self.ui.lineEditReplaceBy.text())
        self.preferences['workspace'] = str(self.ui.lineEditWorkspace.text())
        self.preferences['open_last'] = self.ui.checkBoxOpenLast.isChecked()

        #@TODO: put the try block here
        if not os.path.exists(self.preferences['workspace']):
            os.makedirs(self.preferences['workspace'])

        print self.preferences
        QDialog.accept(self)

    def reject(self):
        """Reject event."""
        QDialog.reject(self)
