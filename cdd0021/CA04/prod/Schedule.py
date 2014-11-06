'''
Created on Nov 6, 2014

@author: drury
'''
import Iteration as Iteration
import Project as Project
import Calendar as Calendar

class Schedule(object):
    '''
    Schedule Class - Parameters: project and calendar
    '''


    def __init__(self, project, calendar):
        '''
        Constructor
        '''
        self.project = project
        self.calendar = calendar
        
    def getLastDay(self):
        sumEffort = 0
        numDays = 0
        for iteration in self.project.getIterationList():
            sumEffort += iteration.getEffort()
        while (sumEffort>0):
            sumEffort -= self.calendar.get(numDays+1)
            numDays += 1
        return numDays
    
        