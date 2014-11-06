'''
Created on Nov 5, 2014

@author: drury
'''

class Project(object):
    '''
    Project Class
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.iterationList = []
        
    def add(self, iteration):
        self.iterationList.append(iteration)
        return self.iterationList.index(iteration) + 1
    
    def getIterationCount(self):
        return len(self.iterationList)
    
    def getIteration(self, iterationNumber):
        return self.iterationList[iterationNumber-1].__str__()
    
    def getEffort(self):
        sumEffort = 0
        for iteration in self.iterationList:
            sumEffort += iteration.getEffort()
            
        return sumEffort
    
    def getPV(self):
        sumPV = 0
        for iteration in self.iterationList:
            sumPV += iteration.getPV()
            
        return sumPV
        