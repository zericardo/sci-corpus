#!/usr/bin/python

import sqlite3


def add(**kwargs):
	'''
	'''
	db = sqlite3.connect('CORPUS.db')
	cursor = db.cursor()
	
	if kwargs is not None:
                        
                ''' Adds a new section (if it doesnt exists)'''       
                sections = kwargs.get('section',[])
                
                cursor.execute("SELECT sectionName from section")
                sectionListRaw = cursor.fetchall()
                sectionList = []
                
                for sec in sectionListRaw:
                        sectionList.append(sec[0])
                
                for sec in sections:
                        if sec not in sectionList:
                                cursor.execute('''INSERT INTO section (sectionName) VALUES(?)''', (sec,))
                
                
                subsections = kwargs.get('subsection',[])
                
                cursor.execute("SELECT subSecName from subsec")
                subSectionListRaw = cursor.fetchall()
                subSectionList = []
                
                for subsec in subSectionListRaw:
                        subSectionList.append(subsec[0])
                
                for subsec in subsections:
                        if subsec not in subSectionList:
                                cursor.execute('''INSERT INTO subsec(subSecName) VALUES(?)''', (subsec,))
        
        
        
                newSectionList = list(set(sectionList+sections))
                print newSectionList
                for sec in sections:
                        cursor.execute("SELECT section_id FROM section WHERE sectionName=?",(sec,))
                
        
        

                functions = kwargs.get('function',[])
                
                cursor.execute("SELECT functionName from function")
                functionListRaw = cursor.fetchall()
                functionList = []
                
                for func in functionListRaw:
                        functionList.append(func[0])
                
                for func in functions:
                        if func not in functionList:
                                cursor.execute('''INSERT INTO function(functionName) VALUES(?)''', (func,) )
    
	db.commit()
	db.close()

try:
   #Creates or open the database
   db = sqlite3.connect('CORPUS.db')
   cur = db.cursor()
   
   cur.execute("DROP TABLE section")
   cur.execute("DROP TABLE subsec")
   cur.execute("DROP TABLE function")
   cur.execute("DROP TABLE secSubSec")
   
   cur.execute('''CREATE TABLE IF NOT EXISTS
                     section(section_id INTEGER PRIMARY KEY, sectionName TEXT)''')
                     
   cur.execute('''CREATE TABLE IF NOT EXISTS
                     subsec(subsec_id INTEGER PRIMARY KEY, subSecName TEXT)''')
   
   cur.execute('''CREATE TABLE IF NOT EXISTS
                     secSubSec( relSection_id INTEGER, relSubSec_id INTEGER,
                                FOREIGN KEY (relSection_id) REFERENCES section(section_id),
                                FOREIGN KEY (relSubSec_id) REFERENCES subsec(subsec_id)) ''' )
                     
   cur.execute('''CREATE TABLE IF NOT EXISTS
                     function(function_id INTEGER PRIMARY KEY, functionName TEXT)''')
   
   #cur.execute('''CREATE TABLE IF NOT EXISTS
   #                 secSubSecFunction(secSubSecFunction_id INTEGER PRIMARY KEY, 
   #                 secSubSecId INTEGER, functionId INTEGER )''')

   #cur.execute('''CREATE TABLE IF NOT EXISTS
   #                  phrase(phrase_id INTEGER PRIMARY KEY, sentence TEXT, ref TEXT)''')

   #cur.execute('''CREATE TABLE IF NOT EXISTS
   #                 secSubSecFunctionPhrase(secSubSecFunctionPhrase_id INTEGER PRIMARY KEY,
   #                 secSubSecFunctionId INTEGER, phraseId INTEGER )''')
   
   
                    
   db.commit()
   print('Connected to the database!\n')
   db.close()
   

   
except Excecption as e:
   cb.rollback()
   raise e

finally:
   
	db = sqlite3.connect('CORPUS.db')
	cur = db.cursor()
   
	add(section=['teuso','teusa'],subsection=['charlinho'],function=['exuxu'])
        
        add(section=['teuso','charle'])
        
        add(subsection=['charlinho','teusinho'])
        
        add(function=['exuxu','ze'])
        
	cur.execute("SELECT * FROM section")
         
	rows = cur.fetchall()
        
        print "section"
        
	for row in rows:
		print(row)
                
        print "sub section"
                
	cur.execute("SELECT * FROM subsec")
         
	rows = cur.fetchall()
         
	for row in rows:
		print(row)
                
        print "function"
                
	cur.execute("SELECT * FROM function")
         
	rows = cur.fetchall()
         
	for row in rows:
		print(row)
	
	db.close()





