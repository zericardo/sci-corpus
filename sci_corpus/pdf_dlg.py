#! python
# -*- coding: utf-8 -*-

"""
.. module:: pdf_dlg
   :platform: Unix, Windows
   :synopsis: Graphical interface PDF setup.

.. moduleauthor:: Daniel Pizetta <daniel.pizetta@usp.br>

Date: 01/05/2014 #@TODO: how to put this?

This script provides a graphical interface for PDF setup.

"""

import os
import ui.pdf_dlg_ui
from PySide.QtGui import QDialog, QFileDialog

class PDFDialog(QDialog):

    """PDF dialog."""

    def __init__(self, preferences,  parent=None):
        """Contructor."""

        super(PDFDialog, self).__init__(parent)
        self.ui = ui.preferences_dlg_ui.Ui_Preferences()
        self.ui.setupUi(self)
        self.preferences = preferences

        # Signals
        self.ui.pushButtonOk.clicked.connect(self.accept)
        self.ui.pushButtonCancel.clicked.connect(self.reject)
        self.ui.pushButtonPath.clicked.connect(self.searchPath)

        self.ui.lineEditPath.setText(str(self.preferences['workspace']))

    def searchPath(self):
        """Seach a workspace."""

        path = QFileDialog.getSaveFileName(
            self,
            self.tr('Path to save PDF'),
            self.tr(self.workspace), 
            self.tr('(*.pdf)'))[0]
        if path != '':
            path = os.path.abspath(path)
            self.ui.lineEditPath.setText(os.path.abspath(path))

    def accept(self):
        """Accept event."""

        self.preferences['title'] = self.ui.lineEditTitle.text()
        self.preferences['author'] = str(self.ui.lineEditAuthor.text())
        self.preferences['description'] = str(self.ui.textEditDescription.text())
        self.preferences['pdf']['replace'] = str(self.ui.radioButtonReplace.isChecked())
        self.preferences['pdf']['dim'] = str(self.ui.radioButtonReplace.isChecked())
        self.preferences['pdf']['font'] = str(self.ui.radioButtonReplace.isChecked())
        self.preferences['pdf']['size'] = str(self.ui.spinBox.value())
        self.preferences['pdf']['date'] = str(self.ui.checkBoxDate.isChecked())

        QDialog.accept(self)

    def reject(self):
        """Reject event."""
        
        QDialog.reject(self)
