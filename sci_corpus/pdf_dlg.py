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
from sci_corpus.ui import pdf_dlg_ui
from PySide.QtGui import QDialog, QFileDialog

class PDFDialog(QDialog):

    """PDF dialog."""

    def __init__(self, preferences, workspace,  parent=None):
        """Contructor."""

        super(PDFDialog, self).__init__(parent)
        self.ui = pdf_dlg_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.preferences = preferences
        self.workspace = workspace

        # Signals
        self.ui.pushButtonOk.clicked.connect(self.accept)
        self.ui.pushButtonCancel.clicked.connect(self.reject)
        self.ui.pushButtonPath.clicked.connect(self.searchPath)
        
        path = os.path.join(str(self.workspace),'MySciCorpus.pdf')
        path = os.path.abspath(path)
        self.ui.lineEditPath.setText(path)
        
        try:
            self.ui.lineEditTitle.setText(self.preferences['title'])
            self.ui.lineEditAuthor.setText(self.preferences['author'])
            self.ui.textEditDescription.setText(self.preferences['description'])
            self.ui.radioButtonDim.setChecked(self.preferences['pdf']['dim'])
            self.ui.radioButtonReplace.setChecked(self.preferences['pdf']['replace'])
            self.ui.spinBoxSize.setValue(self.preferences['pdf']['size'])
            self.ui.checkBoxDate.setChecked(self.preferences['pdf']['date'])
        except Exception:
            pass

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
        
        while str(self.ui.lineEditPath.text()) == '':
            self.searchPath()

        self.preferences['title'] = self.ui.lineEditTitle.text()
        self.preferences['author'] = str(self.ui.lineEditAuthor.text())
        self.preferences['description'] = str(self.ui.textEditDescription.toPlainText())
        
        self.preferences['pdf'] = {}
        self.preferences['pdf']['path'] = str(self.ui.lineEditPath.text())
        
        self.preferences['pdf']['dim'] = self.ui.radioButtonDim.isChecked()
        self.preferences['pdf']['replace'] = self.ui.radioButtonReplace.isChecked()
        
        self.preferences['pdf']['font'] = self.ui.comboBoxFont.currentText()
        self.preferences['pdf']['size'] = self.ui.spinBoxSize.value()
        
        self.preferences['pdf']['date'] = self.ui.checkBoxDate.isChecked()

        QDialog.accept(self)

    def reject(self):
        """Reject event."""
        
        QDialog.reject(self)
