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
                db.commit()
                
                #----------------------------------------------------------------------------------------

		''' Adds a new subsection (if it doesnt exists)'''       

		subsections = kwargs.get('subsection',[])
                
                cursor.execute("SELECT subSecName from subsec")
                subSectionListRaw = cursor.fetchall()
                subSectionList = []
                
                for subsec in subSectionListRaw:
                        subSectionList.append(subsec[0])
                
                for subsec in subsections:
                        if subsec not in subSectionList:
                                cursor.execute('''INSERT INTO subsec(subSecName) VALUES(?)''', (subsec,))
		db.commit()
        
		#----------------------------------------------------------------------------------------
		
		''' Adds a new relation between Section and Subsection (if it doesnt exists)'''

		sectionIdList = []
                for sec in sections:
                        cursor.execute("SELECT section_id FROM section WHERE sectionName=?",(sec,))
			sectionIdList.append(cursor.fetchone())

		subsecIdList = []
		for subsec in subsections:
			cursor.execute("SELECT subsec_id FROM subsec WHERE subSecName=?",(subsec,))
			subsecIdList.append(cursor.fetchone())

		cursor.execute("SELECT relSection_id, relSubSec_id from secSubSec")
                relSecSubSecList = cursor.fetchall()
					
		for idSec in sectionIdList:
			for idSubSec in subsecIdList:
				if (idSec[0], idSubSec[0]) not in relSecSubSecList:
					cursor.execute("INSERT INTO secSubSec (relSection_id, relSubSec_id)  VALUES(?, ?)", (idSec[0], idSubSec[0],))
				
                db.commit()
        
		#----------------------------------------------------------------------------------------
		
		''' Adds a new Function (if it doesnt exists)'''

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
		
		#----------------------------------------------------------------------------------------
		
		'''Adds a new relation between Function and Rel1 (if it doesnt exists) '''

		funcIdList = []
                for func in functions:
                        cursor.execute("SELECT function_id FROM function WHERE functionName=?",(func,))
			funcIdList.append(cursor.fetchone())

		rel1IdList = []
		for idSec in sectionIdList:
			for idSubSec in subsecIdList:
				cursor.execute("SELECT secSubSec_id FROM secSubSec WHERE relSection_id=? AND relSubSec_id=?",(idSec[0], idSubSec[0]))
				rel1IdList.append(cursor.fetchone())

		cursor.execute("SELECT relFunc_id, relSecSubSec_id FROM secSubSecFunc")
                relSecSubSecFuncList = cursor.fetchall()
					
		for idFunc in funcIdList:
			for idRel1 in rel1IdList:
				if (idFunc[0], idRel1[0]) not in relSecSubSecFuncList:
					cursor.execute("INSERT INTO secSubSecFunc (relFunc_id, relSecSubSec_id)  VALUES(?, ?)", (idFunc[0], idRel1[0],))

		db.commit()

	        #----------------------------------------------------------------------------------------
		
		''' Adds a new Sentence (if it doesnt exists)'''

                sentences = kwargs.get('sentence',[])
                
                cursor.execute("SELECT phrase from sentence")
                phraseListRaw = cursor.fetchall()
                phraseList = []
                
                for pha in phraseListRaw:
                        phraseList.append(pha[0])
                
                for pha in sentences:
                        if pha not in phraseList:
                                cursor.execute('''INSERT INTO sentence(phrase) VALUES(?)''', (pha,) )
    
		db.commit()
				

		#----------------------------------------------------------------------------------------
		
		'''Adds a new relation between Phrase and Rel2 (if it doesnt exists) '''

		sentIdList = []
                for sent in sentences:
                        cursor.execute("SELECT sentence_id FROM sentence WHERE phrase=?",(sent,))
			sentIdList.append(cursor.fetchone())

		rel2IdList = []
		for idFunc in funcIdList:
			for idRel1 in rel1IdList:
				cursor.execute("SELECT secSubSecFunc_id FROM secSubSecFunc WHERE relFunc_id=? AND relSecSubSec_id=?", (idFunc[0],idRel1[0]))
				rel2IdList.append(cursor.fetchone())

		cursor.execute("SELECT relSentence_id, relSecSubSecFunc_id FROM secSubSecFuncSentence")
                relSecSubSecFuncSentenceList = cursor.fetchall()
		
		for idSent in sentIdList:
			for idRel2 in rel2IdList:
				if (idSent[0], idRel2[0]) not in relSecSubSecFuncSentenceList:
					cursor.execute("INSERT INTO secSubSecFuncSentence (relSentence_id, relSecSubSecFunc_id)  VALUES(?, ?)", (idSent[0], idRel2[0],))

		db.commit()

	        #----------------------------------------------------------------------------------------
		
		
	db.close()



def listCategories():
	'''
	'''
	db = sqlite3.connect('CORPUS.db')
	cursor = db.cursor()
	
	cursor.execute("SELECT section_id, sectionName from section")
	sectionListRaw = cursor.fetchall()
	
	cursor.execute("SELECT subsec_id, subSecName from subsec")
        subSectionListRaw = cursor.fetchall()
	
	cursor.execute("SELECT secSubSec_id, relSection_id, relSubSec_id from secSubSec")
        relSecSubSecList = cursor.fetchall()
                
        cursor.execute("SELECT function_id, functionName from function")
        functionListRaw = cursor.fetchall()
                
        cursor.execute("SELECT secSubSecFunc_id, relFunc_id, relSecSubSec_id FROM secSubSecFunc")
        relSecSubSecFuncList = cursor.fetchall()
	
	return (sectionListRaw, subSectionListRaw, relSecSubSecList, functionListRaw, relSecSubSecFuncList)


def listSentence(sections, subSections, functions):
  
  
        functions1 = [(a,) for a in functions] 
	idFuncList = []
	cursor.executemany("SELECT function_id FROM function WHERE functionName=?",functions1)
	idFuncList.append(cursor.fetchall())


	cursor.executemany("SELECT relSecSubSec_id FROM secSubSecFunc WHERE relFunc_id=?",idFuncList)
        rel2IdList.append(cursor.fetchall())
	
        cursor.executemany("SELECT relSection_id, relSubSec_id FROM secSubSec WHERE secSubSec_id=?",rel2IdList)
        secSubSecIdTuple.append(cursor.fetchall())
        
        subSections1 = [(a,) for a in subSections] 
	idSubSecList = []
	cursor.executemany("SELECT subsec_id FROM subsec WHERE subSecName=?",subSections1)
	idSubSecList.append(cursor.fetchall())
        
        sections1 = [(a,) for a in sections] 
	idSecList = []
	cursor.executemany("SELECT section_id FROM section WHERE sectionName=?",sections1)
	idSecList.append(cursor.fetchall())

	
      

try:
   #Creates or open the database
   db = sqlite3.connect('CORPUS.db')
   cur = db.cursor()
   
   #cur.execute("DROP TABLE section")
   #cur.execute("DROP TABLE subsec")
   #cur.execute("DROP TABLE function")
   #cur.execute("DROP TABLE secSubSec")
   #cur.execute("DROP TABLE secSubSecFunc")
   #cur.execute("DROP TABLE sentence")
   #cur.execute("DROP TABLE secSubSecFuncSentence")
   
   
   cur.execute('''CREATE TABLE IF NOT EXISTS
                     section(section_id INTEGER PRIMARY KEY, sectionName TEXT)''')
                     
   cur.execute('''CREATE TABLE IF NOT EXISTS
                     subsec(subsec_id INTEGER PRIMARY KEY, subSecName TEXT)''')
   
   cur.execute('''CREATE TABLE IF NOT EXISTS
                     secSubSec( secSubSec_id INTEGER PRIMARY KEY, relSection_id INTEGER, relSubSec_id INTEGER,
                                FOREIGN KEY (relSection_id) REFERENCES section(section_id),
                                FOREIGN KEY (relSubSec_id) REFERENCES subsec(subsec_id)) ''' )
                     
   cur.execute('''CREATE TABLE IF NOT EXISTS
                     function(function_id INTEGER PRIMARY KEY, functionName TEXT)''')
   
   cur.execute('''CREATE TABLE IF NOT EXISTS
                    secSubSecFunc(secSubSecFunc_id INTEGER PRIMARY KEY, relFunc_id INTEGER, relSecSubSec_id INTEGER, 
                    FOREIGN KEY (relFunc_id) REFERENCES function(function_id),
                    FOREIGN KEY (relSecSubSec_id) REFERENCES secSubSec(secSubSec_id)) ''')

   cur.execute('''CREATE TABLE IF NOT EXISTS
                     sentence(sentence_id INTEGER PRIMARY KEY, phrase TEXT)''')

   cur.execute('''CREATE TABLE IF NOT EXISTS
                    secSubSecFuncSentence(secSubSecFuncSentence_id INTEGER PRIMARY KEY,
                    relSentence_id INTEGER, relSecSubSecFunc_id INTEGER, 
                    FOREIGN KEY (relSentence_id) REFERENCES sentence(sentence_id), 
                    FOREIGN KEY (relSecSubSecFunc_id) REFERENCES secSubSecFunc(secSubSecFunc_id))''')
   
   
                    
   db.commit()
   print('Connected to the database!\n')
   db.close()
   



finally:
   
	db = sqlite3.connect('CORPUS.db')
	cur = db.cursor()
   
	add(section=['teuso','teusa'],subsection=['charlinho'],function=['exuxu'],sentence=['oi oi oi'])
	add(section=['guizinho','teusa'],subsection=['charlinho', 'caralinho'],function=['pizetta','plato'])
        
        add(section=['teuso','charle'])
        
        add(subsection=['charlinho','teusinho'])
        
        add(function=['exuxu','ze'])
        
        '''
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

	print "Relation1"
                
	cur.execute("SELECT * FROM secSubSec")
         
	rows = cur.fetchall()
         
	for row in rows:
		print(row)

	print "Relation2"
                
	cur.execute("SELECT * FROM secSubSecFunc")
         
	rows = cur.fetchall()
         
	for row in rows:
		print(row)
	'''
	
	print listCategories()
	
	
	db.close()





