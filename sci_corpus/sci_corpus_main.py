#! python
# -*- coding: utf-8 -*-

"""
Graphical interface for sci-corpus program.
Author: Daniel Pizetta <daniel.pizetta@usp.br>
Date: 04/04/2014

This script provides a graphical interface for sci-corpus program standalone.
"""

from PySide.QtGui import QApplication,  QMainWindow,  QMessageBox,  QListWidgetItem
from PySide.QtCore import WA_DeleteOnClose
from sci_corpus.ui import main_window

if __name__ == '__main__':

    app = QApplication('Sci Corpus')
    main_window = main_window.MainWindow()
    main_window.show()
    exit(app.exec_())

class MainWindow(QMainWindow):
    def __init__(self, argv=None, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setAttribute(WA_DeleteOnClose)
        self.ui = main_window.MainWindow()
        self.ui.setupUi(self)
        # fazer igual pra todos pushbuttom e action
        
        # file
        
        self.ui.actionOpen.clicked.connect(self.openFile)
        self.ui.actionSave.clicked.connect(self.saveFile)
        self.ui.actionSaveAs.clicked.connect(self.saveFileAs)
        self.ui.actionPrint.clicked.connect(self.printFile)
        self.ui.actionClose.clicked.connect(self.closeFile)
        self.ui.actionQuit.clicked.connect(self.quitFile)
        self.ui.actionAbout.clicked.connect(self.about)
        self.ui.actionTips.clicked.connect(self.tips)
        
        # section
        self.ui.pushButtonAddSection.clicked.connect(self.addSection)
        self.ui.pushButtonRemoveSection.clicked.connect(self.removeSection)
        self.ui.pushButtonUpdateSection.clicked.connect(self.updateSection)
        self.ui.actionAddSection.clicked.connect(self.addSection)
        self.ui.actionRemoveSection.clicked.connect(self.removeSection)
        self.ui.actionUpdateSection.clicked.connect(self.updateSection)
        

        
        # subsection
        self.ui.pushButtonAddSubsection.clicked.connect(self.addSubsection)
        self.ui.pushButtonRemoveSubsection.clicked.connect(self.removeSubsection)
        self.ui.pushButtonUpdateSubsection.clicked.connect(self.updateSubsection)
        self.ui.actionAddSubSection.clicked.connect(self.addSubSection)
        self.ui.actionRemoveSubSection.clicked.connect(self.removeSubSection)
        self.ui.actionUpdateSubSection.clicked.connect(self.updateSubSection)
        
        # how to
        self.ui.pushButtonAddHowTo.clicked.connect(self.addHowTo)
        self.ui.pushButtonRemoveHowTo.clicked.connect(self.removeHowTo)
        self.ui.pushButtonUpdateHowTo.clicked.connect(self.updateHowTo)
        self.ui.actionAddHowTo.clicked.connect(self.addHowTo)
        self.ui.actionRemoveHowTo.clicked.connect(self.removeHowTo)
        self.ui.actionUpdateHowTo.clicked.connect(self.updateHowTo)
        
        #Sentence
        self.ui.pushButtonAddSentence.clicked.connect(self.addSentence)
        self.ui.pushButtonRemoveSentence.clicked.connect(self.removeSentence)
        self.ui.pushButtonUpdateSentence.clicked.connect(self.updateSentence)
        self.ui.actionAddSentence.clicked.connect(self.addSentence)
        self.ui.actionRemoveSentence.clicked.connect(self.removeSentence)
        self.ui.actionUpdateSentence.clicked.connect(self.updateSentence)
        
        
    def addSection(self):
        """
        Add a new section. fazer add, remove, update para todos
        """
        section = self.ui.lineEditSection.text()
        #chama metodo tiago inserir secao (section)
        self.updateSectionView()
        
    def removeSection(self):
        """
        """
        section = self.ui.lineEditSection.text()
        
        
    def updateSection(self):
        """
        """
        
    def updateSectionView(self):
        """
        """
        # chama metodo do tiago que retorna lista de secoes
        sections = [] 
        self.ui.listWidgetSection.clear()
        for row, value in enumerate(sections):
            item = QListWidgetItem(str(value))
            self.ui.listWidgetSection.addItem(item)

        
    def about(self):
        """
        Show the dialog About.
        """
        QMessageBox.about(
                          self,
                          self.tr('Sci Corpus'),
                          self.tr(''))
                          
    def close(self):
        answer = QMessageBox.question(  self, 
                                         self.tr('Close'),
                                         self.tr('Do you want to exit Sci Corpus?'),
                                         QMessageBox.Yes | QMessageBox.No, 
                                         QMessageBox.No)
        if answer == QMessageBox.Yes:
            return True
        else:
            return False
