import os
import json
import codecs

class Container():
    """
    Class container.
    """
    def __init__(self):
        self.__path = '../test'
        self.__isModified = False
        self.__dict = {"Not Classified":{"Not Classified":{"Not Classified":[("Sentence","Reference"),("Oi tuto pbom", "Monique")]}}}

    def listCategoriesFromDB(self):
        """
        Do the deep update from db for categories Section, Sub Section and Function.
        We use this just with a insertion, remove or update in any category.
        """
        
    def listSentencesFromDB(self, sections=[],  sub_sections=[],  functions=[]):
        """
        Do the deep update from db for Sentences. [((Section, SubSection, Function),Sentence), ((),)]
        We use this just with a insertion, remove or update in sentence.
        """
        
    def sections(self):
        """
        Return sections.
        """
        sections = self.__dict.keys()
        print 'sections: ',  sections
        return sections
            
        
    def subSections(self,  sections=[]):
        """
        Return sub sections from sections.
        """
        sub_sections = []
        for section in sections:
            sub_sections.extend(self.__dict[section].keys())
        #print 'sub sections: ',  sub_sections
        return sub_sections
        
    def functions(self, sections=[],  sub_sections=[]):
        """
        Return functions from sub sections.
        """
        functions = []
        for section in sections:
            for sub_section in sub_sections:
                functions.extend(self.__dict[section][sub_section].keys())
        #print 'functions: ',  functions
        return functions
        
    def sentences(self,  sections=[],  sub_sections=[],  functions=[]):
        """
        Return sentences from sections, sub_sections and functions.
        """
        sentences = []
        for section in sections:
            for sub_section in sub_sections:
                for function in functions:
                    sentences.extend(self.__dict[section][sub_section][function])
        #print 'sentences: ',  sentences
        return sentences
    
    @property
    def path(self):
        """
        Filepath to read and write.
        """
        return self.__path
        
    @path.setter
    def path(self, path):
        self.__path = os.path.abspath(path)
        
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
        if path == '':
            path = self.path
        else:
            self.path = path
        self.export_(path)
        self.isModified = False
        
    def read_(self,  path):
        """
        Reads file.
        """
        self.import_(path)
        self.path = path
        self.isModified = False
        
    def clear_(self):
        """
        Clear all fields.
        """
        self.__path = ''
        self.__isModified = False
        self.__dict = {'Not Classified':{'Not Classified':{'Not Classified':('Sentence','Reference')}}}
        
    def import_(self,  path=''):
        """
        Import file as XML, JSON, DB.
        """
        print path
        with codecs.open(path, 'rb', 'utf-8') as fp:
            text = fp.read()
            self.__dict = json.loads(str(text))
        self.isModified = False
        
    def export_(self,  path=''):
        """
        Export file as XML, JSON, DB.
        """
        print path
        with codecs.open(path, 'wb',  'utf-8') as project_file:
            json.dump(self.__dict, project_file,  indent=4,  sort_keys=True)
        self.isModified = False

