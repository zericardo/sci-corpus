import os

class Container():
    """
    Class container.
    """
    def __init__(self):
        self.__path = ''
        self.__isModified = False
        self.__sections = [(1, 'Abstract'), (2, 'Introduction'), (3, 'Methodology'), (4, 'Results'), (5, 'Conclusion')]
        self.__relSectionSubSection = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3)]
        self.__subSections = [(1, 'Contextualization'), (2, 'Gap'), (3, 'Propose'), (4, 'Methodology'), (5, 'Results'), (6, 'Conclusion')]
        self.__relSubSectionFunction = [(0,0)]
        self.__functions = [(1,'Fuuuuck')]

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
        sections = []
        for  id, section in self.__sections:
            sections.append(section)
        print sections
        return sections
            
        
    def subSections(self,  sections=[]):
        """
        Return sub sections from sections.
        """
        sub_sections = []
        sections_id = []
        subsections_id = []
        
        # get section ids
        for id, section in self.__sections:
            if section in sections:
                sections_id.append(id)
                
        # get subsection ids
        for id, subsection in self.__subSections:
                subsections_id.append(id)
                
        #use relations to creat a list of all subsections
        for sec_id, subsec_id in self.__relSectionSubSection:
            if sec_id in sections_id:
                index = subsections_id.index(subsec_id)
                sub_sections.append(self.__subSections[index][1])
                
        sub_sections = set(sub_sections)
        print sub_sections
        return sub_sections
        
    def function(self,  sub_sections=[]):
        """
        Return functions from sub sections.
        """
        
    def sentences(self,  sections=[],  sub_sections=[],  functions=[]):
        """
        Return sentences from sections, sub_sections and functions.
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

        self.isModified = False
        
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
