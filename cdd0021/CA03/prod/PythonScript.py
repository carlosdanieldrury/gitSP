'''
Created on Oct 21, 2014

@author: drury
'''

import os
from CA03.prod import Component as Component

class PythonScript(object):
    '''
    PythonScript Class that read a python file and can count how many components there are inside the file and how many
    functions as well.
    '''


    def __init__(self, fileName=None):
        '''
        Constructor
        '''
        if (fileName==None):
            raise ValueError("PythonScript.__init__:   Missing the file name")
        self.fileName = fileName
        self.filePath = None
        
    def getFileName(self):
        return self.fileName
    
    def getFilePath(self):
        self.filePath = os.path.abspath(self.fileName)
        return self.filePath
    
    def countLine(self):
        numLines = 0
        file = open(self.fileName, 'r')
        for line in file:
            numLines +=1
        return numLines
    
    def extractDesign(self):
        file = open(self.fileName, 'r')
        comp = "class"
        func = "def"
        tab = 0
        listComp = []
        listFunc = []
        numSpaces = 0
 
        
        line = file.readline()
             
            
        while 1:
            
            tab = line.count("\t")

            if (line[0:5]==comp):

                cont = 6
                nameClass = ""
                methodCount = 0
                locCount = 0
                while line[cont] != "(":
                    tab = line.count(' ')
                    nameClass = nameClass + line[cont]
                    cont += 1

                line = file.readline()
                #line = line.replace(" ","")
                locCount += 1
                
                while 1:
                    tab = line.count("\t")
                    line = line.strip()
                    if (line[0:3]==func):
                    #if line.find(func)>-1:
                        methodCount += 1
                    line = file.readline()    
                    locCount += 1

                    
                    if ((line[0:5]==comp)or ((line[0:3]==func) and (tab==0))):
                        break

                newComponent = Component.Component(nameClass, methodCount, locCount)
                listComp.append(newComponent)
            else:
                if (line[0:3]==func):
                    nameFunc = ""
                    locCount = 0
                    methodCount = 1
                    cont = 4
                    while line[cont] != "(":
                        nameFunc = nameFunc + line[cont]
                        cont += 1

                    line = file.readline()
                    locCount += 1
                    
                    while 1:
                        tab = line.count("\t")
                        line = line.strip()
                        if (line[0:3]==func):
                        #if line.find(func)>-1:
                            methodCount += 1
                        line = file.readline()    
                        locCount += 1

                        if not line:
                            break
                        if ((line[0:5]==comp) or ((line[0:3]==func) and (tab==0))):
                            break
                    
                    newFunc = Component.Component(nameFunc, methodCount, locCount)
                    listFunc.append(newFunc)
                    if (line[0:5] == comp):
                            break

                else :
                    line = file.readline()
            if not line:
                list = [listComp,listFunc]
                return list
            
        
            
                
                