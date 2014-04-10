import xml.etree.ElementTree as ET

def call_help():
   print("""
   Original por Paulo Eduardo de Faria Junior - fariajunior.pe@gmail.com
   Atualizado e portado para Python por Tiago de Campos - tiagocampo@gmail.com

   Info gerais:
   
   Você pode tanto inserir informações indivíduais ou criar um arquivo .xml 
   com a estrutura abaixo e importá-lo para a base de dados.
   
   Os trechos das frases entre {} são as partes que podem ser reutilizadas.

   Explicando as tags:
  
   <ARTINFO>: tag mestre, resume informações para utilizar na confecção de 
              artigos. Informações entenda-se como frases modelo de artigos
              escritos por nativos.
     <INFOPIECE>: pedaço de informação retirada de um artigo.
        <PHRASE>: a frase em si, ou parte dela, retirada de um artigo ou 
                  texto de nativos. O que está entre colchetes pode ser 
                  desconsiderado e não afeta o entendimento da mesma
               [Eq]: equação numerada no meio da página, dando espaço e 
                     continuando a sentença depois ou não
               [eq]: equação dentro da frase, sem numeração 
               [sim]: símbolo
               [cit]: citação
       <FUNCTION>: função da frase segundo sua utilidade (pode ter mais 
                   de uma função). Se for o caso favor fazer duas entradas
                   modificando a função. Entre chaves [] é a palavra que 
                  vai para a tag <FUNCTION> na base de dado
                => Context
                  ++> Introducing stuff _____________________ [introstuff]
                  ++> Introducing with references ___________ [introref]
                      -> only when there is explicit mention of references
                => Gap ______________________________________ [gap]
                => Purposes
                  ++> Just purposes _________________________ [justpur]
                  ++> Purposes + Metodology _________________ [purmet]
                  ++> Purposes + Results ____________________ [purres]
                => Article structure ________________________ [structure]
                => Motivation and/or value of the research __ [motval]
                => Methodology ______________________________ [methodology]
                => Results and discussion
                  ++> Showing results _______________________ [showres]
                  ++> Discussing results ____________________ [disres]
                  ++> Comparing results _____________________ [compres]
                => Figures/tables caption ___________________ [caption]
                => Conclusions ______________________________ [conclusions]
                => Acknowledgments __________________________ [acknow]
                => Nice Words _______________________________ [words]
       <REF>: revista de onde foi retirada a frase (jornal-volume-pagina-ano).

   Para não deixar a TAG em branco, colocarei um traço -.
   """)

#-----------------------------------------------------------------------
# Add a phrase manually, one by one
#
#-----------------------------------------------------------------------
def add_phrase(db):
   
   cursor = db.cursor()
   
   phrase1=input("Enter the selected PHRASE:\n")
   function1=input("What is the function of this phrase?\n")
   ref1=input("Some referece to know where this phrase came from: \n")
   
   cursor.execute('''INSERT INTO CORPUS(phrase, function, ref) VALUES(?,?,?)''',
     (phrase1,function1,ref1))
   
   db.commit()

   print("Phrase added \n")

#-----------------------------------------------------------------------
# Search phrases by its function
#
#-----------------------------------------------------------------------
def phrases_searh(db):
      
   cursor = db.cursor()
   
   print("""
          <FUNCTION>: função da frase segundo sua utilidade (pode ter mais 
                   de uma função). Se for o caso favor fazer duas entradas
                   modificando a função. Entre chaves [] é a palavra que 
                  vai para a tag <FUNCTION> na base de dado
                => Context
                  ++> Introducing stuff _____________________ [introstuff]
                  ++> Introducing with references ___________ [introref]
                      -> only when there is explicit mention of references
                => Gap ______________________________________ [gap]
                => Purposes
                  ++> Just purposes _________________________ [justpur]
                  ++> Purposes + Metodology _________________ [purmet]
                  ++> Purposes + Results ____________________ [purres]
                => Article structure ________________________ [structure]
                => Motivation and/or value of the research __ [motval]
                => Methodology ______________________________ [methodology]
                => Results and discussion
                  ++> Showing results _______________________ [showres]
                  ++> Discussing results ____________________ [disres]
                  ++> Comparing results _____________________ [compres]
                => Figures/tables caption ___________________ [caption]
                => Conclusions ______________________________ [conclusions]
                => Acknowledgments __________________________ [acknow]
                => Nice Words _______________________________ [words]
   """)
   
   func1=input("Enter the desired function: \n")
            
   cursor.execute("SELECT * FROM CORPUS WHERE function=?", (func1,))
    
   db.commit()

   rows = cursor.fetchall()
   print("\n")
   for row in rows:
      print(row)
      print("\n")

#-----------------------------------------------------------------------
# Reads a xml file and import its data
#
#-----------------------------------------------------------------------
def bulk_add(db,filename):
            
   cursor = db.cursor()
   
   tree = ET.parse(filename)      
   root = tree.getroot()
      
   info = [(w.find('PHRASE').text, w.find('FUNCTION').text, w.find('REF').text) for w in root.findall('INFOPIECE')]
      
   cursor.executemany('''INSERT INTO CORPUS(phrase, function, ref) VALUES(?,?,?)''',
     info)
   
   db.commit()

#-----------------------------------------------------------------------
# How many entries are in the database
#
#-----------------------------------------------------------------------
def how_many(db):
   
   cursor = db.cursor()
   
   cursor.execute("SELECT COUNT(*) FROM CORPUS")
   a = cursor.fetchall()
   print(len(a))
   
