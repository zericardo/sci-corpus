#! python
# -*- coding: utf-8 -*-

"""
Graphical interface for sci-corpus program.
Author: Daniel Pizetta <daniel.pizetta@usp.br>
Date: 04/04/2014

This script provides a graphical interface for sci-corpus program standalone.
"""

from PySide.QtGui import QApplication
from sci_corpus.ui import main_window

if __name__ == '__main__':
    
    app = QApplication('Personal Corpora Trainner')
    main_window = main_window.MainWindow()
    main_window.show()
    exit(app.exec_())

    def aboutToRM(self):
        """
        Show the dialog About.
        """
        QMessageBox.about(
                          self,
                          self.tr('About ToRM IDE'),
                          self.tr('<h2>ToRM IDE {} </h2>'
                                  '<p>Copyright &copy; CIERMag'
                                  '<p>ToRM IDE is a Integrated Development Environment '
                                  'for pulse sequences in Resonance Magnetic.').format(__version__))
    def closeAll(self):
        answer = QMessageBox.question(  self, 
                                         self.tr('Close'),
                                         self.tr('Do you want to exit ToRM IDE?'),
                                         QMessageBox.Yes | QMessageBox.No, 
                                         QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.project.closeAll()
            return True
        else:
            return False
