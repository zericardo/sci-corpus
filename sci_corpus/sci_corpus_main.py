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

from PySide.QtGui import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from PySide.QtGui import QFileDialog, QTableWidgetItem, QAbstractItemView
from PySide.QtGui import QBrush, QColor

from PySide.QtCore import QSettings,  QRect,  Signal

import container
import re
import os
import json
import codecs

from time import gmtime, strftime

from ui import main_window_ui
import start_dlg

__version__='1.0'
__pname__ = 'Sci Corpus'
__ext_name__ = 'Scientific Corpus Manager'

class MainWindow(QMainWindow):
    
    logSig = Signal(str)
    
    def __init__(self, argv=None, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.tabifyDockWidget(self.ui.dockWidgetLogView, self.ui.dockWidgetTableView)
        
        # We should put something util
        start = start_dlg.StartDialog(self)
        start.show()
        start.informationProgress('Starting')
        start.updateProgress(10)
        start.informationProgress('Loading interface')
        start.updateProgress(30)
        start.informationProgress('Loading preferences')
        start.updateProgress(60)
        start.informationProgress('Loading environment')
        start.updateProgress(90)
        start.informationProgress('Finishing to run')
        start.updateProgress(100)
        start.close()
        
        self.container = container.ContainerDB()
        
        self.theme = 'Black'
        self.replaceBy = '...'
        self.marker = '{}'
        self.hideMarked = True
        self.preferences = {'theme':self.theme, 
                    'section':self.ui.checkBoxSection.isChecked(), 
                    'subsection': self.ui.checkBoxSubSection.isChecked(), 
                    'function': self.ui.checkBoxFunction.isChecked(), 
                    'sentence': self.ui.checkBoxSentence.isChecked(), 
                    'reference': self.ui.checkBoxReference.isChecked(), 
                    'strip': self.ui.checkBoxStrip.isChecked(), 
                    'replace_by':self.replaceBy, 
                    'marker': self.marker, 
                    'hide_marked':self.hideMarked, 
                    'last_path': self.container.path}
        
        # File ----------------------------------------------------------------
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionSaveAs.triggered.connect(self.saveFileAs)
        self.ui.actionPrint.triggered.connect(self.printFile)
        self.ui.actionImport.triggered.connect(self.importFile)
        self.ui.actionExport.triggered.connect(self.exportFile)
        self.ui.actionClose.triggered.connect(self.closeFile)
        
        # Application ---------------------------------------------------------
        # Actions
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionTips.triggered.connect(self.tips)
        # Signals
        self.logSig.connect(self.showLogMessage)
        
        # Section --------------------------------------------------------------
        # Buttons
        self.ui.pushButtonSectionAdd.clicked.connect(self.addSection)
        self.ui.pushButtonSectionRemove.clicked.connect(self.removeSection)
        self.ui.pushButtonSectionUpdate.clicked.connect(self.updateSection)
        # Actions
        self.ui.actionAddSection.triggered.connect(self.addSection)
        self.ui.actionRemoveSection.triggered.connect(self.removeSection)
        self.ui.actionUpdateSection.triggered.connect(self.updateSection)
        self.ui.actionTipsSection.triggered.connect(self.tipsSection)
        # Signals
        self.ui.listWidgetSection.doubleClicked.connect(lambda: \
                self.ui.lineEditSection.setText(\
                self.ui.listWidgetSection.currentItem().text()))
        self.ui.listWidgetSection.itemSelectionChanged.connect(lambda: \
                self.ui.lineEditSection.clear())
        self.ui.listWidgetSection.itemSelectionChanged.connect(\
                self.updateSubSectionView)
        self.ui.listWidgetSection.itemSelectionChanged.connect(\
                self.updateSentenceView)
        self.ui.listWidgetSection.itemSelectionChanged.connect(\
                self.updateSelectedNumbers)
        # Properties
        self.ui.listWidgetSection.setSelectionMode(\
                QAbstractItemView.ExtendedSelection)
        self.ui.listWidgetSection.setDragEnabled(False)

        # Subsection ----------------------------------------------------------
        # Buttons
        self.ui.pushButtonSubSectionAdd.clicked.connect(self.addSubSection)
        self.ui.pushButtonSubSectionRemove.clicked.connect(self.removeSubSection)
        self.ui.pushButtonSubSectionUpdate.clicked.connect(self.updateSubSection)
        # Actions
        self.ui.actionAddSubSection.triggered.connect(self.addSubSection)
        self.ui.actionRemoveSubSection.triggered.connect(self.removeSubSection)
        self.ui.actionUpdateSubSection.triggered.connect(self.updateSubSection)
        self.ui.actionTipsSubSection.triggered.connect(self.tipsSubSection)
        # Signals
        self.ui.listWidgetSubSection.doubleClicked.connect(lambda: \
                self.ui.lineEditSubSection.setText(\
                self.ui.listWidgetSubSection.currentItem().text()))
        self.ui.listWidgetSubSection.itemSelectionChanged.connect(lambda: \
                self.ui.lineEditSubSection.clear())
        self.ui.listWidgetSubSection.itemSelectionChanged.connect(self.updateFunctionView)
        self.ui.listWidgetSubSection.itemSelectionChanged.connect(self.updateSentenceView)
        self.ui.listWidgetSubSection.itemSelectionChanged.connect(self.updateSelectedNumbers)
        # Properties
        self.ui.listWidgetSubSection.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.listWidgetSubSection.setDragEnabled(False)
        
        # Function -------------------------------------------------------------
        # Buttons
        self.ui.pushButtonFunctionAdd.clicked.connect(self.addFunction)
        self.ui.pushButtonFunctionRemove.clicked.connect(self.removeFunction)
        self.ui.pushButtonFunctionUpdate.clicked.connect(self.updateFunction)
        # Actions
        self.ui.actionAddFunction.triggered.connect(self.addFunction)
        self.ui.actionRemoveFunction.triggered.connect(self.removeFunction)
        self.ui.actionUpdateFunction.triggered.connect(self.updateFunction)
        self.ui.actionTipsFunction.triggered.connect(self.tipsFunction)
        # Signals
        self.ui.listWidgetFunction.doubleClicked.connect(lambda: \
                self.ui.lineEditFunction.setText(\
                self.ui.listWidgetFunction.currentItem().text()))
        self.ui.listWidgetFunction.itemSelectionChanged.connect(lambda: \
                self.ui.lineEditFunction.clear())
        self.ui.listWidgetFunction.itemSelectionChanged.connect(self.updateSentenceView)
        self.ui.listWidgetFunction.itemSelectionChanged.connect(self.updateSelectedNumbers)
        # Properties
        self.ui.listWidgetFunction.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.listWidgetFunction.setDragEnabled(False)
        
        # Sentence ------------------------------------------------------------
        # Buttons
        self.ui.pushButtonSentenceAdd.clicked.connect(self.addSentence)
        self.ui.pushButtonSentenceRemove.clicked.connect(self.removeSentence)
        self.ui.pushButtonSentenceUpdate.clicked.connect(self.updateSentence)
        # Actions
        self.ui.actionAddSentence.triggered.connect(self.addSentence)
        self.ui.actionRemoveSentence.triggered.connect(self.removeSentence)
        self.ui.actionUpdateSentence.triggered.connect(self.updateSentence)
        self.ui.actionTipsSentence.triggered.connect(self.tipsSentence)
        # Signals
        self.ui.checkBoxSection.clicked.connect(lambda: \
                self.ui.tableWidgetSentence.setColumnHidden(0, \
                not self.ui.checkBoxSection.isChecked()))
        self.ui.checkBoxSubSection.clicked.connect(lambda: 
                self.ui.tableWidgetSentence.setColumnHidden(1, \
                not self.ui.checkBoxSubSection.isChecked()))
        self.ui.checkBoxFunction.clicked.connect(lambda: \
                self.ui.tableWidgetSentence.setColumnHidden(2, \
                not self.ui.checkBoxFunction.isChecked()))
        self.ui.checkBoxSentence.clicked.connect(lambda: \
                self.ui.tableWidgetSentence.setColumnHidden(3, \
                not self.ui.checkBoxSentence.isChecked()))
        self.ui.checkBoxReference.clicked.connect(lambda: \
                self.ui.tableWidgetSentence.setColumnHidden(4, \
                not self.ui.checkBoxReference.isChecked()))
        self.ui.tableWidgetSentence.itemSelectionChanged.connect(self.updateSelectedNumbers)
        self.ui.checkBoxStrip.clicked.connect(self.updateSentenceView)
        # Properties
        self.ui.tableWidgetSentence.setRowCount(0)
        self.ui.checkBoxStrip.setChecked(True)
        # Cleaning
        self.clearAll()
        self.updateSectionView()
        self.updateSentenceView()
        
    def selectedTitles(self, selected_items):
        """
        Return a list of selected titles.
        """
        titles = []
        for item in  selected_items:
            titles.append(str(item.text()))
        return titles  
        
    def updateSelectedNumbers(self):
        """
        Updates selected numbers from list and table views.
        """
        self.ui.labelSelectedSection.setText(str(len(self.ui.listWidgetSection.selectedItems())))
        self.ui.labelSelectedSubSection.setText(str(len(self.ui.listWidgetSubSection.selectedItems())))
        self.ui.labelSelectedFunction.setText(str(len(self.ui.listWidgetFunction.selectedItems())))
        self.ui.labelSelectedSentence.setText(str(len(self.ui.tableWidgetSentence.selectedItems())))
        
    def updateTotalNumbers(self):
        """
        Updates total numbers from list and table views.
        """
        sec = set()
        subs = set()
        func = set()
        sent = set()
        
        # @TODO: This can be better :), maybe a property of container
        for secv, subsv, funcv, sentv, refv in self.container.listSentences():
            sec.add(secv)
            subs.add(subsv)
            func.add(funcv)
            if sentv != u'NULL':
                sent.add(sentv)
        
        self.ui.labelTotalSection.setText(str(len(sec)))
        self.ui.labelTotalSubSection.setText(str(len(subs)))
        self.ui.labelTotalFunction.setText(str(len(func)))
        self.ui.labelTotalSentence.setText(str(len(sent)))
        
        
    # -----------------------------------------------------------------------
    # Section methods
    # -----------------------------------------------------------------------

        
    def addSection(self):
        """
        Add a new section.
        """
        sec = str(self.ui.lineEditSection.text())
        
        if sec != '':
            self.container.addDB(sect=[sec])
            self.logSig.emit('A new section "{}" was added.'.format(sec))
            self.showMessageOnStatusBar('A new section "{}" was added.'.format(sec))
            
        self.updateTotalNumbers()
        self.updateSectionView()


    def removeSection(self):
        """
        Remove a section.
        """
        sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        
        if sec != []:
            if self.removeQuestion("Section",sec) == QMessageBox.Yes:
                self.container.remove(sect=sec)
                self.showMessageOnStatusBar('Section(s) was removed.'.format(sec))
                
        self.updateTotalNumbers()
        self.updateSectionView()
               
               
    def updateSection(self):
        """
        Updates old section with new section.
        """
        old_sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        new_sec = str(self.ui.lineEditSection.text())
        
        if len(old_sec) != 1:
            QMessageBox.warning(self, 
                                self.tr('Update'),
                                self.tr('Please select just one item to update.'),
                                QMessageBox.Ok)
        elif new_sec != '':
            if self.updateQuestion("Section",(old_sec[0], new_sec)) == QMessageBox.Yes:
                self.container.update(section=[(new_sec,old_sec[0])])
                self.showMessageOnStatusBar('Section "{}" was updated to "{}".'.format(old_sec[0], new_sec))

        self.updateSectionView()
        
        
    def updateSectionView(self):
        """
        Updates section view.
        """
        sec = set()
        # @TODO: In the future, not use for
        for secv, subsv, funcv in self.container.listCategories():
            sec.add(secv)
        
        self.ui.listWidgetSection.clear()
        sec = sorted(sec)
        self.ui.labelDisplayedSection.setText(str(len(sec)))
        
        if "Not Classified" in sec:
            sec.remove("Not Classified")
            sec.append("Not Classified")
            
        for row, value in enumerate(sec):
            item = QListWidgetItem(str(value))
            self.ui.listWidgetSection.addItem(item)
            
        self.updateSubSectionView()
        self.updateFunctionView()
        self.updateSentenceView()
            
            
    def tipsSection(self):
        """
        Show tips for the section.
        """    
        QMessageBox.information(self, 
                                self.tr('Section Tips'),
                                self.tr('Sections are the main division of a \
scientific text. In summary, they are the titles of each section.'),
                                QMessageBox.Ok)
                                
    # -----------------------------------------------------------------------
    # Sub Section methods
    # -----------------------------------------------------------------------

    def addSubSection(self):
        """
        Add a new Subsection
        """
        sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        subs = str(self.ui.lineEditSubSection.text())
        
        if subs != '':
            self.container.addDB(sect=sec, subsect=[subs])
            self.showMessageOnStatusBar('A new sub section "{}" was added.'.format(subs))
            
        self.updateTotalNumbers()
        self.updateSubSectionView()

    
    def removeSubSection(self):
        """
        Remove one subsection
        """
        subs = self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())
        
        if subs != []:
            if self.removeQuestion("Subsection",subs) == QMessageBox.Yes:
                self.container.remove(subsect=subs)
                self.showMessageOnStatusBar('A sub section was removed.')
                
        self.updateTotalNumbers()
        self.updateSubSectionView() 
                
                
    def updateSubSection(self):
        """
        Updates one subsection
        """
        old_subs = self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())
        new_subs = str(self.ui.lineEditSubSection.text())
        
        if len(old_subs) != 1:
            QMessageBox.warning(self, 
                                self.tr('Update'),
                                self.tr('Please select just one item to update.'),
                                QMessageBox.Ok)
        elif new_subs != '':
           if self.updateQuestion("Subsection",(old_subs[0], new_subs)) == QMessageBox.Yes:
              self.container.update(subsection=[(new_subs,old_subs[0])])
              self.showMessageOnStatusBar('Sub section "{}" was updated to "{}".'.format(old_subs[0], new_subs))
        
        self.updateSubSectionView()


    def updateSubSectionView(self):
        """
        Updates subsection view
        """
        sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        subs = set()
        subsecs = []

        if sec == []:
            for secv, subsv, funcv in self.container.listCategories(section=sec):
                subs.add(subsv)
        # This havent be treat here, this need to be treated on contianer.
        else:
            for i in range(len(sec)):
                subsecs.append({subsv for secv, subsv, funcv in self.container.listCategories(section=[sec[i]])})
            subs = subsecs[0]
            for i in range(len(sec)-1):
                subs = subs & subsecs[i+1]
            
        self.ui.listWidgetSubSection.clear()
        subs = sorted(subs)

        if "Not Classified" in subs:
            subs.remove("Not Classified")
            subs.append("Not Classified")
       
        for row, value in enumerate(subs):
            item = QListWidgetItem(str(value))
            self.ui.listWidgetSubSection.addItem(item)
            
        self.ui.labelDisplayedSubSection.setText(str(len(subs)))  
        self.updateFunctionView()
        self.updateSentenceView()
            
            
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
        sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        subs = self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())
        func = str(self.ui.lineEditFunction.text())
        
        if func != '':
            self.container.addDB(sect=sec, subsect=subs, funct=[func])
            self.showMessageOnStatusBar('A new function "{}" was added.'.format(func))
        
        self.updateTotalNumbers()  
        self.updateFunctionView()
        
        
    def removeFunction(self, function=''):
        """
        Removes a function.
        """
        func = self.selectedTitles(self.ui.listWidgetFunction.selectedItems())
        
        if func != []:
            if self.removeQuestion("Function",func) == QMessageBox.Yes:
                self.container.remove(funct=func)
                self.showMessageOnStatusBar('A function has already removed.')
        
        self.updateTotalNumbers()
        self.updateFunctionView()


    def updateFunction(self):
        """
        Updates a function.
        """
        old_func = self.selectedTitles(self.ui.listWidgetFunction.selectedItems())
        new_func = str(self.ui.lineEditFunction.text())
        
        if len(old_func) != 1:
            QMessageBox.warning(self, 
                                self.tr('Update'),
                                self.tr('Please select just one item to update.'),
                                QMessageBox.Ok)
        elif new_func != '':
           if self.updateQuestion("Function",(old_func[0], new_func)) == QMessageBox.Yes:
              self.container.update(function=[(new_func,old_func[0])])
              self.showMessageOnStatusBar('Function "{}" was updated to "{}".'.format(old_func[0], new_func))
              
        self.updateFunctionView()


    def updateFunctionView(self):
        """
        Updates a function view.
        """
        sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        subs = self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())
        func = set()
        
        funcs = []

        if sec == [] and subs == []:
            for secv, subsv, funcv in self.container.listCategories(section=sec):
                func.add(funcv)
        # This havent be treat here, this need to be treated on contianer.
        elif sec != [] and subs == []:
            for i in range(len(sec)):
                funcs.append({funcv for secv, subsv, funcv in self.container.listCategories(section=[sec[i]])})
                
            func = funcs[0]
            for i in range(len(sec)-1):
                func = func & funcs[i+1]
                
        elif sec != [] and subs != []:
            for i in range(len(sec)):
                for j in range(len(subs)):
                    funcs.append({funcv for secv, subsv, funcv in self.container.listCategories(section=[sec[i]],subsection=[subs[j]])})
                
            func = funcs[0]
            for i in range(len(funcs)-1):
                func = func & funcs[i+1]    


        self.ui.listWidgetFunction.clear()
        func = sorted(func)
        
        self.ui.labelDisplayedFunction.setText(str(len(func)))

        if "Not Classified" in func:
            func.remove("Not Classified")
            func.append("Not Classified")
            
        for row, value in enumerate(func):
            item = QListWidgetItem(str(value))
            self.ui.listWidgetFunction.addItem(item)
            
        self.updateSentenceView()


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


    def adjustSentence(self,sent="", begin="{", end="}", hideMarked=True, changeBy="..."):
        """
        Adjusts sentences to be displayed on the screen.
        """
        b  = [match.start() for match in re.finditer(re.escape(begin), sent)]
        e  = [match.end() for match in re.finditer(re.escape(end), sent)]

        #exception here b and e must have the same size!
        if(len(b) == len(e)):
            for i in range(0,len(b)):
                if(b[i]>=e[i]):
                    raise AssertionError("Delimiters aren't being used correctly!")

            r = []
        
            for i in range(0,len(b)):
                r.append(sent[b[i]:e[i]])

            if(hideMarked):
                for substring in r:
                    sent = sent.replace(substring, changeBy)
            else:
                if(r != []):
                    # @TODO: talvez colocar um erro em um else para este if!
                    aux=''

                    if 0 not in b:
                        aux += changeBy+" "

                    for i in range(0,len(b)-1):
                        aux += sent[b[i]:e[i]]+" "+changeBy+" "
            
                    if(e[len(b)-1]==len(sent)-1):
                        aux += sent[b[len(b)-1]:e[len(e)-1]]
                    else:
                        aux += sent[b[len(b)-1]:e[len(e)-1]]+" "+changeBy+" "
                
                    sent = aux.replace(begin,"").replace(end,"")
        else:
            raise AssertionError("Delimiter number doesnt match!")
            
        return sent


    def addSentence(self):
        """
        Adds a new sentence.
        """
        # Getting information
        sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        subs = self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())
        func = self.selectedTitles(self.ui.listWidgetFunction.selectedItems())
        sent = str(self.ui.textEditSentence.toPlainText())
        ref = str(self.ui.lineEditReference.text())
        
        self.ui.textEditSentence.clear()
        self.ui.lineEditReference.clear()
        
        # Insertting in DB
        self.container.addDB(sect=sec, subsect=subs, funct=func, phrase=[sent], ref=[ref])
        self.showMessageOnStatusBar('A new sentence was added.')
        
        self.updateTotalNumbers()
        self.updateSentenceView()
        
        
    def removeSentence(self):
        """
        Removes a sentence.
        """
        self.notImplementedYet()      
        self.updateTotalNumbers()
        self.updateSentenceView()


    def updateSentence(self,  old_sentence='',  new_sentence=''):
        """
        Updates a sentence.
        """
        self.notImplementedYet()
        self.updateSentenceView()
        
        
    def updateSentenceView(self):
        """
        Updates a sentence view.
        """
        
        sections = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        sub_sections =  self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())
        functions =  self.selectedTitles(self.ui.listWidgetFunction.selectedItems())       
        sentences = self.container.listSentences(section=sections,subsection=sub_sections,function=functions)
        
        self.ui.tableWidgetSentence.clearContents()
        self.ui.tableWidgetSentence.setColumnCount(5)
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(0,QTableWidgetItem('Section'))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(1,QTableWidgetItem('Sub Section'))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(2,QTableWidgetItem('Function'))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(3,QTableWidgetItem('Sentence'))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(4,QTableWidgetItem('Reference'))

        row = 0
        strip = self.ui.checkBoxStrip.isChecked()

        for secv, subsv, funcv, sentv, refv in sentences:
            if sentv != u'NULL':

                sec_item = QTableWidgetItem(str(secv))
                subs_item = QTableWidgetItem(str(subsv))
                func_item = QTableWidgetItem(str(funcv))
                sent_item = QTableWidgetItem(str(sentv))
                ref_item = QTableWidgetItem(str(refv))
                
                self.ui.tableWidgetSentence.setItem(row,0,sec_item)
                self.ui.tableWidgetSentence.setItem(row,1,subs_item)
                self.ui.tableWidgetSentence.setItem(row,2,func_item)
                self.ui.tableWidgetSentence.setItem(row,3,sent_item)
                self.ui.tableWidgetSentence.setItem(row,4,ref_item)
                
                if strip:
                    try:
                        sent_item.setText(str(self.adjustSentence(sentv, "{", "}", False, "...")))
                    except Exception:
                        sent_item.setText(str(sentv))
                        # Background red
                        sent_item.setBackground(QBrush(QColor(255,0,0,127)))
                row += 1
                
        self.ui.labelDisplayedSentence.setText(str(row))
        self.ui.tableWidgetSentence.setRowCount(row)
        
        self.ui.tableWidgetSentence.setColumnHidden(0, \
            not self.ui.checkBoxSection.isChecked())
        self.ui.tableWidgetSentence.setColumnHidden(1, \
            not self.ui.checkBoxSubSection.isChecked())
        self.ui.tableWidgetSentence.setColumnHidden(2, \
            not self.ui.checkBoxFunction.isChecked())
        self.ui.tableWidgetSentence.setColumnHidden(3, \
            not self.ui.checkBoxSentence.isChecked())
        self.ui.tableWidgetSentence.setColumnHidden(4, \
            not self.ui.checkBoxReference.isChecked())
        
            
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
            self.container.read_(path)
            self.setWindowTitle(__pname__+" V."+__version__+" : "+self.container.path)
            self.updateSelectedNumbers()
            self.updateTotalNumbers()
            self.updateSectionView()
            self.isModified = False
            
            
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
                self.saveFile()

        self.container.close_()
        self.setWindowTitle(__pname__+" V."+__version__)
        self.clearAll()    
        
        
    def exportFile(self):
        """
        Export file with extension.
        """
        self.notImplementedYet()
        """
        path = QFileDialog.getSaveFileName(self,
                                           self.tr('Export File'),
                                           self.tr(self.container.path))
        if path != '':
            self.container.export_(path)
        """
        
        
    def importFile(self):
        """
        Import file with extension.
        """
        #@TODO: show a dialog to choose separator and id
        QMessageBox.information(self, 
                self.tr('Import File'),
                self.tr('Please, before you try import the file,\n \
                        ensure that if it is a CSV one, the separator is ; (semi collon) \n \
                        and string identificator is " (double quote)'),
                QMessageBox.Ok)
                
        path = QFileDialog.getOpenFileName(self,
                                           self.tr('Import File'),
                                           self.tr(os.path.dirname(self.container.path)),
                                           self.tr('(*.xml *.csv)'))[0]

        if path != '':
            try:
                self.container.import_(path)
            except Exception, e:
                self.clearAll()
                QMessageBox.warning(self, 
                        self.tr('Import File'),
                        self.tr('We could not import the file. \nError:{}'.format(str(e))),
                        QMessageBox.Ok)
        
        self.updateSectionView()
        self.updateSentenceView()
        
    # -----------------------------------------------------------------------
    # Application methods
    # -----------------------------------------------------------------------
        
    def readPreferences(self):
        """
        Reads preferences from file.
        """
        with codecs.open(os.path.abspath(os.path.join(\
                os.path.expanduser('~'), \
                'scicorpuspreferences.ini')), 'wb', 'utf-8') as file:
            self.preferences = json.loads(file)
        
        
    def writePreferences(self):
        """
        Writes preferences on file.
        """
        with codecs.open(os.path.abspath(os.path.join(\
                os.path.expanduser('~'), \
                'scicorpuspreferences.ini')), 'wb', 'utf-8') as file:
            json.dump(self.preferences, file,  indent=4,  sort_keys=True)


    def writeSettings(self):
        """
        Write settings fo window state and geometry.
        """
        settings = QSettings("SciCorpus", "SciCorpus")
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("windowState", self.saveState())


    def readSettings(self):
        """
        Read settings of window state and geometry.
        """
        settings = QSettings ("SciCorpus", "SciCorpus")
        self.restoreGeometry(settings.value("geometry").toByteArray())
        self.restoreState(settings.value("windowState").toByteArray())


    def clearAll(self):
        """
        Clear all viewers.
        """
        # Clear edit fields
        self.ui.lineEditSection.clear()
        self.ui.lineEditSubSection.clear()
        self.ui.lineEditFunction.clear()
        self.ui.textEditSentence.clear()
        # Clear list viewers
        self.ui.listWidgetSection.clear()
        self.ui.listWidgetSubSection.clear()
        self.ui.listWidgetFunction.clear()
        # Clear table view
        self.ui.tableWidgetSentence.clearContents()

        
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
            self.closeFile()
            self.writeSettings()
            event.accept()
        else:
            event.ignore()


    def showMessageOnStatusBar(self,  msg):
        """
        Display message on status bar.
        """
        status_bar = self.statusBar()
        status_bar.clearMessage()
        status_bar.showMessage(str(msg), 5000)
        
        
    def showLogMessage(self, msg):
        """
        Show log message in log view.
        """
        time_now = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
        new_text = '{} || {}'.format(time_now, str(msg))
        self.ui.textEditLogView.append(new_text)
        scrolbar = self.ui.textEditLogView.verticalScrollBar()
        scrolbar.setValue(scrolbar.maximum())


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


    def removeQuestion(self, category='', who=[]):
        """
        Removes a section item
        """    
            
        return QMessageBox.question(self,
                                    self.tr('Remove'),
                                    self.tr("Do you want to remove item(s) {} from {}?".format(str(who)[1:-1], category)),
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)
                                    
                                    
    def updateQuestion(self, category, (old_who, new_who)):
        """
        Updates a section item
        """
        return QMessageBox.question(self,
                                    self.tr('Update'),
                                    self.tr("Do you want to update item '{}' to '{}' in {}?".format(old_who,new_who,category)),
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)
                                    
                                    
    def about(self):
        """
        About shows the main information about the application.
        """
        QMessageBox.about(self,
                          self.tr('About {}'.format(__pname__)),
                          self.tr('This software is a corpus manager, that allows you to trainer.\
\n\nFor more information, please, visite the page: <https://github.com/zericardo182/sci-corpus/wiki> \
\n\nThis software was created by: Daniel C. Pizetta,  Jose R.F. Ronqui and Thiago Campo.\
\n\nVersion:{}'.format(__version__)))



if __name__ == '__main__':
    app = QApplication(__pname__)
    try:
        style_sheet = ''
        with open(os.path.abspath('ui/white_theme.sty'),'rb') as style_file:
            style_sheet = str(style_file.read())
            app.setStyleSheet(style_sheet)
    except Exception,  e:
        print 'Error in style sheet: ',  e
        pass
        
    main_window = MainWindow()
    main_window.setWindowTitle(__pname__+" V."+__version__) 
    main_window.showMaximized()
    exit(app.exec_())
