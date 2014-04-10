
import os


class Container():
    """
    Class container.
    """
    self.__path = ''
    self.__isModified = False
    
    @property
    def path(self):
        return self.__path
        
    @path.setter
    def path(self, path):
        self.__path = os.path.abspath(path)
        
    @property
    def isModified(self):
        return self.__isModified
        
    @isModified.setter
    def isModified(self, state):
        self.__isModified = state
        
    def _write(path=''):
        """
        writes file.
        """
    def _read(path):
        """
        Reads file.
        """
        
    def _import(path=''):
        """
        Import file as XML, JSON, DB.
        """
        
    def _export(path=''):
        """
        Export file as XML, JSON, DB.
        """
