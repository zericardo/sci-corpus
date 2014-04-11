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
        
        #Section
        
        self.ui.pushButtonAddSection.clicked.connect(self.addSection)
        self.ui.pushButtonRemoveSection.clicked.connect(self.removeSection)
        self.ui.pushButtonUpdateSection.clicked.connect(self.updateSection)
        self.ui.actionAddSection.clicked.connect(self.addSection)
        self.ui.actionRemoveSection.clicked.connect(self.removeSection)
        self.ui.actionUpdateSection.clicked.connect(self.updateSection)
        self.ui.listWidgetSection.doubleClicked.connect(self.tipsSection)

        #Subsection
        
        self.ui.pushButtonAddSubsection.clicked.connect(self.addSubsection)
        self.ui.pushButtonRemoveSubsection.clicked.connect(self.removeSubsection)
        self.ui.pushButtonUpdateSubsection.clicked.connect(self.updateSubsection)
        self.ui.actionAddSubSection.clicked.connect(self.addSubSection)
        self.ui.actionRemoveSubSection.clicked.connect(self.removeSubSection)
        self.ui.actionUpdateSubSection.clicked.connect(self.updateSubSection)
        self.ui.listWidgetSubSection.doubleClicked.connect(self.tipsSubSection)


        #Function
        
        self.ui.pushButtonAddFunction.clicked.connect(self.addFunction)
        self.ui.pushButtonRemoveFunction.clicked.connect(self.removeFunction)
        self.ui.pushButtonUpdateFunction.clicked.connect(self.updateFunction)
        self.ui.actionAddFunction.clicked.connect(self.addFunction)
        self.ui.actionRemoveFunction.clicked.connect(self.removeFunction)
        self.ui.actionUpdateFunction.clicked.connect(self.updateFunction)
        self.ui.listWidgetFunction.doubleClicked.connect(self.tipsFunction)

        
        #Sentence
        
        self.ui.pushButtonAddSentence.clicked.connect(self.addSentence)
        self.ui.pushButtonRemoveSentence.clicked.connect(self.removeSentence)
        self.ui.pushButtonUpdateSentence.clicked.connect(self.updateSentence)
        self.ui.actionAddSentence.clicked.connect(self.addSentence)
        self.ui.actionRemoveSentence.clicked.connect(self.removeSentence)
        self.ui.actionUpdateSentence.clicked.connect(self.updateSentence)
        self.ui.listWidgetSentence.doubleClicked.connect(self.tipsSentence)

       
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
        if section != '':
            section = self.ui.lineEditSection.text()
        else: 
            if self.removeQuestion("section",section) == QMessageBox.Yes:
                # chama função remove Tiago
        
        
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
    # Subsection methods
    # -----------------------------------------------------------------------

    def addSubsection(self):
        """
        Add a new Subsection
        """
        
    def removeSubsection(self, subsection=''):
        """
        Remove one subsection
        """
        if subsection != '':
            subsection = self.ui.lineEditSection.text()
        else: 
            if self.removeQuestion("subsection",subsection) == QMessageBox.Yes:
                # chama função remove Tiago

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
    # Function methods
    # -----------------------------------------------------------------------

    def addFunction(self):
        """
        Adds a new function.
        """
        
    def removeFunction(self, function=''):
        """
        Removes a function.
        """
        if function != '':
            section = self.ui.lineEditSection.text()
        else: 
            if self.removeQuestion("function",function) == QMessageBox.Yes:
                # chama função remove Tiago

    def updateFunction(self):
        """
        Updates a function.
        """

    def updateFunctionView(self):
        """
        Updates a function view.
        """

    def tipsFunction(self):
        """
        Show tips for function.
        """

    # -----------------------------------------------------------------------
    # Sentence methods
    # -----------------------------------------------------------------------

    def addSentence(self):
        """
        Adds a new sentence.
        """
        
    def removeSentence(self, sentence=''):
        """
        Removes a sentence.
        """
        if sentence != '':
            section = self.ui.lineEditSection.text()
        else: 
            if self.removeQuestion("sentence",sentence) == QMessageBox.Yes:
                # chama função remove Tiago

    def updateSentence(self):
        """
        Updates a sentence.
        """

    def updateSentenceView(self):
        """
        Updates a sentence view.
        """

    def tipsSentence(self):
        """
        Show tips for sentence.
        """ 

    # -----------------------------------------------------------------------
    # File methods
    # -----------------------------------------------------------------------
       
        def openFile(self):
            '''
            Opens a new file.
            '''
            
            path = QFileDialog.getOpenFileName(self,
                                               self.tr('Open File'),
                                               self.tr(self.container.path))

            if path != '':
                self.conteiner.read_(path)

        def saveFile(self):
            '''
            Saves the file that is being used.
            '''
            self.container.write_()

        def saveFileAs(self):
            '''
            Saves a new file
            '''
            
            path = QFileDialog.getSaveFileName(self,
                                               self.tr('Save As'),
                                               self.tr(self.container.path))
            if path != '':
                self.container.write_(path)
            
            
        def printFile(self):
            '''
            Generates a PDF file with all sentences included in database.
            '''


    # -----------------------------------------------------------------------
    # Application methods
    # -----------------------------------------------------------------------

    def about(self):
        """
        About shows the main information about the application.
        """
        QMessageBox.about(self,
                          self.tr('About Sci Corpus'),
                          self.tr('This software is a corpus manager,\
                                   that allows you to trainer.\
                                   For more information, please, \
                                   visite the page: xxx.xxx.xxx. \
                                   Version:{}')).format(__version__)
    
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
            return True
        else:
            return False

    def tips(self):
        '''
        Show tips about aplication
        '''

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
                self.container.write_()
                self.container.close_()
            elif answer == QMessageBox.No:
                self.container.close_()
        else:
            self.container.close_()

    def removeQuestion(self, what='', who=''):
        """
        Removes a section item
        """
        return QMessageBox.question(self,
                                    self.tr('Remove'),
                                    self.tr('Do you want to remove item {} from {}?'.format(who, what)),
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)

    def updateQuestion(self, section=([], []), subsection=([], []), function=([], [])):
        """
        Updates a section item
        """
        return QMessageBox.question(self,
                                    self.tr('Update'),
                                    self.tr('Do you want to update item {} to {} in {}?'.format(oldWho,newWho,what)),
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)
