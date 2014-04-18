#! python
# -*- coding: utf-8 -*-

"""
Graphical interface for sci-corpus program.
Author: Daniel Pizetta <daniel.pizetta@usp.br>
        Tiago de Campos <tiago.campo@usp.br>
Date: 04/04/2014

This script provides a graphical interface for sci-corpus program standalone.
"""

from PySide.QtGui import QApplication,  QMainWindow,  QMessageBox,  QListWidgetItem
from PySide.QtGui import QFileDialog,  QTableWidgetItem
import container
from ui import main_window_ui

__version__='0.1.B'



class MainWindow(QMainWindow):
    def __init__(self, argv=None, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.container = container.ContainerDB()
        
        # File
        
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionSaveAs.triggered.connect(self.saveFileAs)
        self.ui.actionPrint.triggered.connect(self.printFile)
        self.ui.actionImport.triggered.connect(self.importFile)
        self.ui.actionExport.triggered.connect(self.exportFile)
        self.ui.actionClose.triggered.connect(self.closeFile)
        
        # Application
        
        self.ui.actionQuit.triggered.connect(self.quit)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionTips.triggered.connect(self.tips)
        
        # Section
        
        self.ui.pushButtonSectionAdd.clicked.connect(self.addSection)
        self.ui.pushButtonSectionRemove.clicked.connect(self.removeSection)
        self.ui.pushButtonSectionUpdate.clicked.connect(self.updateSection)
        
        self.ui.actionAddSection.triggered.connect(self.addSection)
        self.ui.actionRemoveSection.triggered.connect(self.removeSection)
        self.ui.actionUpdateSection.triggered.connect(self.updateSection)
        self.ui.actionTipsSection.triggered.connect(self.tipsSection)
        
        self.ui.listWidgetSection.doubleClicked.connect(self.tipsSection)
        self.ui.listWidgetSection.itemSelectionChanged.connect(self.updateSubSectionView)

        # Subsection
        
        self.ui.pushButtonSubSectionAdd.clicked.connect(self.addSubSection)
        self.ui.pushButtonSubSectionRemove.clicked.connect(self.removeSubSection)
        self.ui.pushButtonSubSectionUpdate.clicked.connect(self.updateSubSection)
        
        self.ui.actionAddSubSection.triggered.connect(self.addSubSection)
        self.ui.actionRemoveSubSection.triggered.connect(self.removeSubSection)
        self.ui.actionUpdateSubSection.triggered.connect(self.updateSubSection)
        self.ui.actionTipsSubSection.triggered.connect(self.tipsSubSection)
        
        self.ui.listWidgetSubSection.doubleClicked.connect(self.tipsSubSection)
        self.ui.listWidgetSubSection.itemSelectionChanged.connect(self.updateFunctionView)

        # Function
        
        self.ui.pushButtonFunctionAdd.clicked.connect(self.addFunction)
        self.ui.pushButtonFunctionRemove.clicked.connect(self.removeFunction)
        self.ui.pushButtonFunctionUpdate.clicked.connect(self.updateFunction)
        
        self.ui.actionAddFunction.triggered.connect(self.addFunction)
        self.ui.actionRemoveFunction.triggered.connect(self.removeFunction)
        self.ui.actionUpdateFunction.triggered.connect(self.updateFunction)
        self.ui.actionTipsFunction.triggered.connect(self.tipsFunction)
        
        self.ui.listWidgetFunction.doubleClicked.connect(self.tipsFunction)
        self.ui.listWidgetFunction.itemSelectionChanged.connect(self.updateSentenceView)

        # Sentence
        
        self.ui.pushButtonSentenceAdd.clicked.connect(self.addSentence)
        self.ui.pushButtonSentenceRemove.clicked.connect(self.removeSentence)
        self.ui.pushButtonSentenceUpdate.clicked.connect(self.updateSentence)
        
        self.ui.actionAddSentence.triggered.connect(self.addSentence)
        self.ui.actionRemoveSentence.triggered.connect(self.removeSentence)
        self.ui.actionUpdateSentence.triggered.connect(self.updateSentence)
        self.ui.actionTipsSentence.triggered.connect(self.tipsSentence)
        
        self.updateSectionView()
        self.updateSubSectionView()
        self.updateFunctionView()
        self.updateSentenceView()
        
    def selectedTitles(self,  selected_items):
        """
        Return a list of selected titles.
        """
        titles = []
        for item in  selected_items:
            titles.append(str(item.text()))
        return titles  
        
    # -----------------------------------------------------------------------
    # Section methods
    # -----------------------------------------------------------------------

        
    def addSection(self):
        """
        Add a new section.
        """
        section = str(self.ui.lineEditSection.text())
        if section != '':
            #section = list(str(section))
            self.container.addDB(sect=[section])
        self.ui.listWidgetSection.clear()
        self.updateSectionView()
        self.updateSentenceView()

    def removeSection(self, section=''):
        """
        Remove a section.
        """
        if section != '':
            section = str(self.ui.lineEditSection.text())
        else: 
            if self.removeQuestion("section",section) == QMessageBox.Yes:
                print section
                self.container.remove(sect=[section])
        self.container.isModified(True)
                
    def updateSection(self, (old_section, new_section)):
        """
        Updates old section with new section.
        """
        self.container.update(section=[(old_section, new_section)])
        self.container.isModified(True)
        self.updateSectionView()
        
    def updateSectionView(self):
        """
        Updates section view.
        """
        #sections = self.container.sections()
        sections = self.container.listCategories()
        sections = sections[0]
        self.ui.listWidgetSection.clear()
        sections = sorted(sections)
        for row, value in enumerate(sections):
            item = QListWidgetItem(str(value))
            self.ui.listWidgetSection.addItem(item)
            
    def tipsSection(self):
        """
        Show tips for the section.
        """    
        QMessageBox.information(self, 
                                self.tr('Section Tips'),
                                self.tr('Sections are the main division of a scientific text.\
In summary, they are the titles of each section.'),
                                QMessageBox.Ok)
                                
    # -----------------------------------------------------------------------
    # Subsection methods
    # -----------------------------------------------------------------------
    

        
    def addSubSection(self):
        """
        Add a new Subsection
        """

        section = str(self.selectedTitles(self.ui.listWidgetSection.selectedItems())[0])
        sub_section = str(self.ui.lineEditSubSection.text())        
        if sub_section != '':
            self.container.addDB(sect=[section], subsect=[sub_section])
        self.updateSubSectionView()
        self.updateSentenceView()
        
    def removeSubSection(self, subsection=''):
        """
        Remove one subsection
        """
        if subsection != '':
            subsection = self.ui.lineEditSection.text()
        else: 
            if self.removeQuestion("subsection",subsection) == QMessageBox.Yes:
                self.container.remove(subsect=[subsection])
        self.container.isModified(True)
                
    def updateSubSection(self):
        """
        Updates one subsection
        """

    def updateSubSectionView(self):
        """
        Updates subsection view
        """
        sections = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        sections = list(sections)
        subsections = self.container.listCategories(section=sections)
        subsections = subsections[1]
        self.ui.listWidgetSubSection.clear()
        subsections = sorted(subsections)
        
        for row, value in enumerate(subsections):
            item = QListWidgetItem(str(value))
            self.ui.listWidgetSubSection.addItem(item)
            
    def tipsSubSection(self):
        """
        Show tips for Subsection
        """
        QMessageBox.information(self, 
                                self.tr('Sub Section Tips'),
                                self.tr('Sub section are a sub division of the section.\
\n\nAs an example, section Introduction has a Contextualization, Gap and Propose sub sections \
in an article.'),
                                QMessageBox.Ok)

    # -----------------------------------------------------------------------
    # Function methods
    # -----------------------------------------------------------------------

    def addFunction(self):
        """
        Adds a new function.
        """
        section = str(self.selectedTitles(self.ui.listWidgetSection.selectedItems())[0])
        sub_section = str(self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())[0])
        function = str(self.ui.lineEditFunction.text())
        
        print function
        
        if function != '':
            self.container.addDB(sect=[section], subsect=[sub_section], funct=[function])
        self.updateFunctionView()
        self.updateSentenceView()
        
    def removeFunction(self, function=''):
        """
        Removes a function.
        """
        if function != '':
            section = self.ui.lineEditSection.text()
        else: 
            if self.removeQuestion("function",function) == QMessageBox.Yes:
                self.container.remove(funct=[function])
        self.container.isModified(True)

    def updateFunction(self):
        """
        Updates a function.
        """

    def updateFunctionView(self):
        """
        Updates a function view.
        """

        sections = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        sub_sections = self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())
        sections = list(sections)
        sub_sections = list(sub_sections)
        functions = self.container.listCategories(section=sections,subsection=sub_sections)
        functions = functions[2]
        self.ui.listWidgetFunction.clear()
        functions = sorted(functions)
        
        for row, value in enumerate(functions):
            item = QListWidgetItem(str(value))
            self.ui.listWidgetFunction.addItem(item)

    def tipsFunction(self):
        """
        Show tips for function.
        """
        QMessageBox.information(self, 
                        self.tr('Function Tips'),
                        self.tr('Function explain what each sentence is.'),
                        QMessageBox.Ok)

    # -----------------------------------------------------------------------
    # Sentence methods
    # -----------------------------------------------------------------------

    def addSentence(self):
        """
        Adds a new sentence.
        """
        section = str(self.selectedTitles(self.ui.listWidgetSection.selectedItems())[0])
        sub_section = str(self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())[0])
        function = str(self.selectedTitles(self.ui.listWidgetFunction.selectedItems())[0])
        sentence = str(self.ui.textEditSentence.toPlainText())
        reference = str(self.ui.lineEditReference.text())
        
        if section != '':
            self.container.addDB(sect=[section], subsect=[sub_section], funct=[function], phrase=[sentence], ref=[reference])
        self.updateSentenceView()
        
    def removeSentence(self, sentence=''):
        """
        Removes a sentence.
        """
        if sentence != '':
            section = self.ui.lineEditSection.text()
        else: 
            if self.removeQuestion("sentence",sentence) == QMessageBox.Yes:
                self.container.remove(phrase=[sentence])
        self.container.isModified(True)

    def updateSentence(self):
        """
        Updates a sentence.
        """

    def updateSentenceView(self):
        """
        Updates a sentence view.
        """
        sentencesFinal = []
        sections = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        sub_sections =  self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())
        functions =  self.selectedTitles(self.ui.listWidgetFunction.selectedItems())       

        sentences = self.container.listSentences(section=list(sections),subsection=list(sub_sections),function=list(functions))
        self.ui.tableWidgetSentence.clear()
        
        for i in range(len(sentences[0])):
            if sentences[0][i] != (u'NULL',u'NULL'):
               sentencesFinal.append(sentences[0][i])
        
        self.ui.tableWidgetSentence.setColumnCount(2)
        self.ui.tableWidgetSentence.setRowCount(len(sentencesFinal))
        
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(0,QTableWidgetItem(str('Sentence')))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(1,QTableWidgetItem(str('Reference')))
                      
        for row, sentence in enumerate(sentencesFinal):
            if sentence[0] != 'NULL' and sentence[1] != 'NULL':
               item_sentence = QTableWidgetItem(str(sentence[0]))
               self.ui.tableWidgetSentence.setItem(row,0,item_sentence)
               item_reference = QTableWidgetItem(str(sentence[1]))
               self.ui.tableWidgetSentence.setItem(row,1,item_reference)
            

    def tipsSentence(self):
        """
        Show tips for sentence.
        """ 
        QMessageBox.information(self, 
                self.tr('Sentence Tips'),
                self.tr('Sentences are extracted from scientific documents.\
 \n\nTo remove specific words or sub sentences, please, use {{}}.\
 \n\nExample: Here, we demonstrate the {{capacity of imaging spectroscopy}} to discriminate among \
 {{genotypes of Populus tremuloides}}.\
 \n\nThis will provide you a short view like: Here, we demonstrate the ... to discriminate among ...\
 \n\nNote that the original sentence remains unbroken.'),
                QMessageBox.Ok)

    # -----------------------------------------------------------------------
    # File methods
    # -----------------------------------------------------------------------
       
    def openFile(self):
        '''
        Opens a new file.
        '''
        path = QFileDialog.getOpenFileName(self,
                                           self.tr('Open File'),
                                           self.tr(self.container.path))[0]

        if path != '':
            # precisa salvar se tiver algo aberto antes
            self.container.read_(path)
            self.updateSectionView()

    def saveFile(self):
        '''
        Saves the file that is being used.
        '''
        if self.container.path == '':
            self.saveFileAs()
        else:
            self.container.write_()

    def saveFileAs(self):
        '''
        Saves a new file
        '''
        path = QFileDialog.getSaveFileName(self,
                                           self.tr('Save As'),
                                           self.tr(self.container.path))[0]
        if path != '':
            self.container.write_(path)
        
    def printFile(self):
        '''
        Generates a PDF file with all sentences included in database.
        '''
        self.notImplementedYet()

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
                self.container.clear_()
            elif answer == QMessageBox.No:
                self.container.clear_()
        else:
            self.container.clear_()
            
            
    def exportFile(self):
        '''
        Export file with extension.
        '''
        path = QFileDialog.getSaveFileName(self,
                                           self.tr('Export JSON File'),
                                           self.tr(self.container.path))
        if path != '':
            self.container.write_(path)
        
        
    def importFile(self):
        '''
        Import file with extension.
        '''
        path = QFileDialog.getOpenFileName(self,
                                           self.tr('Open JSON File'),
                                           self.tr(self.container.path))

        if path != '':
            self.container.read_(path)
            
    # -----------------------------------------------------------------------
    # Application methods
    # -----------------------------------------------------------------------

    def about(self):
        """
        About shows the main information about the application.
        """
        QMessageBox.about(self,
                          self.tr('About Sci Corpus'),
                          self.tr('This software is a corpus manager, that allows you to trainer.\
\n\nFor more information, please, visite the page: <https://github.com/zericardo182/sci-corpus/wiki> \
\n\nThis software was created by: Daniel C. Pizetta,  Jose R.F. Ronqui and Thiago Campo.\
\n\nVersion:{}'.format(__version__)))
    
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
            self.__db.close()
            self.closeFile()
            self.close()
            return True
        else:
            return False

    def tips(self):
        '''
        Show tips about aplication
        '''
        self.notImplementedYet()
        
    def notImplementedYet(self):
        """
        Show tips for function.
        """
        QMessageBox.information(self, 
                        self.tr('Sorry'),
                        self.tr('We have no implemented this function yet.'),
                        QMessageBox.Ok)

    def removeQuestion(self, category='', who=''):
        """
        Removes a section item
        """
        return QMessageBox.question(self,
                                    self.tr('Remove'),
                                    self.tr('Do you want to remove item {} from {}?'.format(who, category)),
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)
    #Have to change for [(,)]
    def updateQuestion(self, section=([], []), subsection=([], []), function=([], [])):
        """
        Updates a section item
        """
        return QMessageBox.question(self,
                                    self.tr('Update'),
                                    self.tr('Do you want to update item {} to {} in {}?'.format(oldWho,newWho,what)),
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)


if __name__ == '__main__':
    app = QApplication('Sci Corpus')
    main_window = MainWindow()
    main_window.show()
    exit(app.exec_())


'''

    # -----------------------------------------------------------------------
    # Section methods
    # -----------------------------------------------------------------------

        
    def addSection(self):
        """
        Add a new section.
        """
        section = str(self.ui.lineEditSection.text())
        if section != '':
            self.container.add(section)
        self.updateSectionView()

    def removeSection(self, section=''):
        """
        Remove a section.
        """
        if section != '':
            section = self.ui.lineEditSection.text()
        else: 
            if self.removeQuestion("section",section) == QMessageBox.Yes:
                return
        self.container.isModified(True)
                
    def updateSection(self, (old_section, new_section)):
        """
        Updates old section with new section.
        """
        self.container.isModified(True)
        self.updateSectionView()
        
    def updateSectionView(self):
        """
        Updates section view.
        """
        sections = self.container.sections()
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
                                self.tr('Sections are the main division of a scientific text.\
In summary, they are the titles of each section.'),
                                QMessageBox.Ok)
                                
    # -----------------------------------------------------------------------
    # Subsection methods
    # -----------------------------------------------------------------------
    

        
    def addSubSection(self):
        """
        Add a new Subsection
        """

        section = str(self.selectedTitles(self.ui.listWidgetSection.selectedItems())[0])
        sub_section = str(self.ui.lineEditSubSection.text())
        
        if sub_section != '':
            self.container.add(section, sub_section)
        self.updateSubSectionView()
        
    def removeSubSection(self, subsection=''):
        """
        Remove one subsection
        """
        if subsection != '':
            subsection = self.ui.lineEditSection.text()
        else: 
            if self.removeQuestion("subsection",subsection) == QMessageBox.Yes:
                return
                
    def updateSubSection(self):
        """
        Updates one subsection
        """

    def updateSubSectionView(self):
        """
        Updates subsection view
        """
        sections = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        subsections = self.container.subSections(sections)
        self.ui.listWidgetSubSection.clear()
        
        for row, value in enumerate(subsections):
            item = QListWidgetItem(str(value))
            self.ui.listWidgetSubSection.addItem(item)
            
    def tipsSubSection(self):
        """
        Show tips for Subsection
        """
        QMessageBox.information(self, 
                                self.tr('Sub Section Tips'),
                                self.tr('Sub section are a sub division of the section.\
\n\nAs an example, section Introduction has a Contextualization, Gap and Propose sub sections \
in an article.'),
                                QMessageBox.Ok)

    # -----------------------------------------------------------------------
    # Function methods
    # -----------------------------------------------------------------------

    def addFunction(self):
        """
        Adds a new function.
        """
        section = str(self.selectedTitles(self.ui.listWidgetSection.selectedItems())[0])
        sub_section = str(self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())[0])
        function = str(self.ui.lineEditFunction.text())
        if function != '':
            self.container.add(section, sub_section, function)
        self.updateFunctionView()
        
    def removeFunction(self, function=''):
        """
        Removes a function.
        """
        if function != '':
            section = self.ui.lineEditSection.text()
        else: 
            if self.removeQuestion("function",function) == QMessageBox.Yes:
                return
                # chama função remove Tiago

    def updateFunction(self):
        """
        Updates a function.
        """

    def updateFunctionView(self):
        """
        Updates a function view.
        """
        sections = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        sub_sections = self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())
        
        functions = self.container.functions(sections, sub_sections)
        self.ui.listWidgetFunction.clear()
        
        for row, value in enumerate(functions):
            item = QListWidgetItem(str(value))
            self.ui.listWidgetFunction.addItem(item)

    def tipsFunction(self):
        """
        Show tips for function.
        """
        QMessageBox.information(self, 
                        self.tr('Function Tips'),
                        self.tr('Function explain what each sentence is.'),
                        QMessageBox.Ok)

    # -----------------------------------------------------------------------
    # Sentence methods
    # -----------------------------------------------------------------------

    def addSentence(self):
        """
        Adds a new sentence.
        """
        section = str(self.selectedTitles(self.ui.listWidgetSection.selectedItems())[0])
        sub_section = str(self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())[0])
        function = str(self.selectedTitles(self.ui.listWidgetFunction.selectedItems())[0])
        sentence = str(self.ui.textEditSentence.toPlainText())
        reference = str(self.ui.lineEditReference.text())
        if section != '':
            self.container.add(section, sub_section, function, sentence, reference)
        self.updateSentenceView()
        
    def removeSentence(self, sentence=''):
        """
        Removes a sentence.
        """
        if sentence != '':
            section = self.ui.lineEditSection.text()
        else: 
            if self.removeQuestion("sentence",sentence) == QMessageBox.Yes:
                return
                # chama função remove Tiago

    def updateSentence(self):
        """
        Updates a sentence.
        """

    def updateSentenceView(self):
        """
        Updates a sentence view.
        """
        sections = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        sub_sections =  self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())
        functions =  self.selectedTitles(self.ui.listWidgetFunction.selectedItems())
        sentences = self.container.sentences(sections, sub_sections, functions)
        self.ui.tableWidgetSentence.clear()
        
        self.ui.tableWidgetSentence.setColumnCount(2)
        self.ui.tableWidgetSentence.setRowCount(len(sentences))
        
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(0,QTableWidgetItem(str('Sentence')))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(1,QTableWidgetItem(str('Reference')))
        
        for row, (sentence, reference) in enumerate(sentences):
            item_sentence = QTableWidgetItem(str(sentence))
            self.ui.tableWidgetSentence.setItem(row,0,item_sentence)
            item_reference = QTableWidgetItem(str(reference))
            self.ui.tableWidgetSentence.setItem(row,1,item_reference)
            

    def tipsSentence(self):
        """
        Show tips for sentence.
        """ 
        QMessageBox.information(self, 
                self.tr('Sentence Tips'),
                self.tr('Sentences are extracted from scientific documents.\
 \n\nTo remove specific words or sub sentences, please, use {{}}.\
 \n\nExample: Here, we demonstrate the {{capacity of imaging spectroscopy}} to discriminate among \
 {{genotypes of Populus tremuloides}}.\
 \n\nThis will provide you a short view like: Here, we demonstrate the ... to discriminate among ...\
 \n\nNote that the original sentence remains unbroken.'),
                QMessageBox.Ok)

    # -----------------------------------------------------------------------
    # File methods
    # -----------------------------------------------------------------------
       
    def openFile(self):
        """
        Opens a new file.
        """
        path = QFileDialog.getOpenFileName(self,
                                           self.tr('Open File'),
                                           self.tr(self.container.path))[0]

        if path != '':
            # precisa salvar se tiver algo aberto antes
            self.container.read_(path)
            self.updateSectionView()

    def saveFile(self):
        """
        Saves the file that is being used.
        """
        if self.container.path == '':
            self.saveFileAs()
        else:
            self.container.write_()

    def saveFileAs(self):
        """
        Saves a new file
        """
        path = QFileDialog.getSaveFileName(self,
                                           self.tr('Save As'),
                                           self.tr(self.container.path))[0]
        if path != '':
            self.container.write_(path)
        
    def printFile(self):
        """
        Generates a PDF file with all sentences included in database.
        """
        self.notImplementedYet()

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
                self.container.clear_()
            elif answer == QMessageBox.No:
                self.container.clear_()
        else:
            self.container.clear_()
            
            
    def exportFile(self):
        """
        Export file with extension.
        """
        path = QFileDialog.getSaveFileName(self,
                                           self.tr('Export JSON File'),
                                           self.tr(self.container.path))
        if path != '':
            self.container.write_(path)
        
        
    def importFile(self):
        '""
        Import file with extension.
        """
        path = QFileDialog.getOpenFileName(self,
                                           self.tr('Open JSON File'),
                                           self.tr(self.container.path))

        if path != '':
            self.container.read_(path)
            
    # -----------------------------------------------------------------------
    # Application methods
    # -----------------------------------------------------------------------

    def about(self):
        """
        About shows the main information about the application.
        """
        QMessageBox.about(self,
                          self.tr('About Sci Corpus'),
                          self.tr('This software is a corpus manager, that allows you to trainer.\
\n\nFor more information, please, visite the page: <https://github.com/zericardo182/sci-corpus/wiki> \
\n\nThis software was created by: Daniel C. Pizetta,  Jose R.F. Ronqui and Thiago Campo.\
\n\nVersion:{}'.format(__version__)))
    
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
            self.closeFile()
            self.close()
            return True
        else:
            return False

    def tips(self):
        """
        Show tips about aplication
        """
        self.notImplementedYet()
        
    def notImplementedYet(self):
        """
        Show tips for function.
        """
        QMessageBox.information(self, 
                        self.tr('Sorry'),
                        self.tr('We have no implemented this function yet.'),
                        QMessageBox.Ok)

    def removeQuestion(self, category='', who=''):
        """
        Removes a section item
        """
        return QMessageBox.question(self,
                                    self.tr('Remove'),
                                    self.tr('Do you want to remove item {} from {}?'.format(who, category)),
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


if __name__ == '__main__':
    app = QApplication('Sci Corpus')
    main_window = MainWindow()
    main_window.show()
    exit(app.exec_())
'''

