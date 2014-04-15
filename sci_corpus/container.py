import os

class Container():
    """
    Class container.
    """
    def __init__(self):
        self.__path = ''
        self.__isModified = False
        #{Section1: [SubSection1, SubSection2], }
        self.__sections = {}
        self.__subSections = {}
        self.__functions = {}
    
    def listCategories(self):
        """
        Do the deep update from db for categories Section, Sub Section and Function.
        """
        
    def listSentences(self, (Section, SubSection, Function)):
        """
        Do the deep update from db for Sentences. [((Section, SubSection, Function),Sentence), ((),)]
        """
    
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
        writes file in path or in self.path if not passed.
        """
        
    def read_(self,  path):
        """
        Reads file.
        """
        
    def close(self):
        """
        
        """
        
    def import_(self,  path=''):
        """
        Import file as XML, JSON, DB.
        """
        
    def export_(self,  path=''):
        """
        Export file as XML, JSON, DB.
        """
