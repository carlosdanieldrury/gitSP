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
        if (fileName==""):
            raise ValueError("PythonScript.__init__:   The name cannot be empty")
        if (isinstance(fileName, basestring)):
            if (os.path.exists(fileName)):
                auxName = fileName.strip(".")
                if (auxName.find(".py")>-1):
                    self.fileName = fileName
                    self.filePath = None
                else:
                    raise ValueError("PythonScript.__init__:   It is not a python file")
            else:
                raise ValueError("PythonScript.__init__:   The file does not exist")
        else:
            raise ValueError("PythonScript.__init__:   fileName needs to be a string")
        
    def getFileName(self):
        return self.fileName
    
    def getFilePath(self):
        self.filePath = os.path.abspath(self.fileName)
        return self.filePath
    
    def countLine(self):
        numLines = 0
        file = open(self.fileName, 'r')
        for line in file:
            auxLine = line.strip(" ")
            if ((auxLine[0] != "#") and (auxLine.find("'''")==-1)):
                numLines +=1
        return numLines
    
    def findClassName(self, line):
        cont = 6
        nameClass = ""
        while line[cont] != "(":
            tab = line.count(' ')
            nameClass = nameClass + line[cont]
            cont += 1
        
        return nameClass

    def findNameFunc(self, line):
        nameFunc = ""
        cont = 4
        while line[cont] != "(":
            nameFunc = nameFunc + line[cont]
            cont += 1
        
        return nameFunc

    def verificationNoCommentDocumentation(self, line):
        if line:
            auxLine = line.strip(" ")
            if ((auxLine[0] != "#") and (auxLine.find("'''") == -1)):
                return True
        return False


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
                locCount = 0
                methodCount = 0
                nameClass = self.findClassName(line)

                line = file.readline()
                if (self.verificationNoCommentDocumentation(line)):
                        locCount += 1
                
                while 1:
                    tab = line.count("\t")
                    line = line.strip()
                    if (line[0:3]==func):
                        methodCount += 1
                    line = file.readline()
                    if (self.verificationNoCommentDocumentation(line)):
                        locCount += 1

                    if ((line[0:5]==comp)or ((line[0:3]==func) and (tab==0))):
                        break

                newComponent = Component.Component(nameClass, methodCount, locCount)
                listComp.append(newComponent)
            else:
                if (line[0:3]==func):
                    locCount = 0
                    methodCount = 1
                    nameFunc = self.findNameFunc(line)

                    line = file.readline()
                    if (self.verificationNoCommentDocumentation(line)):
                        locCount += 1
                    
                    while 1:
                        tab = line.count("\t")
                        line = line.strip()
                        if (line[0:3]==func):
                            methodCount += 1
                        line = file.readline()    
                        locCount += 1

                        if ((line[0:5]==comp) or ((line[0:3]==func) and (tab==0))):
                            break

                        if not line:
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
            
        
            
                
                