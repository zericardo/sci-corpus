import os
import json
import codecs
import sqlite3
import csv
import xml.etree.ElementTree as ET
import StringIO as strio
from shutil import copy2

class ContainerDB():
    """
    Class container.
    """
    def __init__(self):
        self.__path = ''
        self.__defaultpath = '../examples/backup.db'
        self.__isModified = False
        self.createNconnectDB()


    def createNconnectDB(self, path=''):
        '''
        Make a sqlite connection and creates a table.
        If no path, the connection will be with memory
        otherwise, with the database file referenced by path
        '''

        try:
            if path != '':
                self.__dbfile = sqlite3.connect(path)
                self.__dbfile.text_factory = str
            else:
                self.__dbmem = sqlite3.connect(":memory:")
                self.__dbmem.text_factory = str

        except sqlite3.Error, err:
            print "[INFO creatNconnect] %s" % err

        else:
            if path != '':
                self.__dbfile.cursor().execute('''CREATE TABLE IF NOT EXISTS
                            corpus(id INTEGER PRIMARY KEY, sec TEXT, subsec TEXT,
                            func TEXT, phrase TEXT, ref TEXT)''')
                self.__dbfile.commit()
            else:
                self.__dbmem.cursor().execute('''CREATE TABLE IF NOT EXISTS
                            corpus(id INTEGER PRIMARY KEY, sec TEXT, subsec TEXT,
                            func TEXT, phrase TEXT, ref TEXT)''')
                self.__dbmem.commit()


    def importToMemory(self):
        '''
        This function imports a DB file to memory
        '''
        try:
             tempfile = strio.StringIO()
             for line in self.__dbfile.iterdump():
                 tempfile.write('%s\n' % line)
             self.__dbfile.close()
             tempfile.seek(0)

             self.__dbmem.cursor().execute('DROP TABLE corpus')
             self.__dbmem.cursor().executescript(tempfile.read())
             self.__dbmem.commit()

        except sqlite3.Error, err:
            print "[INFO importToMemory] %s" % err

    def importToDBFile(self):
        '''
        This function imports a memory table to DB file
        '''
        try:
             tempfile = strio.StringIO()
             for line in self.__dbmem.iterdump():
                 tempfile.write('%s\n' % line)
             tempfile.seek(0)

             self.__dbfile.cursor().executescript(tempfile.read())
             self.__dbfile.commit()
             self.__dbfile.close()
        except sqlite3.Error, err:
            print "[INFO importToDBFile] %s" % err


    def addDB(self,sect=['Not Classified'],subsect=['Not Classified'],funct=['Not Classified'],phrase=['NULL'],ref=['NULL']):

        cursor = self.__dbmem.cursor()

        if sect == ['']: sect = ['Not Classified']
        if subsect == ['']: subsect = ['Not Classified']
        if funct == ['']: funct = ['Not Classified']
        if phrase == ['']: phrase = ['NULL']
        if ref == ['']: ref = ['NULL']

        try:
            whatadd = [(a,b,c,d,e) for a in sect for b in subsect for c in funct for d in phrase for e in ref]
            cursor.executemany('''INSERT INTO corpus(sec,subsec,func,phrase,ref) VALUES(?,?,?,?,?)''',whatadd)
            
        except sqlite3.Error, err:
            print "[INFO addDB] %s" % err
            
        else:
            self.isModified  = True


    def listCategories(self,section=[],subsection=[],function=[]):

        cursor = self.__dbmem.cursor()

        secsubsecfunc = []
        subsecfunc = []
        functions = []
        final = []

        try:
            if section == [] and subsection == [] and function == []:
               cursor.execute('''SELECT DISTINCT sec, subsec, func FROM corpus''')
               secsubsecfunc = cursor.fetchall()
    
            if section != [] and subsection == [] and function == []:
               cursor.execute('SELECT DISTINCT sec, subsec, func FROM corpus WHERE sec in ({0})'.format(','.join('?' for _ in section)), section)
               subsecfunc = cursor.fetchall()
    
            if section != [] and subsection != [] and function == []:
               secsubsecTuple = [(a,b) for a in section for b in subsection]
               for i in range(len(secsubsecTuple)):
                  cursor.execute('''SELECT DISTINCT sec, subsec, func FROM corpus WHERE sec=? AND subsec=?''',secsubsecTuple[i])
                  functions.extend(cursor.fetchall())
                  
        except sqlite3.Error, err:
            print "[INFO listCategories] %s" % err
            
        finally:
            final.extend(secsubsecfunc)
            final.extend(subsecfunc)
            final.extend(functions)
            return final


    def listSentences(self,section=[],subsection=[],function=[]):

        cursor = self.__dbmem.cursor()

        phrases = []

        try:
            if section == [] and subsection == [] and function == []:
               cursor.execute('''SELECT DISTINCT sec, subsec, func, phrase, ref FROM corpus''')
               phrases.extend(cursor.fetchall())

            if section != [] and subsection == [] and function == []:
               cursor.execute('SELECT DISTINCT sec, subsec, func, phrase, ref FROM corpus WHERE sec in ({0})'.format(','.join('?' for _ in section)), section)
               phrases.extend(cursor.fetchall())

            if section != [] and subsection != [] and function == []:
               secsubsecTuple = [(a,b) for a in section for b in subsection]
               for i in range(len(secsubsecTuple)):
                  cursor.execute('''SELECT DISTINCT sec, subsec, func, phrase, ref FROM corpus WHERE sec=? AND subsec=?''',secsubsecTuple[i])
                  phrases.extend(cursor.fetchall())

            if section != [] and subsection != [] and function != []:
               secsubsecfuncTuple = [(a,b,c) for a in section for b in subsection for c in function]
               for i in range(len(secsubsecfuncTuple)):
                  cursor.execute('''SELECT DISTINCT sec, subsec, func, phrase, ref FROM corpus WHERE sec=? AND subsec=? AND func=?''',secsubsecfuncTuple[i])
                  phrases.extend(cursor.fetchall())
                
        except sqlite3.Error, err:
            print "[INFO listSentences] %s" % err
            
        finally:
            return phrases

    def listAll(self):
        '''
        return a list o tuples with all info
        '''
        cursor = self.__dbmem.cursor()

        allInfo = []

        try:
            cursor.execute('SELECT DISCTINC sec, subsec, func, phrase, ref from corpus')
            allInfo.append(cursor.fetchall())
        
        except sqlite3.Error, err:
            print "[INFO listAll] %s" % err
        
        finally:
            return allInfo


    def update(self, section=[('NULL','NULL')],subsection=[('NULL','NULL')],function=[('NULL','NULL')],phrase=[('NULL','NULL')],ref=[('NULL','NULL')]):

        cursor = self.__dbmem.cursor()

        try:
            if section != [('NULL','NULL')] and subsection == [('NULL','NULL')] and function == [('NULL','NULL')] and phrase == [('NULL','NULL')] and ref == [('NULL','NULL')]:
               cursor.execute('''UPDATE corpus
                              SET sec=? WHERE sec=?''',section[0])
    
            if section == [('NULL','NULL')] and subsection != [('NULL','NULL')] and function == [('NULL','NULL')] and phrase == [('NULL','NULL')] and ref == [('NULL','NULL')]:
               cursor.execute('''UPDATE corpus
                              SET subsec=? WHERE subsec=?''',subsection[0])
    
            if section == [('NULL','NULL')] and subsection == [('NULL','NULL')] and function != [('NULL','NULL')] and phrase == [('NULL','NULL')] and ref == [('NULL','NULL')]:
               cursor.execute('''UPDATE corpus
                              SET func=? WHERE func=?''',function[0])
    
            if section == [('NULL','NULL')] and subsection == [('NULL','NULL')] and function == [('NULL','NULL')] and phrase != [('NULL','NULL')] and ref == [('NULL','NULL')]:
               cursor.execute('''UPDATE corpus
                              SET phrase=? WHERE phrase=?''',phrase[0])
    
            if section == [('NULL','NULL')] and subsection == [('NULL','NULL')] and function == [('NULL','NULL')] and phrase == [('NULL','NULL')] and ref != [('NULL','NULL')]:
               cursor.execute('''UPDATE corpus
                              SET ref=? WHERE ref=?''',ref[0])
        
        except sqlite3.Error, err:
            print "[INFO update] %s" % err
            
        else:
            self.isModified  = True

    def remove(self,sect=[],subsect=[],funct=[],phrase=[]):

        cursor = self.__dbmem.cursor()

        try:
            if sect != [] and subsect == [] and funct == [] and phrase == []:
               whatup = [('Not Classified',a) for a in sect]
               self.update(section=whatup)
    
            if sect == [] and subsect != [] and funct == [] and phrase == []:
               whatup = [('Not Classified',a) for a in subsect]
               self.update(subsection=whatup)
    
            if sect == [] and subsect == [] and funct != [] and phrase == []:
               whatup = [('Not Classified',a) for a in funct]
               self.update(function=whatup)
    
            if sect == [] and subsect == [] and funct == [] and phrase != []:
               whatup = [('NULL',a) for a in phrase]
               self.update(phrase=whatup)
        
        except sqlite3.Error, err:
            print "[INFO remove] %s" % err
        else:
            self.isModified  = True


    def bulk_add(self, info):

        cursor = self.__dbmem.cursor()

        #print info

        try:
            cursor.executemany('INSERT INTO corpus(sec,subsec,func,phrase,ref) VALUES(?,?,?,?,?)',info)
        except sqlite3.Error, err:
            print "[INFO addbulk insert] %s" % err    
        else:
            self.isModified  = True

                
    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = os.path.abspath(path)

    @property
    def defaultpath(self):
        return self.__defaultpath

    @defaultpath.setter
    def defaultpath(self, path):
        self.__defaultpath = os.path.abspath(path)

    @property
    def dbfile(self):
        self.__dbfile

    @property
    def dbmem(self):
        self.__dbmem

    @property
    def isModified(self):
        """
        Shows the answer for is modified question.
        """
        return self.__isModified

    @isModified.setter
    def isModified(self, state):
        self.__isModified = state

    def write_(self, path=''):
        """
        Writes file in path or in self.path if not passed.
        """

        self.__dbmem.commit()

        if path == '':
            path = self.path
            try:
                shutil.copy2(path,self.__defaultpath)
                os.remove(path)
            except OSError, e:
                print ("Error: %s - %s." % (e.filename,e.strerror))
            else:
                self.createNconnectDB(path)
                self.importToDBFile()
        else:
            self.path = path
            try:
                os.remove(path)
            except OSError, e:
                print ("Error: %s - %s." % (e.filename,e.strerror))
            finally:
                self.createNconnectDB(path)
                self.importToDBFile()

        self.isModified = False

    def read_(self,  path):
        """
        Reads file.
        """

        try:
            self.createNconnectDB(path)
            self.importToMemory()
        except Exception:
            raise
        else:
            self.path = path
            self.isModified = False


    def close_(self):
        """
        Clear all fields.
        """

        try:
           self.__dbmem.close()
        except sqlite3.Error, err:
            print "[INFO line 326] %s" % err
        else:
           self.__path = ''
           self.__isModified = False
        finally:
            self.createNconnectDB()


    def import_(self,  path=''):
        """
        Import file as XML, JSON, DB.
        """
        # @TODO: We need to implement a signal to send a log message.
        print 'Importing from: ',  path

        path = os.path.abspath(path)
        ext = os.path.splitext(path)[1]

        if (ext == '.xml') or (ext == '.XML'):
            print "Importing XML ..."
            
            try:
                tree = ET.parse(path)
                root = tree.getroot()
            
            except ET.ParseError, err:
                print "[INFO xml import] %s" % err
            
            else:
                info = []
                
                try:
                    for w in root.findall('INFOPIECE'):
                        sec = w.find('SECTION').text
                        if sec == None: sec = 'Not Classified'
                        subs = w.find('SUBSECTION').text
                        if subs == None: subs = 'Not Classified'
                        func = w.find('FUNCTION').text
                        if func == None: func = 'Not Classified'
                        sent = w.find('PHRASE').text
                        if sent == None: sent = 'Not Classified'
                        ref = w.find('REF').text
                        if ref == None: ref = 'Not Classified'
                        
                        info.append((sec.encode("utf-8"), subs.encode("utf-8"), func.encode("utf-8"), sent.encode("utf-8"), ref.encode("utf-8")))
            
                        #print info
            
                except ET.ParseError, err:
                    print "[INFO xml import] %s" % err
                
                else:
                    self.bulk_add(info)
                    self.isModified = True

        elif (ext == '.csv') or (ext == '.CSV'):
            print "Importing CSV ..."
            with codecs.open(path, 'rb', 'utf-8') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
                row_number = 0
                for row in spamreader:
                    if row_number != 0:
                        [sec,  subs,  func,  sent,  ref]  = row
                        # Splitting many fields in the same category
                        sec = [x.encode("utf-8") for x in sec.split(',')]
                        subs = [x.encode("utf-8") for x in subs.split(',')]
                        func = [x.encode("utf-8") for x in func.split(',')]
                        self.addDB(sect=sec,subsect=subs,funct=func,phrase=[sent.encode("utf-8")],ref=[ref.encode("utf-8")])
                    row_number += 1                    
        elif (ext == '.json') or (ext == '.JSON'):
            print "Importing JSON ..."
                    
        
    def export_(self,  path=''):
        """
        Export file as XML, JSON, DB.
        """
        print 'Exporting to: ',  path

        path = os.path.abspath(path)
        ext = os.path.splitext(path)[1]
        
        if (ext == '.xml') or (ext == '.XML'):
            print "Exporting XML ..."

                
        elif (ext == '.csv') or (ext == '.CSV'):
            print "Exporting CSV ..."
            
        elif (ext == '.json') or (ext == '.JSON'):
            print "Exporting JSON ..."

    def crazyRepetition(self, sBase="", sConnect="",  sItems =[]):
        """
        Repeats the sentence in loop, avoiding extra work.

        <Args>
        sBase: String that will be repeated n times.
        sConnect: String that will connect all the different sBase strings.
        sItems: String list that will be replaced in the '?' signal on the sBase
                sentences, making new ones.
        <Returns>
        sFinal: A string composed by all len(sItens) strings linked together with
                sConnect string. 
        """   
   
        sFinal=''

        if(len(sItems)>0):
      
            queryList = []

            for item in sItems:
                queryList.append(sBase.replace("?","\""+item+"\""))

            if(len(sItems)==1):
                sFinal = queryList[0]
            else:
                for i in range(0,len(queryList)-1):
                    sFinal += queryList[i]+" "+sConnect+" "+queryList[i+1]
         

        else:
            raise AssertionError("Number of itens in the sItens is incompatible!")

        return sFinal

