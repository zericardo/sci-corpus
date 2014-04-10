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
from sci_corpus import container

__version__='0.1.B'

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
        
        self.container = container.Container()
        
        # file
        
        self.ui.actionOpen.clicked.connect(self.openFile)
        self.ui.actionSave.clicked.connect(self.saveFile)
        self.ui.actionSaveAs.clicked.connect(self.saveFileAs)
        self.ui.actionPrint.clicked.connect(self.printFile)
        self.ui.actionClose.clicked.connect(self.closeFile)
        
        # application
        
        self.ui.actionQuit.clicked.connect(self.quit)
        self.ui.actionAbout.clicked.connect(self.about)
        self.ui.actionTips.clicked.connect(self.tips)
        
        # section
        
        self.ui.pushButtonAddSection.clicked.connect(self.addSection)
        self.ui.pushButtonRemoveSection.clicked.connect(self.removeSection)
        self.ui.pushButtonUpdateSection.clicked.connect(self.updateSection)
        self.ui.actionAddSection.clicked.connect(self.addSection)
        self.ui.actionRemoveSection.clicked.connect(self.removeSection)
        self.ui.actionUpdateSection.clicked.connect(self.updateSection)
        # ZE POE UM DESSES TBM EM TODOS
        self.ui.listWidgetSection.doubleClicked.connect(self.tipsSection)

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
        
        # sentence
        
        self.ui.pushButtonAddSentence.clicked.connect(self.addSentence)
        self.ui.pushButtonRemoveSentence.clicked.connect(self.removeSentence)
        self.ui.pushButtonUpdateSentence.clicked.connect(self.updateSentence)
        self.ui.actionAddSentence.clicked.connect(self.addSentence)
        self.ui.actionRemoveSentence.clicked.connect(self.removeSentence)
        self.ui.actionUpdateSentence.clicked.connect(self.updateSentence)
       
    # -----------------------------------------------------------------------
    # Section methods
    # -----------------------------------------------------------------------
        
    def addSection(self):
        """
        Add a new section.
        """
        # fazer add, remove, update para todos
        section = self.ui.lineEditSection.text()
        #chama metodo tiago inserir secao (section)
        self.updateSectionView()
        
        
    def removeSection(self, section=''):
        """
        Remove a section.
        """
        section = self.ui.lineEditSection.text()
        
        
    def updateSection(self, (old_section, new_section)):
        """
        Updates old section with new section.
        """
        
    def updateSectionView(self):
        """
        Updates section view.
        """
        # chama metodo do tiago que retorna lista de secoes
        sections = [] 
        self.ui.listWidgetSection.clear()
        for row, value in enumerate(sections):
            item = QListWidgetItem(str(value))
            self.ui.listWidgetSection.addItem(item)
            
            
    def tipsSection(self):
        """
        Show tips for the section.
        """    
        QMessageBox.information(self, 
                                self.tr('Section Tips'),
                                self.tr('Do you want to exit Sci Corpus?'),
                                QMessageBox.Ok)
                                
    # -----------------------------------------------------------------------
    # Sub section methods
    # -----------------------------------------------------------------------

    def addSubsection(self):
        """
        Add a new Subsection
        """
        
    def removeSubsection(self, subsection=''):
        """
        Remove one subsection
        """

    def updateSubsection(self):
        """
        Updates one subsection
        """

    def updateSubsectionView(self):
        """
        Updates subsection view
        """

    def tipsSubsection(self):
        """
        Show tips for Subsection
        """

    # -----------------------------------------------------------------------
    # How to methods
    # -----------------------------------------------------------------------

    def addHowTo(self):
        """
        Add a new How To
        """
        
    def removeHowTo(self, howTo=''):
        """
        Remove one How To
        """

    def updateHowTo(self):
        """
        Updates one How To
        """

    def updateHowToView(self):
        """
        Updates How To view
        """

    def tipsHowTo(self):
        """
        Show tips for How To
        """

    # -----------------------------------------------------------------------
    # Application methods
    # -----------------------------------------------------------------------


    def about(self):
        """
        About shows the main information about the application.
        """
        QMessageBox.about(
                          self,
                          self.tr('About Sci Corpus'),
                          self.tr('This software is a corpus manager,\
                                   that allows you to trainer.\
                                   For more information, please, \
                                   visite the page: xxx.xxx.xxx. \
                                   Version:{}')).format(__version__)
                                   
    def saveFileAs2():
        """http://qt-project.org/doc/qt-4.8/qfiledialog.html"""
        
        path = QFileDialog.getSaveFileName(self,
                                           self.tr('Save As'),
                                           self.tr(self.container.path))
        if path != '':
            self.container.write(path)
        
    
    def closeFile(self):
        """
        Closes current file.
        """
        
        if self.container.isModified:
            answer = QMessageBox.question(self, 
                                      self.tr('Save'),
                                      self.tr('Do you want to save the current work?'),
                                      QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, 
                                      QMessageBox.Yes)
                                      
            if answer == QMessageBox.Yes:
                self.container.write()
                self.container.close()
            elif answer == QMessageBox.No:
                self.container.close()
        else:
            self.container.close()

    def quit(self):
        """
        Quit current application.
        """
        answer = QMessageBox.question(self, 
                                      self.tr('Quit'),
                                      self.tr('Do you want to exit Sci Corpus?'),
                                      QMessageBox.Yes | QMessageBox.No, 
                                      QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.fileClose()

            return True
        else:
            return False
