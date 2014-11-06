'''
Created on Nov 4, 2014

@author: drury
'''
from optparse import isbasestring
from Crypto.Protocol.AllOrNothing import isInt

class Iteration(object):
    '''
    Iteration Class - Parameters effort and plannedVelocity
    '''


    def __init__(self, effort=None, plannedVelocity=None):
        '''
        Constructor
        '''
        if (effort==None) or (plannedVelocity==None):
            raise ValueError("Iteration.__init__:  The parameters are incorrect")
        
        if not isInt(effort):
            raise ValueError("Iteration.__init__:  The effort value needs to be an integer")
        if effort <= 0:
            raise ValueError("Iteration.__init__:  The effort value needs to be grand than 0")
        if not isInt(plannedVelocity):
            raise ValueError("Iteration.__init__:  The plannedVelocity value needs to be an integer")
        if plannedVelocity <= 0:
            raise ValueError("Iteration.__init__:  The plannedVelocity value needs to be grand than 0")
        
        self.effort = effort
        self.plannedVelocity = plannedVelocity
    
    def getEffort(self):
        return self.effort
    
    def getPV(self):
        return self.plannedVelocity
    
    def __str__(self, *args, **kwargs):
        return "<Iteration(%s,%s)>" % (self.effort, self.plannedVelocity)