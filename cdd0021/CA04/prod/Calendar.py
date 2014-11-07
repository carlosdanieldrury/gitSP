'''
Created on Nov 5, 2014

@author: drury
'''
from __builtin__ import int
#27 LOC
class Calendar(object):
    '''
    Class Calendar
    '''
    
    def __init__(self):
        self.dayEffortList = {}
    
    def add(self, day, effort):
        if ((day <= 0) or (not isinstance(day, int))):
            raise ValueError("Calendar.add:  The value of day needs to be an integer grand than 0")
        if ((effort<0) or (not isinstance(effort, int))):
            raise ValueError("Calendar.add:  The value of effort needs to be equal or gran than 0")
        self.dayEffortList.update({day:effort})
        sumEffort = 0
        for dayEffort in self.dayEffortList.values():
            sumEffort += dayEffort
            
        return sumEffort
    
    def getLength(self):
        return max(self.dayEffortList.keys())
    
    def get(self, day):
        if not isinstance(day, int):
            raise ValueError("Calendar.get:  It is not a valid value for day")
        if self.dayEffortList.get(day)==None:
            return 0
        return self.dayEffortList.get(day)
    
    def getTotalEffort(self):
        sumEffort = 0
        for dayEffort in self.dayEffortList.values():
            sumEffort += dayEffort
        return sumEffort