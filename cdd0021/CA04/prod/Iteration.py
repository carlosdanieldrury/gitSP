'''
Created on Nov 4, 2014

@author: drury
'''

class Iteration(object):
    '''
    Iteration Class - Parameters effort and plannedVelocity
    '''


    def __init__(self, effort, plannedVelocity):
        '''
        Constructor
        '''
        if effort <= 0:
            raise ValueError("Iteration.__init__:  The effort value needs to be grand than 0")
        
        self.effort = effort
        self.plannedVelocity = plannedVelocity
    
    def getEffort(self):
        return self.effort
    
    def getPV(self):
        return self.plannedVelocity