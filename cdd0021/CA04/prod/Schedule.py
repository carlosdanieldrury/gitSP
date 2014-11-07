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
        if ((project.getEffort()==0) or (calendar.getTotalEffort==0)):
            raise ValueError("Schedule.__init__:  The calendar/project needs to have sufficient days/effort to create an instance")
        sumEffort = project.getEffort()
        sumEffortDaysCalendar = calendar.getTotalEffort()

        if (sumEffort > sumEffortDaysCalendar):
            raise ValueError("Schedule.__init__:  The calendar needs to have sufficient days to execute the project")
        
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
    
        
    def getBurnDown(self, day):
        if ((day<1) or (day>self.calendar.getLength())):
            raise ValueError("Schedule.getBurnDown:  The value of day is out of the limit")
        sumEffort = 0
        numDays = 0
        for iteration in self.project.getIterationList():
            sumEffort += iteration.getEffort()
        while (numDays<day):
            sumEffort -= self.calendar.get(numDays+1)
            numDays += 1
        return sumEffort
    
    def getPV(self,day):
        sumEffort = 0
        numDays = 0
        remainingDays = self.getLastDay()
        for iteration in self.project.getIterationList():
            sumEffort += iteration.getEffort()
        while (numDays<day):
            sumEffort -= self.calendar.get(numDays+1)
            numDays += 1
            remainingDays -= 1
            if ((numDays==day) and (sumEffort > self.calendar.get(day))):
                remainingDays +=1
        return remainingDays
        