#! python
# -*- coding: utf-8 -*-

"""
Graphical interface for sci-corpus program.

Author: Daniel Pizetta <daniel.pizetta@usp.br>
             Tiago de Campos <tiago.campos@usp.br>
             José Ricardo Furlan Ronqui <jose.ronqui@usp.br>
Date: 04/04/2014

This script provides a graphical interface for sci-corpus program standalone.
"""

from PySide.QtGui import QApplication,  QMainWindow,  QMessageBox,  QListWidgetItem
from PySide.QtGui import QFileDialog,  QTableWidgetItem, QAbstractItemView

import container as container
import re

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
        self.ui.listWidgetSection.itemSelectionChanged.connect(self.updateSentenceView)

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
        self.ui.listWidgetSubSection.itemSelectionChanged.connect(self.updateSentenceView)

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
        
        # Signals
        self.ui.checkBoxSection.clicked.connect(lambda: self.ui.tableWidgetSentence.setColumnHidden(0, not self.ui.checkBoxSection.isChecked()))
        self.ui.checkBoxSubSection.clicked.connect(lambda: self.ui.tableWidgetSentence.setColumnHidden(1, not self.ui.checkBoxSubSection.isChecked()))
        self.ui.checkBoxFunction.clicked.connect(lambda: self.ui.tableWidgetSentence.setColumnHidden(2, not self.ui.checkBoxFunction.isChecked()))
        self.ui.checkBoxReference.clicked.connect(lambda: self.ui.tableWidgetSentence.setColumnHidden(4, not self.ui.checkBoxReference.isChecked()))
        
        self.updateSectionView()
        self.updateSubSectionView()
        self.updateFunctionView()
        self.updateSentenceView()
        
        # When initialize
        self.ui.tableWidgetSentence.setColumnHidden(0, not self.ui.checkBoxSection.isChecked())
        self.ui.tableWidgetSentence.setColumnHidden(1, not self.ui.checkBoxSubSection.isChecked())
        self.ui.tableWidgetSentence.setColumnHidden(2, not self.ui.checkBoxFunction.isChecked())
        self.ui.tableWidgetSentence.setColumnHidden(4, not self.ui.checkBoxReference.isChecked())
        
    def selectedTitles(self, selected_items):
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
            self.container.addDB(sect=[section])
            self.writeStatusBar('A new section "{}" has already added.'.format(section))
        self.ui.listWidgetSection.clear()
        self.updateSectionView()
        self.updateSentenceView()

    def removeSection(self):
        """
                    Remove a section.
                    """
        section = list(self.selectedTitles(self.ui.listWidgetSection.selectedItems()))
        if section != []:
            if self.removeQuestion("section",section) == QMessageBox.Yes:
                self.container.remove(sect=section)
        self.updateSectionView()
                
    def updateSection(self):
        """
                    Updates old section with new section.
                    """
        old_section = list(self.selectedTitles(self.ui.listWidgetSection.selectedItems()))
        new_section = str(self.ui.lineEditSection.text())
        
        if old_section != [] and new_section != '':
            if self.updateQuestion("section",(new_section,old_section)) == QMessageBox.Yes:
              self.container.update(section=[(new_section,old_section[0])])
        
        self.updateSectionView()
        
    def updateSectionView(self):
        """
                    Updates section view.
                    """
        self.ui.listWidgetSection.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.listWidgetSection.setDragEnabled(False)
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
        section = list(self.selectedTitles(self.ui.listWidgetSection.selectedItems()))
        sub_section = str(self.ui.lineEditSubSection.text())
        if sub_section != '':
            self.container.addDB(sect=section, subsect=[sub_section])
            self.writeStatusBar('A new sub section "{}" has already added.'.format(sub_section))
        self.updateSubSectionView()
        self.updateSentenceView()
        
    def removeSubSection(self):
        """
                    Remove one subsection
                    """
        subsection = list(self.selectedTitles(self.ui.listWidgetSubSection.selectedItems()))
        if subsection != []:
            if self.removeQuestion("subsection",subsection) == QMessageBox.Yes:
                self.container.remove(subsect=subsection)
        self.updateSubSectionView()
                
    def updateSubSection(self):
        """
                    Updates one subsection
                    """
        old_subsection = list(self.selectedTitles(self.ui.listWidgetSubSection.selectedItems()))
        new_subsection = str(self.ui.lineEditSubSection.text())
        
        if old_subsection != [] and new_subsection != '':
           if self.updateQuestion("subsection",(new_subsection,old_subsection)) == QMessageBox.Yes:
              self.container.update(subsection=[(new_subsection,old_subsection[0])])
        
        self.updateSubSectionView()

    def updateSubSectionView(self):
        """
                    Updates subsection view
                    """
        self.ui.listWidgetSubSection.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.listWidgetSubSection.setDragEnabled(False)
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
        section = list(self.selectedTitles(self.ui.listWidgetSection.selectedItems()))
        sub_section = list(self.selectedTitles(self.ui.listWidgetSubSection.selectedItems()))
        function = str(self.ui.lineEditFunction.text())
        
        if function != '':
            self.container.addDB(sect=section, subsect=sub_section, funct=[function])
            self.writeStatusBar('A new function "{}" has already added.'.format(function))
            
        self.updateFunctionView()
        
    def removeFunction(self, function=''):
        """
                    Removes a function.
                    """
        function = list(self.selectedTitles(self.ui.listWidgetFunction.selectedItems()))
        
        if function != []:
            if self.removeQuestion("function",function) == QMessageBox.Yes:
                self.container.remove(funct=function)
                
        self.updateFunctionView()

    def updateFunction(self):
        """
                    Updates a function.
                    """
        old_function = list(self.selectedTitles(self.ui.listWidgetFunction.selectedItems()))
        new_function = str(self.ui.lineEditFunction.text())
        
        if old_function != [] and new_function != '':
           if self.updateQuestion("function",(new_function,old_function)) == QMessageBox.Yes:
              self.container.update(function=[(new_function,old_function[0])])
        
        self.updateFunctionView()


    def updateFunctionView(self):
        """
                    Updates a function view.
                    """
        self.ui.listWidgetFunction.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.listWidgetFunction.setDragEnabled(False)
        sections = list(self.selectedTitles(self.ui.listWidgetSection.selectedItems()))
        sub_sections = list(self.selectedTitles(self.ui.listWidgetSubSection.selectedItems()))
        functions = self.container.listCategories(section=sections,subsection=sub_sections)[2]
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

    def adjustSentence(sent="", begin="", end="", hideMarked=True):
        """
        Adjusts sentences to be displayed on the screen.
        """
        b  = [match.start() for match in re.finditer(re.escape(begin), sent)]
        e  = [match.end() for match in re.finditer(re.escape(end), sent)]
        
        #exception here b and e must have the same size!
        if(len(b) == len(e)):
            
            replace = []
        
            if(hideMarked):
                for i in range(0,len(b)):
                    replace.append(sent[b[i]:e[i]])
            
                for substring in replace:
                    sent = sent.replace(substring, "...")
            else:
                aux=''

                if 0 not in b:
                    aux += " ... "

                for i in range(0,len(b)-1):
                    aux += sent[b[i]:e[i]]+" ... "
            
                if(e[len(b)-1]==len(sent)-1):
                    aux += sent[b[len(b)-1]:e[len(e)-1]]
                else:
                    aux += sent[b[len(b)-1]:e[len(e)-1]]+" ... "
                
                sent = aux.replace(begin,"").replace(end,"")
        else:
            raise AssertionError("Delimiter number doesnt match! =(")
            
        return sent

    def addSentence(self):
        """
        Adds a new sentence.
        """
        # Getting information
        section = list(self.selectedTitles(self.ui.listWidgetSection.selectedItems()))
        sub_section = list(self.selectedTitles(self.ui.listWidgetSubSection.selectedItems()))
        function = list(self.selectedTitles(self.ui.listWidgetFunction.selectedItems()))
        sentence = str(self.ui.textEditSentence.toPlainText())
        reference = str(self.ui.lineEditReference.text())
        # Insertting in DB
        if section != '':
            self.container.addDB(sect=section, subsect=sub_section, funct=function, phrase=[sentence], ref=[reference])
            self.writeStatusBar('A new sentence has already added.')
        self.updateSentenceView()
        
    def removeSentence(self):
        """
        Removes a sentence.
        """
        sentence = self.selectedTitles(self.ui.tableWidgetSentence.selectedItems())
        if sentence != []:
            if self.removeQuestion("sentence",sentence) == QMessageBox.Yes:
                self.container.remove(phrase=sentence)
        self.updateSentenceView()

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
            if sentences[0][i][0] != u'NULL':
               sentencesFinal.append(sentences[0][i])
               
        self.ui.tableWidgetSentence.setRowCount(len(sentencesFinal))
        self.ui.tableWidgetSentence.setColumnWidth(4,50)
        self.ui.tableWidgetSentence.setColumnCount(5)
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(0,QTableWidgetItem(str('Section')))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(1,QTableWidgetItem(str('Sub Section')))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(2,QTableWidgetItem(str('Function')))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(3,QTableWidgetItem(str('Sentence')))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(4,QTableWidgetItem(str('Reference')))

        for row, sentence in enumerate(sentencesFinal):
            if sentence[0] != 'NULL' and sentence[1] != 'NULL':
               item_sentence = QTableWidgetItem(str(sentence[0]))
               self.ui.tableWidgetSentence.setItem(row,3,item_sentence)
               item_reference = QTableWidgetItem(str(sentence[1]))
               self.ui.tableWidgetSentence.setItem(row,4,item_reference)
            

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
        """"
                    Opens a new file.
                    """
        path = QFileDialog.getOpenFileName(self,
                                           self.tr('Open File'),
                                           self.tr(self.container.path))[0]

        if path != '':
            self.closeFile()
            self.container.read_(path)
            self.updateSectionView()

    def saveFile(self):
        """"
                    Saves the file that is being used.
                    """
        if self.container.path == '':
            self.saveFileAs()
        else:
            self.container.write_()

    def saveFileAs(self):
        """"
                    Saves a new file
                    """
        path = QFileDialog.getSaveFileName(self,
                                 self.tr('Save As'),
                                 self.tr(self.container.path))[0]
        if path != '':
            self.container.write_(path)
        
    def printFile(self):
        """"
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
        '''
        Export file with extension.
        '''
        path = QFileDialog.getSaveFileName(self,
                                           self.tr('Export File'),
                                           self.tr(self.container.path))
        if path != '':
            self.container.write_(path)
        
        
    def importFile(self):
        '''
        Import file with extension.
        '''
        path = QFileDialog.getOpenFileName(self,
                                           self.tr('Import File'),
                                           self.tr(self.container.path),
                                           self.tr("Files (*.json *.xml)"))

        if path != '':
            self.container.read_(path)
        
        self.updateSectionView()
        self.updateSubSectionView()
        self.updateFunctionView()
        self.updateSentenceView()
            
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
        Quit application.
        """
        self.closeEvent()
        
    def closeEvent(self, event):
        """
        Close event.
        """
        answer = QMessageBox.question(self, 
                                      self.tr('Quit'),
                                      self.tr('Do you want to exit Sci Corpus?'),
                                      QMessageBox.Yes | QMessageBox.No, 
                                      QMessageBox.No)
        if answer == QMessageBox.Yes:
            
            # Isto esta errado...fazer um metodo para fechar...
            self.container.__db.close()
            self.closeFile()
            event.accept()
        else:
            event.ignore()
            
    def writeStatusBar(self,  msg):
        """
        Display message on status bar.
        """
        status_bar = self.statusBar()
        status_bar.clearMessage()
        status_bar.showMessage(str(msg), 5000)

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
                                    
    def updateQuestion(self, section=(), subsection=(), function=()):
        """
        Updates a section item
        """
        
        if section != ():
           category = 'section'
           oldWho = section[1]
           newWho = section[0]

        if subsection != ():
           category = 'subsection'
           oldWho = subsection[1]
           newWho = subsection[0]
        
        if function != ():
           category = 'function'
           oldWho = function[1]
           newWho = function[0]
        
        return QMessageBox.question(self,
                                    self.tr('Update'),
                                    self.tr('Do you want to update item "{}" to "{}" in {}?'.format(oldWho[0],newWho,category)),
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

