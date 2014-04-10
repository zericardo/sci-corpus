#!/usr/bin/python3

# ------Tiago de Campos------
# This script will handle the CORPUS required by Scientific Writing course.
# I will use a sqlite database to store the data.
# The data discrimination will be BASED (NOT THE SAME) on the ScipoFarmacia tool.
# www.nilc.icmc.usp.br/scipo-farmacia


import sqlite3
from aux_functions import *

try:
   #Creates or open the database
   db = sqlite3.connect('CORPUS.db')
   cur = db.cursor()
   #cur.execute('''DROP TABLE CORPUS''')
   cur.execute('''CREATE TABLE IF NOT EXISTS
                     CORPUS(id INTEGER PRIMARY KEY, phrase TEXT, function TEXT, ref TEXT)''')
                     
   db.commit()
   
   print('Connected to the database!\n')
   
except Excecption as e:
   cb.rollback()
   raise e

finally:
   
   ans=True
   
   while ans:
      
      print("""
      
                  @@@@@@@@@@ TIAGO DE CAMPOS @@@@@@@@@@
                  
                     !!!!!! BETA TEST VERSION !!!!!!!
                     
            IF YOU CHOOSE TO INSET BY A XML FILE, MAKE SURE TO NOT INCLUDE
            THE SAME PHRASE AGAIN. THIS PROGRAMA DOESNT HANDLE DUPLICATED
            PHRASES!
            
      """)
      
      
      print("""
      1. Help
      2. Add manually a phrase
      3. Select a file to import
      4. Make a search
      5. Print all entries (use with care)
      6. Exit/Quit
      """)
      
      ans=input("What would you like to do? ")
      
      if ans=="1":
         call_help()
      
      elif ans=="2":
         print("Add manually a phrase \n")
         add_phrase(db)
         
      elif ans=="3":
         print("Select a file to import \n")
         filename=input('Enter with a path/name to the XML file:\n')
         bulk_add(db,filename)
         
      elif ans=="4":
         print("Make a search \n")
         phrases_searh(db)
      
      elif ans=="5":
         print("Print all entries \n")
          
         cur.execute("SELECT * FROM CORPUS")
         
         rows = cur.fetchall()
         
         for row in rows:
            print(row)
         
      elif ans=="6":
         print("Goodbye \n") 
         ans = None
         
      else:
         print("Not Valid Choice Try again \n")


   db.close()


   
