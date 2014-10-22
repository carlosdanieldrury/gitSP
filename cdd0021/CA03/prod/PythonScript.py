'''
Created on Oct 21, 2014

@author: drury
'''

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
        
    def getFileName(self):
        return self.fileName