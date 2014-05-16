#! python
# -*- coding: utf-8 -*-

"""
.. module:: sci_corpus_main
   :platform: Unix, Windows
   :synopsis: Graphical interface for sci-corpus program.

.. moduleauthor:: Daniel Pizetta <daniel.pizetta@usp.br>
.. moduleauthor:: Tiago de Campos <tiago.campos@usp.br>
.. moduleauthor:: José Ricardo Furlan Ronqui <jose.ronqui@usp.br>

Date: 04/04/2014 #@TODO: how to put this?

This script provides a graphical interface for sci-corpus program standalone.
"""

from PySide.QtGui import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from PySide.QtGui import QFileDialog, QTableWidgetItem, QAbstractItemView
from PySide.QtGui import QBrush, QColor
from PySide.QtCore import QSettings, Signal, Qt

from sci_corpus import pdf_writer
from sci_corpus import start_dlg
from sci_corpus import preferences_dlg
from sci_corpus import container
from sci_corpus.ui import main_window_ui

import re
import os
import sys
import json
import codecs
import platform

from time import gmtime, strftime
from reportlab.platypus.doctemplate import BaseDocTemplate

__version__ = 'v.0.9.0'
__name__ = 'Sci Corpus'
__ext_name__ = 'Scientific Corpus Manager'


class MainWindow(QMainWindow):

    logSig = Signal(str)

    def __init__(self, argv=None, parent=None):
        """
        Constructor for Main Window class.

        Parameters:
        -----------
        argv: list
              List of arguments.

        parent: QWidget
                Widget set as a parent.

        """
        super(MainWindow, self).__init__(parent)
        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle(__name__+ " "+ __version__)

        self.firstTimeOpened = True
        self.workspace = os.path.abspath(os.path.expanduser('~'))
        self.defaultPref = {
            'section': True,
            'subsection': True,
            'function': True,
            'sentence': True,
            'reference': False,
            'strip': True,
            'theme': 'White',
            'marker': '{}',
            'replace_by': '...',
            'replace_where': 'Outside Markers',
            'win_workspace':'',
            'lin_workspace':'',
            'mac_workspace':'',
            'open_last': True,
            'last_path': ''}
        self.preferences = self.defaultPref
        self.setupWorkspace()

        start = start_dlg.StartDialog(self)
        start.version(__version__)
        start.year(2014)
        start.logSig.connect(self.showLogMessage)
        start.show()
        start.informationProgress('Starting')

        start.updateProgress(10)
        start.informationProgress('Loading interface')
        self.tabifyDockWidget(
            self.ui.dockWidgetLogView,
            self.ui.dockWidgetTableView)

        start.updateProgress(20)
        start.informationProgress('Creating a container')
        self.container = container.ContainerDB()


        start.updateProgress(30)
        start.informationProgress('Loading preferences')
        
        self.readPreferences()

        start.updateProgress(50)
        start.informationProgress('Loading pdfwriter')
        self.pdfwriter = pdf_writer.MyDocTemplate(BaseDocTemplate,container=self.container) 

        start.updateProgress(60)
        start.informationProgress('Setting environment')

        start.updateProgress(90)
        start.informationProgress('Finishing to run')

        start.updateProgress(100)
        start.close()



        # Application ---------------------------------------------------------
        # Actions
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionTips.triggered.connect(self.tips)
        self.ui.actionPreferences.triggered.connect(
            lambda: preferences_dlg.PreferencesDialog(
                self.preferences, False,  self).exec_())
        # Signals
        self.logSig.connect(self.showLogMessage)

        # File ----------------------------------------------------------------
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionSaveAs.triggered.connect(self.saveFileAs)
        self.ui.actionPrint.triggered.connect(self.printFile)
        self.ui.actionImport.triggered.connect(self.importFile)
        self.ui.actionExport.triggered.connect(self.exportFile)
        self.ui.actionClose.triggered.connect(self.closeFile)

        # Section -------------------------------------------------------------
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
        self.ui.listWidgetSection.doubleClicked.connect(
            lambda: self.ui.lineEditSection.setText(
                self.ui.listWidgetSection.currentItem().text()))
        self.ui.listWidgetSection.itemSelectionChanged.connect(
            lambda: self.ui.lineEditSection.clear())
        self.ui.listWidgetSection.itemSelectionChanged.connect(
            self.updateSubSectionView)
        self.ui.listWidgetSection.itemSelectionChanged.connect(
            self.updateSentenceView)
        self.ui.listWidgetSection.itemSelectionChanged.connect(
            self.updateSelectedNumbers)
        # Properties
        self.ui.listWidgetSection.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        self.ui.listWidgetSection.setDragEnabled(False)

        # Subsection ----------------------------------------------------------
        # Buttons
        self.ui.pushButtonSubSectionAdd.clicked.connect(self.addSubSection)
        self.ui.pushButtonSubSectionRemove.clicked.connect(
            self.removeSubSection)
        self.ui.pushButtonSubSectionUpdate.clicked.connect(
            self.updateSubSection)
        # Actions
        self.ui.actionAddSubSection.triggered.connect(self.addSubSection)
        self.ui.actionRemoveSubSection.triggered.connect(self.removeSubSection)
        self.ui.actionUpdateSubSection.triggered.connect(self.updateSubSection)
        self.ui.actionTipsSubSection.triggered.connect(self.tipsSubSection)
        # Signals
        self.ui.listWidgetSubSection.doubleClicked.connect(
            lambda: self.ui.lineEditSubSection.setText(
                self.ui.listWidgetSubSection.currentItem().text()))
        self.ui.listWidgetSubSection.itemSelectionChanged.connect(
            lambda: self.ui.lineEditSubSection.clear())
        self.ui.listWidgetSubSection.itemSelectionChanged.connect(
            self.updateFunctionView)
        self.ui.listWidgetSubSection.itemSelectionChanged.connect(
            self.updateSentenceView)
        self.ui.listWidgetSubSection.itemSelectionChanged.connect(
            self.updateSelectedNumbers)
        # Properties
        self.ui.listWidgetSubSection.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        self.ui.listWidgetSubSection.setDragEnabled(False)

        # Function ------------------------------------------------------------
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
        self.ui.listWidgetFunction.doubleClicked.connect(
            lambda: self.ui.lineEditFunction.setText(
                self.ui.listWidgetFunction.currentItem().text()))
        self.ui.listWidgetFunction.itemSelectionChanged.connect(
            lambda: self.ui.lineEditFunction.clear())
        self.ui.listWidgetFunction.itemSelectionChanged.connect(
            self.updateSentenceView)
        self.ui.listWidgetFunction.itemSelectionChanged.connect(
            self.updateSelectedNumbers)
        # Properties
        self.ui.listWidgetFunction.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
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
        self.ui.checkBoxSection.clicked.connect(
            lambda: self.ui.tableWidgetSentence.setColumnHidden(
                0, not self.ui.checkBoxSection.isChecked()))
        self.ui.checkBoxSubSection.clicked.connect(
            lambda: self.ui.tableWidgetSentence.setColumnHidden(
                1, not self.ui.checkBoxSubSection.isChecked()))
        self.ui.checkBoxFunction.clicked.connect(
            lambda: self.ui.tableWidgetSentence.setColumnHidden(
                2, not self.ui.checkBoxFunction.isChecked()))
        self.ui.checkBoxSentence.clicked.connect(
            lambda: self.ui.tableWidgetSentence.setColumnHidden(
                3, not self.ui.checkBoxSentence.isChecked()))
        self.ui.checkBoxReference.clicked.connect(
            lambda: self.ui.tableWidgetSentence.setColumnHidden(
                4, not self.ui.checkBoxReference.isChecked()))
        self.ui.tableWidgetSentence.itemSelectionChanged.connect(
            self.updateSelectedNumbers)
        self.ui.checkBoxStrip.clicked.connect(self.updateSentenceView)
        self.ui.tableWidgetSentence.cellDoubleClicked.connect(self.getSentFromTableNDisplay)
        self.ui.tableWidgetSentence.cellClicked.connect(self.getSentFromTable)
        # Properties
        self.ui.tableWidgetSentence.setRowCount(0)
        self.ui.checkBoxStrip.setChecked(True)

        # Cleaning ----------------------------------------------------------
        self.clearAll()
        self.updateSectionView()
        self.updateSentenceView()
        
        if self.preferences['open_last'] and not self.firstTimeOpened:
            self.openFile(str(self.preferences['last_path']))

    def getSentFromTable(self, row,  column):
        """
        Get a sentence from table's click
        """
       
        self.ID = int(self.ui.tableWidgetSentence.item(row, 5).text())
        [(self.sent, self.ref)] = self.container.searchByID(self.ID)
        
    
    def getSentFromTableNDisplay(self, row,  column):

        """
        Get a sentence from table's doubleclick and display in text editor
        """
       
        self.getSentFromTable(row,  column)
       
        #self.ID = int(self.ui.tableWidgetSentence.item(row, 5).text())
        #[(self.sent, self.ref)] = self.container.searchByID(self.ID)
        
        self.ui.textEditSentence.setText(self.sent)
        self.ui.lineEditReference.setText(self.ref)


    def selectedTitles(self, selected_items):
        """
        Return a list of selected titles.

        Parameters:
        -----------
        selected_items: QList
                        Items from list or table view.

        Returns:
        titles: list(str)
                Returns converted list of string items.

        """
        titles = []
        for item in selected_items:
            titles.append(str(item.text()))
        return titles

    def updateSelectedNumbers(self):
        """Updates selected numbers from list and table views."""
        self.ui.labelSelectedSection.setText(
            str(len(self.ui.listWidgetSection.selectedItems())))
        self.ui.labelSelectedSubSection.setText(
            str(len(self.ui.listWidgetSubSection.selectedItems())))
        self.ui.labelSelectedFunction.setText(
            str(len(self.ui.listWidgetFunction.selectedItems())))
        self.ui.labelSelectedSentence.setText(
            str(len(self.ui.tableWidgetSentence.selectedItems())))

    def updateTotalNumbers(self):
        """Updates total numbers from list and table views."""
        sec = set()
        subs = set()
        func = set()
        sent = set()

        # @TODO: This can be better :), maybe a property of container
        for idv, secv, subsv, funcv, sentv, refv in self.container.listSentences():
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
        """Add a new section."""
        sec = str(self.ui.lineEditSection.text())

        if sec != '':
            self.container.addDB(sect=[sec])
            self.logSig.emit('A new section "{}" was added.'.format(sec))
            self.showMessageOnStatusBar(
                'A new section "{}" was added.'.format(sec))

        self.updateTotalNumbers()
        self.updateSectionView()

    def removeSection(self):
        """Remove a section."""
        sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())

        if sec != []:
            if self.removeQuestion("Section", sec) == QMessageBox.Yes:
                self.container.remove(sect=sec)
                self.showMessageOnStatusBar(
                    'Section(s) was removed.'.format(sec))

        self.updateTotalNumbers()
        self.updateSectionView()

    def updateSection(self):
        """Updates old section with new section."""
        old_sec = self.selectedTitles(
            self.ui.listWidgetSection.selectedItems())
        new_sec = str(self.ui.lineEditSection.text())

        if len(old_sec) != 1:
            QMessageBox.warning(
                self,
                self.tr('Update'),
                self.tr('Please select just one item to update.'),
                QMessageBox.Ok)
        elif new_sec != '':
            if self.updateQuestion("Section", (old_sec[0], new_sec)) == QMessageBox.Yes:
                self.container.update(section=[(new_sec, old_sec[0])])
                self.showMessageOnStatusBar(
                    'Section "{}" was updated to "{}".'.format(
                        old_sec[0],
                        new_sec))

        self.updateSectionView()

    def updateSectionView(self):
        """Updates section view."""
        sec = self.container.listSections()
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
        """Show tips for the section."""
        QMessageBox.information(self,
                                self.tr('Section Tips'),
                                self.tr('Sections are the main division of a \
scientific text. In summary, they are the titles of each section.'),
                                QMessageBox.Ok)

    # -----------------------------------------------------------------------
    # Sub Section methods
    # -----------------------------------------------------------------------

    def addSubSection(self):
        """Add a new Subsection."""
        sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        subs = str(self.ui.lineEditSubSection.text())

        if subs != '':
            self.container.addDB(sect=sec, subsect=[subs])
            self.showMessageOnStatusBar(
                'A new sub section "{}" was added.'.format(subs))

        self.updateTotalNumbers()
        self.updateSubSectionView()

    def removeSubSection(self):
        """Remove one subsection."""
        subs = self.selectedTitles(
            self.ui.listWidgetSubSection.selectedItems())

        if subs != []:
            if self.removeQuestion("Subsection", subs) == QMessageBox.Yes:
                self.container.remove(subsect=subs)
                self.showMessageOnStatusBar('A sub section was removed.')

        self.updateTotalNumbers()
        self.updateSubSectionView()

    def updateSubSection(self):
        """Updates one subsection."""
        old_subs = self.selectedTitles(
            self.ui.listWidgetSubSection.selectedItems())
        new_subs = str(self.ui.lineEditSubSection.text())

        if len(old_subs) != 1:
            QMessageBox.warning(
                self,
                self.tr('Update'),
                self.tr('Please select just one item to update.'),
                QMessageBox.Ok)
        elif new_subs != '':
            if self.updateQuestion("Subsection", (old_subs[0], new_subs)) == QMessageBox.Yes:
                self.container.update(subsection=[(new_subs, old_subs[0])])
                self.showMessageOnStatusBar(
                    'Sub section "{}" was updated to "{}".'.format(
                        old_subs[0],
                        new_subs))

        self.updateSubSectionView()

    def updateSubSectionView(self):
        """Updates subsection view."""
        
        sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        subs=self.container.listSubSections(qsections=sec)
        subs_all = self.container.listSubSections()
        self.ui.listWidgetSubSection.clear()
        subs_all = sorted(subs_all)
        
        if "Not Classified" in subs_all:
            subs_all.remove("Not Classified")
            subs_all.append("Not Classified")
        
        for row, value in enumerate(subs_all):
            item = QListWidgetItem(str(value))
            if value in subs:
                item.setBackground(QBrush(QColor(0, 0, 255, 30)))
            self.ui.listWidgetSubSection.addItem(item)
        
        self.ui.labelDisplayedSubSection.setText(str(len(subs)))
        self.updateFunctionView()
        self.updateSentenceView()

    def tipsSubSection(self):
        """Show tips for Subsection."""
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
        """Adds a new function."""
        sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        subs = self.selectedTitles(
            self.ui.listWidgetSubSection.selectedItems())
        func = str(self.ui.lineEditFunction.text())

        if func != '':
            self.container.addDB(sect=sec, subsect=subs, funct=[func])
            self.showMessageOnStatusBar(
                'A new function "{}" was added.'.format(func))

        self.updateTotalNumbers()
        self.updateFunctionView()

    def removeFunction(self):
        """Removes a function."""
        func = self.selectedTitles(self.ui.listWidgetFunction.selectedItems())

        if func != []:
            if self.removeQuestion("Function", func) == QMessageBox.Yes:
                self.container.remove(funct=func)
                self.showMessageOnStatusBar('A function has already removed.')

        self.updateTotalNumbers()
        self.updateFunctionView()

    def updateFunction(self):
        """Updates a function."""
        old_func = self.selectedTitles(
            self.ui.listWidgetFunction.selectedItems())
        new_func = str(self.ui.lineEditFunction.text())

        if len(old_func) != 1:
            QMessageBox.warning(
                self,
                self.tr('Update'),
                self.tr('Please select just one item to update.'),
                QMessageBox.Ok)
        elif new_func != '':
            if self.updateQuestion("Function", (old_func[0], new_func)) == QMessageBox.Yes:
                self.container.update(function=[(new_func, old_func[0])])
                self.showMessageOnStatusBar(
                    'Function "{}" was updated to "{}".'.format(
                        old_func[0],
                        new_func))

        self.updateFunctionView()

    def updateFunctionView(self):
        """Updates a function view."""
        
        sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        subs = self.selectedTitles(self.ui.listWidgetSubSection.selectedItems())
        func = self.container.listFunctions(qsections=sec,qsubsections=subs)
        func_all = self.container.listFunctions()
        self.ui.listWidgetFunction.clear()
        func_all = sorted(func_all)

        self.ui.labelDisplayedFunction.setText(str(len(func)))

        if "Not Classified" in func:
            func_all.remove("Not Classified")
            func_all.append("Not Classified")

        for row, value in enumerate(func_all):
            item = QListWidgetItem(str(value))
            if value in func:
                item.setBackground(QBrush(QColor(0, 0, 255, 30)))
            self.ui.listWidgetFunction.addItem(item)

        self.updateSentenceView()

    def tipsFunction(self):
        """Show tips for function."""
        QMessageBox.information(
            self,
            self.tr('Function Tips'),
            self.tr('Function explain what each sentence is.'),
            QMessageBox.Ok)

    # -----------------------------------------------------------------------
    # Sentence methods
    # -----------------------------------------------------------------------

    def adjustSentence(
            self,
            sent="",
            begin="{",
            end="}",
            replace_where='Inside markers',
            replace_by="..."):
        """Adjusts sentences to be displayed on the screen."""
        b = [match.start() for match in re.finditer(re.escape(begin), sent)]
        e = [match.end() for match in re.finditer(re.escape(end), sent)]

        # exception here b and e must have the same size!
        if(len(b) == len(e)):
            for i in range(0, len(b)):
                if(b[i] >= e[i]):
                    raise AssertionError(
                        "Delimiters aren't being used correctly!")

            r = []

            for i in range(0, len(b)):
                r.append(sent[b[i]:e[i]])

            if replace_where == 'Inside markers':
                for substring in r:
                    sent = sent.replace(substring, replace_by)
            else:
                if(r != []):
                    # @TODO: talvez colocar um erro em um else para este if!
                    aux = ''

                    if 0 not in b:
                        aux += replace_by + " "

                    for i in range(0, len(b) - 1):
                        aux += sent[b[i]:e[i]] + " " + replace_by + " "

                    if(e[len(b) - 1] == len(sent) - 1):
                        aux += sent[b[len(b) - 1]:e[len(e) - 1]]
                    else:
                        aux += sent[b[len(b) - 1]:e[len(e) - 1]
                                    ] + " " + replace_by + " "

                    sent = aux.replace(begin, "").replace(end, "")
        else:
            raise AssertionError("Delimiter number doesnt match!")

        return sent

    def addSentence(self):
        """Adds a new sentence."""
        # Getting information
        sec = self.selectedTitles(self.ui.listWidgetSection.selectedItems())
        subs = self.selectedTitles(
            self.ui.listWidgetSubSection.selectedItems())
        func = self.selectedTitles(self.ui.listWidgetFunction.selectedItems())
        sent = str(self.ui.textEditSentence.toPlainText())
        ref = str(self.ui.lineEditReference.text())
        # Cleaning
        self.ui.textEditSentence.clear()
        self.ui.lineEditReference.clear()

        if sent != '':
            # Insertting in DB
            self.container.addDB(
                sect=sec,
                subsect=subs,
                funct=func,
                phrase=[sent],
                ref=[ref])
            self.logSig.emit('A new sentence was added in \n Section(s):{} \n Sub Section(s): {} \n \
                                  Function(s): {} \n Sentence: {} \n Reference: {}'.format(sec, subs, func, sent, ref))
            self.showMessageOnStatusBar('A new sentence was added.')

        self.updateTotalNumbers()
        self.updateSentenceView()

    def removeSentence(self):
        """Removes a sentence."""
        
        #sent = self.selectedTitles(self.ui.tableWidgetSentence.selectedItems())
        
        sent = self.sent
        
        if sent != '':
            if self.removeQuestion("Sentence", [sent]) == QMessageBox.Yes:
                print 'Removing sentences: ',  sent
                self.container.remove(phrase=[sent])
                self.showMessageOnStatusBar('Sentence(s) was removed.')
                
        self.updateTotalNumbers()
        self.updateSentenceView()

    def updateSentence(self, old_sentence='', new_sentence=''):
        """Updates a sentence."""
       
        old_sent = self.sent
        old_ref = self.ref
        
        sent = str(self.ui.textEditSentence.toPlainText())
        ref = str(self.ui.lineEditReference.text())
        
        if sent != '' and ref != '' and old_sent != '' and old_ref != '':
            if self.updateQuestion("Sentence", (old_sent, sent)) == QMessageBox.Yes:
                self.container.upSent((old_sent,sent),(old_ref,ref))
                self.showMessageOnStatusBar(
                    'Sentence "{}" was updated to "{}".'.format(
                        old_sent,
                        sent))
                
        self.updateSentenceView()

    def updateSentenceView(self):
        """Updates a sentence view."""

        sections = self.selectedTitles(
            self.ui.listWidgetSection.selectedItems())
        sub_sections = self.selectedTitles(
            self.ui.listWidgetSubSection.selectedItems())
        functions = self.selectedTitles(
            self.ui.listWidgetFunction.selectedItems())
        sentences = self.container.listSentences(
            section=sections,
            subsection=sub_sections,
            function=functions)

        self.ui.tableWidgetSentence.clearContents()
        self.ui.tableWidgetSentence.setColumnCount(6)
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(
            0,
            QTableWidgetItem('Section'))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(
            1,
            QTableWidgetItem('Sub Section'))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(
            2,
            QTableWidgetItem('Function'))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(
            3,
            QTableWidgetItem('Sentence'))
        self.ui.tableWidgetSentence.setHorizontalHeaderItem(
            4,
            QTableWidgetItem('Reference'))

        #the last column will be always hidden cause it will contain the
        #unique ID from the entry. Its necessary to update properly.
        self.ui.tableWidgetSentence.setColumnHidden(5, True)

        row = 0
        strip = self.ui.checkBoxStrip.isChecked()
        self.ui.tableWidgetSentence.setRowCount(row)

        for idv, secv, subsv, funcv, sentv, refv in sentences:
            if sentv != u'NULL':
                # This must be provided by method of list sentences..not return NULL sentences.
                # Or maybe, put a check box to choose if will be show or not
                # null sentences.
                self.ui.tableWidgetSentence.setRowCount(row + 1)

                sec_item = QTableWidgetItem(str(secv))
                subs_item = QTableWidgetItem(str(subsv))
                func_item = QTableWidgetItem(str(funcv))
                sent_item = QTableWidgetItem(str(sentv))
                ref_item = QTableWidgetItem(str(refv))
                id_item = QTableWidgetItem(str(idv))

                self.ui.tableWidgetSentence.setItem(row, 0, sec_item)
                self.ui.tableWidgetSentence.setItem(row, 1, subs_item)
                self.ui.tableWidgetSentence.setItem(row, 2, func_item)
                self.ui.tableWidgetSentence.setItem(row, 3, sent_item)
                self.ui.tableWidgetSentence.setItem(row, 4, ref_item)
                self.ui.tableWidgetSentence.setItem(row, 5, id_item)

                if strip:
                    try:
                        marker = self.preferences['marker']
                        marker_beg = marker[:len(marker) / 2]
                        marker_end = marker[len(marker) / 2:]
                        sent_item.setText(
                            str(
                                self.adjustSentence(
                                    sentv,
                                    marker_beg,
                                    marker_end,
                                    self.preferences['replace_where'],
                                    self.preferences['replace_by'])))
                    except Exception:
                        sent_item.setText(str(sentv))
                        # Background red
                        sent_item.setBackground(QBrush(QColor(255, 0, 0, 127)))
                row += 1

        self.ui.labelDisplayedSentence.setText(str(row))

        self.ui.tableWidgetSentence.setColumnHidden(
            0, not self.ui.checkBoxSection.isChecked())
        self.ui.tableWidgetSentence.setColumnHidden(
            1, not self.ui.checkBoxSubSection.isChecked())
        self.ui.tableWidgetSentence.setColumnHidden(
            2, not self.ui.checkBoxFunction.isChecked())
        self.ui.tableWidgetSentence.setColumnHidden(
            3, not self.ui.checkBoxSentence.isChecked())
        self.ui.tableWidgetSentence.setColumnHidden(
            4, not self.ui.checkBoxReference.isChecked())

    def tipsSentence(self):
        """Show tips for sentence."""
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

    def openFile(self,  path=''):
        """Opens a new file."""
        if path == '':
            path = QFileDialog.getOpenFileName(self,
                                               self.tr('Open File'),
                                               self.tr(str(self.workspace)),
                                               self.tr('(*.db)'))[0]
        if path != '':
            self.closeFile()
            try:
                self.container.read_(path)
            except Exception:
                self.closeFile()
            else:
                self.setWindowTitle(__name__+" "+__version__+" - "+str(self.container.path))
                self.preferences['last_path'] = path
                self.updateSelectedNumbers()
                self.updateTotalNumbers()
                self.updateSectionView()
                self.isModified = False

    def saveFile(self):
        """" Saves the file that is being used."""
        if self.container.path == '':
            self.saveFileAs()
        else:
            self.container.write_()

    def saveFileAs(self):
        """" Saves a new file."""
        path = QFileDialog.getSaveFileName(self,
                                           self.tr('Save As'),
                                           self.tr(str(self.workspace)),
                                           self.tr('(*.db)'))[0]
        if path != '':
            self.container.write_(path)

    def printFile(self):
        """Generates a PDF file with all sentences included in database."""
        path = QFileDialog.getSaveFileName(self,
                                           self.tr('Save As'),
                                           self.tr(str(self.workspace)),
                                           self.tr('(*.pdf)'))[0]
        if path != '':
            self.pdfwriter.exportToPDF(path)

    def closeFile(self):
        """Closes current file."""
        if self.container.isModified:
            answer = QMessageBox.question(
                self,
                self.tr('Save'),
                self.tr('Do you want to save the current work?'),
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                QMessageBox.Yes)

            if answer == QMessageBox.Yes:
                self.saveFile()

        self.container.close_()
        self.setWindowTitle(__name__ + " " + __version__)
        self.clearAll()
        self.updateSelectedNumbers()
        self.updateTotalNumbers()
        self.updateSectionView()

    def exportFile(self):
        """Export file with extension."""

        path = QFileDialog.getSaveFileName(self,
                                           self.tr('Export File'),
                                           self.tr(str(self.workspace)),
                                           self.tr('(*.xml *.csv *.json)'))[0]
        if path != '':
            self.container.export_(path)

    def importFile(self):
        """Import file with extension."""

        # This is not general and should be moved to tips about importing
        # This should be here, because without this information
        # you cant open a csv file. We need to put more information
        # about other types too.
        #@TODO: show a dialog to choose separator and id
        QMessageBox.information(self,
                                self.tr('Import File'),
                                self.tr('Please, before you try import the file, ensure that if it is a:\
\nCSV:  separator is ; (semi collon)\
       \n quote char is " (double quote) and \
       \n quoting is for All elements.\
       \n Example: "SECTION";"SUB SECTION";"FUNCTION";"SENTENCE";"REFERENCE"\
       \n          "Abstract";"Gap";"Importance";"However, this problem still unsolved";""\
\nJSON: fields are list of list: \
       \n Example: [["SECTION", "SUB SECTION", "FUNCTION", "SENTENCE", "REFERENCE"],\
       \n           ["Abstract","Gap","Importance","However, this problem still unsolved",""]]'),
                                QMessageBox.Ok)

        path = QFileDialog.getOpenFileName(
            self,
            self.tr('Import File'),
            self.tr(
                os.path.dirname(str(self.workspace))),
            self.tr('(*.xml *.csv *.json)'))[0]

        if path != '':
            try:
                self.container.import_(path)
            except Exception as e:
                self.clearAll()
                QMessageBox.warning(
                    self,
                    self.tr('Import File'),
                    self.tr(
                        'We could not import the file. \nError:{}'.format(
                            str(e))),
                    QMessageBox.Ok)

        self.updateSectionView()
        self.updateSentenceView()

    # -----------------------------------------------------------------------
    # Application methods
    # -----------------------------------------------------------------------

    def setupWorkspace(self):
        """Setup user preferences."""

        os_sys = platform.system()
        if os_sys == 'Windows':
            self.workspace = os.path.abspath(self.preferences['win_workspace'])
        elif os_sys == 'Linux':
            self.workspace = os.path.abspath(self.preferences['lin_workspace'])
        elif os_sys == 'Mac':
            self.workspace = os.path.abspath(self.preferences['mac_workspace'])
          

    def readPreferences(self):
        """Reads preferences from file."""
        
        os_sys = platform.system()
        filepath = ''
        
        if os_sys == 'Windows':
            filepath = os.path.abspath(os.path.join(os.path.expanduser('~'),'scicorpus.ini'))
        elif os_sys == 'Linux' or os_sys == 'Mac':
            filepath = os.path.abspath(os.path.join(os.path.expanduser('~'),'.scicorpus.ini'))

        try:
            with codecs.open(filepath, 'rb', 'utf-8') as ini_file:
                text = ini_file.read()
                config = json.loads(str(text))
        except Exception:
            self.logSig.emit("File scicorpus.ini not found.")
            preferences_dlg.PreferencesDialog(self.preferences, True,  self).exec_()
            pass
        else:
            self.firstTimeOpened = False
            self.preferences = config
            self.logSig.emit("File scicorpus.ini was found.")
        finally:
            self.setupWorkspace()
            self.ui.checkBoxSection.setChecked(self.preferences['section'])
            self.ui.checkBoxSubSection.setChecked(self.preferences['subsection'])
            self.ui.checkBoxFunction.setChecked(self.preferences['function'])
            self.ui.checkBoxSentence.setChecked(self.preferences['sentence'])
            self.ui.checkBoxReference.setChecked(self.preferences['reference'])
            self.ui.checkBoxStrip.setChecked(self.preferences['strip'])

    def writePreferences(self):
        """Writes preferences on file."""
        
        os_sys = platform.system()
        
        if os_sys == 'Windows':
            filepath = os.path.abspath(os.path.join(os.path.expanduser('~'),'scicorpus.ini'))
        elif os_sys == 'Linux' or os_sys == 'Mac':
            filepath = os.path.abspath(os.path.join(os.path.expanduser('~'),'.scicorpus.ini'))
            
        self.preferences['section'] = self.ui.checkBoxSection.isChecked()
        self.preferences['subsection'] = self.ui.checkBoxSubSection.isChecked()
        self.preferences['function'] = self.ui.checkBoxFunction.isChecked()
        self.preferences['sentence'] = self.ui.checkBoxSentence.isChecked()
        self.preferences['reference'] = self.ui.checkBoxReference.isChecked()
        self.preferences['strip'] = self.ui.checkBoxStrip.isChecked()
        
        with codecs.open(filepath, 'wb', 'utf-8') as pref_file:
            json.dump(self.preferences, pref_file, indent=4, sort_keys=True)


    def writeSettings(self):
        """Write settings fo window state and geometry."""
        settings = QSettings("SciCorpus", "SciCorpus")
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("windowState", self.saveState())

    def readSettings(self):
        """Read settings of window state and geometry."""
        settings = QSettings("SciCorpus", "SciCorpus")
        self.restoreGeometry(settings.value("geometry").toByteArray())
        self.restoreState(settings.value("windowState").toByteArray())

    def clearAll(self):
        """Clear all viewers."""
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
        """Close event."""
        answer = QMessageBox.question(
            self,
            self.tr('Quit'),
            self.tr('Do you want to exit Sci Corpus?'),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.closeFile()
            self.writePreferences()
            self.writeSettings()
            event.accept()
        else:
            event.ignore()

    def showMessageOnStatusBar(self, msg):
        """Display message on status bar."""
        status_bar = self.statusBar()
        status_bar.clearMessage()
        status_bar.showMessage(str(msg), 5000)

    def showLogMessage(self, msg):
        """Show log message in log view."""
        time_now = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
        new_text = '{} || {}'.format(time_now, str(msg))
        self.ui.textEditLogView.append(new_text)
        scrolbar = self.ui.textEditLogView.verticalScrollBar()
        scrolbar.setValue(scrolbar.maximum())

    def tips(self):
        """Show tips about aplication."""
        self.notImplementedYet()

    def notImplementedYet(self):
        """Show tips for function."""
        QMessageBox.information(
            self,
            self.tr('Sorry'),
            self.tr('We have no implemented this function yet.'),
            QMessageBox.Ok)

    def removeQuestion(self, category='', who=[]):
        """Removes a section item."""

        return QMessageBox.question(
            self,
            self.tr('Remove'),
            self.tr(
                "Do you want to remove item(s) {} from {}?".format(
                    str(who)[1:-1],
                    category)),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)

    def updateQuestion(self, category, xxx_todo_changeme):
        """Updates a section item."""
        (old_who, new_who) = xxx_todo_changeme
        return QMessageBox.question(
            self,
            self.tr('Update'),
            self.tr(
                "Do you want to update item '{}' to '{}' in {}?".format(
                    old_who,
                    new_who,
                    category)),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)

    def about(self):
        """About shows the main information about the application."""
        QMessageBox.about(self,
                          self.tr('About {}'.format(__name__)),
                          self.tr('This software is a corpus manager, that allows you to trainer.\
\n\nFor more information, please, visite the page: <https://github.com/zericardo182/sci-corpus/wiki> \
\n\nThis software was created by: Daniel C. Pizetta,  Jose R.F. Ronqui and Thiago Campo.\
\n\n{}'.format(__version__)))

def main():

    argv = sys.argv
    app = QApplication(argv)
    main_window = MainWindow()
    
    style_sheet = ''
    style_path = ''

    if main_window.preferences['theme'] == 'Black':
        style_path = 'sci_corpus/ui/black_theme.sty'
    else:
        style_path = 'sci_corpus/ui/white_theme.sty'

    try:
        with open(os.path.abspath(style_path), 'rb') as style_file:
            style_sheet = str(style_file.read())
            app.setStyleSheet(style_sheet)

    except Exception as e:
        print 'Error in style sheet: ', e
        pass

    main_window.showMaximized()
    app.exec_()
