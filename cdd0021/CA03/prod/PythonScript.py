'''
Created on Oct 21, 2014

@author: drury
'''

import os

class PythonScript(object):
    '''
    PythonScript Class that read a python file and can count how many components there are inside the file and how many
    functions as well.
    '''


    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.fileName = fileName
        self.filePath = None
        
    def getFileName(self):
        return self.fileName
    
    def getFilePath(self):
        self.filePath = os.path.abspath(self.fileName)
        return self.filePath