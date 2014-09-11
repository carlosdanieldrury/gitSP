'''
Created on Sep 10, 2014

@author: drury
'''

class Component(object):
    '''
    Class Component describe the properties of pieces of software.
    The informations that a component can have are: name, how many methods this component has and
    how many lines of code this component has.
    '''


    def __init__(self, name=None, methodCount=None, locCount=None):
        '''
        Constructor
        '''
        if name==None:
            raise ValueError("Component.__init__: The Component needs a name")
        else:
            if isinstance(name, basestring):
                self.name = name
            else:
                raise ValueError("Component.__init__: Invalid name for the Component")
        if (methodCount == None):
            raise ValueError("Component.__init__: MethodCount Missing")
        else:
            if isinstance(methodCount, int):
                if (methodCount >= 0):
                    self.methodCount = methodCount
                else:
                    raise ValueError("Component.__init__: methodCount needs to be grand than or equal to 0")
            else:
                raise ValueError("Component.__init__: Invalid value for methodCount, it needs to be a number grand than or equal to 0")
        if (locCount == None):
            raise ValueError("Component.__init__: Missing locCount value")
        else:
            if isinstance(locCount, int):
                if locCount > 0:
                    self.locCount = locCount
                else:
                    raise ValueError("Component.__init__:Invalid Value for the locCount, integer grand than 0")
            else:
                raise ValueError("Component.__init__: Invalid Value for locCount value, integer")
        
    def getName(self):
        return self.name
    
    #Returns the method count
    def getMethodCount(self):
        return self.methodCount
        
    #Returns the number of line of code    
    def getLocCount(self):
        return self.locCount