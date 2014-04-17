#!/usr/bin/python

import sqlite3


def add(section=['NULL'],subsection=['NULL'],function=['NULL'],phrase=['NULL']):
        
        db = sqlite3.connect('CORPUS.db')
        cursor = db.cursor()
        
        whatadd = [(a,b,c,d) for a in section for b in subsection for c in function for d in phrase]

        cursor.executemany('''INSERT INTO corpus(sec,subsec,func,phrase) VALUES(?,?,?,?)''',whatadd)
                
        db.commit()
        db.close()

def listCategories(section=[],subsection=[],function=[]):
        
        db = sqlite3.connect('CORPUS.db')
        cursor = db.cursor()
        
        sections = []
        subsections = []
        functions = []
        
        if section == [] and subsection == [] and function == []:
           cursor.execute('''SELECT DISTINCT sec FROM corpus''')
           sections = cursor.fetchall()
                
        if section != [] and subsection == [] and function == []:
           cursor.execute('SELECT DISTINCT subsec FROM corpus WHERE sec in ({0})'.format(','.join('?' for _ in section)), section)
           subsections = cursor.fetchall()
              
        if section != [] and subsection != [] and function == []:
           secsubsecTuple = [(a,b) for a in section for b in subsection]
           
           for i in range(len(secsubsecTuple)):
              cursor.execute('''SELECT DISTINCT func FROM corpus WHERE sec=? AND subsec=?''',secsubsecTuple[i])
              functions.append(cursor.fetchall())
   
   
        db.close()
        
        sectionsFinal = []
        subsectionsFinal = []
        functionsFinal = []
        
        for i in sections:
           sectionsFinal.append(i[0])
        
        for i in subsections:
           subsectionsFinal.append(i[0])
           
        for i in functions:
           functionsFinal.append(i[0])

        return [sectionsFinal,subsectionsFinal,functionsFinal]

   

def listSentences(section=[],subsection=[],function=[]):

        db = sqlite3.connect('CORPUS.db')
        cursor = db.cursor()
        
        phrases = []

        if section == [] and subsection == [] and function == []:
           cursor.execute('''SELECT DISTINCT phrase FROM corpus''')
           phrases = cursor.fetchall()
        
        if section != [] and subsection == [] and function == []:
           cursor.execute('SELECT DISTINCT phrase FROM corpus WHERE sec in ({0})'.format(','.join('?' for _ in section)), section)
           phrases = cursor.fetchall()
        
        if section != [] and subsection != [] and function == []:
           secsubsecTuple = [(a,b) for a in section for b in subsection]
           
           for i in range(len(secsubsecTuple)):
              cursor.execute('''SELECT DISTINCT phrase FROM corpus WHERE sec=? AND subsec=?''',secsubsecTuple[i])
              phrases.append(cursor.fetchall())
        
        if section != [] and subsection != [] and function != []:
           secsubsecfuncTuple = [(a,b,c) for a in section for b in subsection for c in function]
           
           for i in range(len(secsubsecfuncTuple)):
              cursor.execute('''SELECT DISTINCT phrase FROM corpus WHERE sec=? AND subsec=? AND func=?''',secsubsecfuncTuple[i])
              phrases.append(cursor.fetchall())
        
        phrasesFinal = []
        
        for i in phrases:
           phrasesFinal.append(i[0])
        
        return phrasesFinal
        
def removePhrase(section=['NULL'],subsection=['NULL'],function=['NULL'],phrase=['NULL']):

        db = sqlite3.connect('CORPUS.db')
        cursor = db.cursor()
        
        whatrm = [(a,b,c,d) for a in section for b in subsection for c in function for d in phrase]
        
        cursor.executemany('''DELETE FROM corpus WHERE sec=? AND subsec=? AND func=? and phrase=?''',whatrm)
        
        db.commit()
        db.close()

def update(section=[('NULL','NULL')],subsection=[('NULL','NULL')],function=[('NULL','NULL')],phrase=[('NULL','NULL')]):
        
        db = sqlite3.connect('CORPUS.db')
        cursor = db.cursor()

        if section != [('NULL','NULL')] and subsection == [('NULL','NULL')] and function == [('NULL','NULL')] and phrase == [('NULL','NULL')]:
           cursor.execute('''UPDATE corpus 
                          SET sec=? WHERE sec=?''',section[0])
        
        if section == [('NULL','NULL')] and subsection != [('NULL','NULL')] and function == [('NULL','NULL')] and phrase == [('NULL','NULL')]:
           cursor.execute('''UPDATE corpus 
                          SET subsec=? WHERE subsec=?''',subsection[0])        

        if section == [('NULL','NULL')] and subsection == [('NULL','NULL')] and function != [('NULL','NULL')] and phrase == [('NULL','NULL')]:
           cursor.execute('''UPDATE corpus 
                          SET function=? WHERE function=?''',function[0]) 

        if section == [('NULL','NULL')] and subsection == [('NULL','NULL')] and function == [('NULL','NULL')] and phrase != [('NULL','NULL')]:
           cursor.execute('''UPDATE corpus 
                          SET phrase=? WHERE phrase=?''',phrase[0]Ad) 
        
        db.commit()
        db.close()

try:
   #Creates or open the database
   db = sqlite3.connect('CORPUS.db')
   cur = db.cursor()
 
   cur.execute('''DROP TABLE corpus''')
 
   cur.execute('''CREATE TABLE IF NOT EXISTS
                     corpus(id INTEGER PRIMARY KEY, sec TEXT, subsec TEXT,
                     func TEXT, phrase TEXT)''')
                     
   db.commit()
   print('Connected to the database!\n')
   db.close()
   



finally:
   
	db = sqlite3.connect('CORPUS.db')
	cur = db.cursor()
   
	add(section=['teuso','teusa'],subsection=['charlinho'],function=['exuxu'],phrase=['oi oi oi'])
        add(section=['teuso'],subsection=['charlinho'],function=['tiago'],phrase=['to cansado'])
        
	#add(section=['guizinho','teusa'],subsection=['charlinho', 'caralinho'],function=['pizetta','plato'])
        
        #add(section=['teuso','charle'])
        print listCategories(section=['teuso'],subsection=['charlinho'])
        print listSentences(section=['teuso'])
        
        update(section=[('teuso','teuso1')])
        
        removePhrase(section=['teuso'],subsection=['charlinho'],function=['tiago'],phrase=['to cansado'])
        print listCategories(section=['teuso'],subsection=['charlinho'])
        print listSentences(section=['teuso'])
        
        #add(subsection=['charlinho','teusinho'])
        
        #add(function=['exuxu','ze'])
        
	#cur.execute("SELECT * FROM corpus")
         
	#rows = cur.fetchall()
              
	#for row in rows:
	#	print(row)
                
	

	db.close()





