'''
Created on Nov 5, 2014

@author: drury
'''

class Calendar(object):
    '''
    Class Calendar
    '''
    
    def __init__(self):
        self.dayEffortList = {}
    
    def add(self, day, effort):
        self.dayEffortList.update({day:effort})
        sumEffort = 0
        for dayEffort in self.dayEffortList.values():
            sumEffort += dayEffort
            
        return sumEffort
    
    def getLength(self):
        return max(self.dayEffortList.keys())
    
    def get(self, day):
        #if (day>0) and (day<=self.getLength()):
            if self.dayEffortList.get(day)==None:
                return 0
            return self.dayEffortList.get(day)