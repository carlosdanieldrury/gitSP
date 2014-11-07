'''
Created on Nov 6, 2014

@author: drury
'''
import Project as Project
import Calendar as Calendar
from __builtin__ import int
#50 LOC
class Schedule(object):
    '''
    Schedule Class - Parameters: project and calendar
    '''


    def __init__(self, project=None, calendar=None):
        '''
        Constructor
        '''
        if ((project==None) or (calendar==None)):
            raise ValueError("Schedule.__init__:  It is missing parameter(s)")
        if (not isinstance(project, Project.Project)):
            raise ValueError("Schedule.__init__:  Invalid instance for Project")
        if (not isinstance(calendar, Calendar.Calendar)):
            raise ValueError("Schedule.__init__:  Invalid instance for Calendar")
        if ((project.getEffort()==0) or (calendar.getTotalEffort==0)):
            raise ValueError("Schedule.__init__:  The calendar/project needs to have sufficient days/effort to create an instance")
        sumEffort = project.getEffort()
        sumEffortDaysCalendar = calendar.getTotalEffort()

        if (sumEffort > sumEffortDaysCalendar):
            raise ValueError("Schedule.__init__:  The calendar needs to have sufficient days to execute the project")
        
        self.project = project
        self.calendar = calendar
        
    def getLastDay(self):
        sumEffort = self.project.getEffort()
        numDays = 0
        while (sumEffort>0):
            sumEffort -= self.calendar.get(numDays+1)
            numDays += 1
        return numDays
    
        
    def getBurnDown(self, day):
        if not isinstance(day, int):
            raise ValueError("Schedule.getBurnDown:  The value of day needs to be integer")
        if ((day<1) or (day>self.calendar.getLength())):
            raise ValueError("Schedule.getBurnDown:  The value of day is out of the limit")
        numDays = 0
        sumEffort = self.project.getEffort()
        while (numDays<day):
            sumEffort -= self.calendar.get(numDays+1)
            numDays += 1
        return sumEffort
    
    def getPV(self,day):
        if not isinstance(day, int):
            raise ValueError("Schedule.getPV:  The value of day needs to be integer")
        numDays = 0
        remainingDays = self.getLastDay()
        sumEffort = self.project.getEffort()
        while (numDays<day):
            sumEffort -= self.calendar.get(numDays+1)
            numDays += 1
            remainingDays -= 1
            if ((numDays==day) and (sumEffort > self.calendar.get(day))):
                remainingDays +=1
        return remainingDays
        