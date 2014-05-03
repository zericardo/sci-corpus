#! python
# -*- coding: utf-8 -*-

"""
.. module:: start_dlg
   :platform: Unix, Windows
   :synopsis: Starting screen module.
   
.. moduleauthor:: Daniel Pizetta <daniel.pizetta@usp.br>
"""

from PySide.QtGui import QDialog
from PySide.QtCore import Signal, Qt
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
        
        Parameters:
        -----------
        parent: QWidget
                Parent widget.
        delay: float/int
               Minimum time delay, in seconds, between each progress bar update.
        """
        super(StartDialog, self).__init__(parent)
        self.ui = ui.start_dlg_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui.progressBar.setRange(0,100)
        self.ui.progressBar.setValue(0)
        
        self.setWindowFlags(QtCore.Qt.SplashScreen | \
                            QtCore.Qt.WindowStaysOnTopHint |\
                            QtCore.Qt.FramelessWindowHint |\
                            QtCore.Qt.WindowTitleHint)
        self.__delay = delay
        self.informationProgress("Starting")


    def version(self, version):
        """
        Sets version to show.
        
        Parameters:
        -----------
        version: int/float/str
                 Program version to be shown.
        """
        self.ui.labelVersion.setText("V."+str(version))
        
        
    def year(self, year):
        """
        Sets year to show.
        
        Parameters:
        -----------
        year: int/str
              Year of the program version.
        """
        self.ui.labelYear.setText(str(year))
        
        
    def updateProgress(self, value=0):
        """
        Update progress bar with value (0-100).
        
        Parameter:
        ----------
        value: int (0-100)
               Update the progress bar with this value. Must be between 0-100.
        """
        self.ui.progressBar.setValue(value)
        sleep(self.__delay)
        
        
    def informationProgress(self, text=""):
        """
        Update string that shows information about progress.
        
        Parameters:
        -----------
        text: str
              A text informing the progress, its current activity.
        """
        self.logSig.emit(str(text))
        self.ui.labelInformationProgress.setText(str(text)+" ...")

