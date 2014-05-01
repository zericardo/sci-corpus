#! python
# -*- coding: utf-8 -*-

"""
Starting screen.

Author: Daniel Pizetta <daniel.pizetta@usp.br>
Date: 28/04/2014
"""

from PySide.QtGui import QDialog
from PySide import QtCore
import ui.start_dlg_ui 
from time import sleep

class StartDialog(QDialog):
    """
    Starting screen class.
    """
    logSig = QtCore.Signal(str)
    def __init__(self, parent=None, delay=0.3):
        """
        Contructor
        """
        super(StartDialog, self).__init__(parent)
        self.ui = ui.start_dlg_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.SplashScreen | \
                            QtCore.Qt.WindowStaysOnTopHint |\
                            QtCore.Qt.FramelessWindowHint |\
                            QtCore.Qt.WindowTitleHint)
        
        self.delay = delay
        
        self.ui.progressBar.setRange(0,100)
        self.ui.progressBar.setValue(0)
        self.informationProgress("Starting")

    def version(self, version):
        """
        Set version to show.
        
        Parameters
            version : int/float/str
        """
        self.ui.labelVersion.setText("V."+str(version))
        
    def year(self, year):
        """
        Set year to show.
        
        Parameters
            year : int/str
        """
        self.ui.labelYear.setText(str(year))
        
    def updateProgress(self, value=0):
        """
        Update progress bar with value (0-100).
        
        Parameters
            value : int (0-100)
        """
        self.ui.progressBar.setValue(value)
        sleep(self.delay)
        
    def informationProgress(self, text=""):
        """
        Update string that shows information about progress.
        
        Parameters
            text : str
        """
        self.logSig.emit(str(text))
        self.ui.labelInformationProgress.setText(str(text)+" ...")

