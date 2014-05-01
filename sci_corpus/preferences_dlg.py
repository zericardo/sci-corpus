#! python
# -*- coding: utf-8 -*-

"""
Starting screen.

Author: Daniel Pizetta <daniel.pizetta@usp.br>
Date: 28/04/2014
"""

from PySide.QtGui import QDialog
import ui.start_dlg_ui 


class PreferencesDialog(QDialog):
    """
    Starting screen class.
    """

    def __init__(self, parent=None):
        """
        Contructor
        """
        super(PreferencesDialog, self).__init__(parent)
        self.ui = ui.start_dlg_ui.Ui_Preferences()
        self.ui.setupUi(self)


