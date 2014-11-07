'''
Created on Nov 6, 2014

@author: drury
'''
import unittest
import CA04.prod.Schedule as Schedule
import CA04.prod.Project as Project
import CA04.prod.Calendar as Calendar
import CA04.prod.Iteration as Iteration

class Test(unittest.TestCase):


    def test100_010_ShouldConstructSchedule(self):
        myCalendar = Calendar.Calendar()
        myProject = Project.Project()
        iteration1 = Iteration.Iteration(30, 1)
        myProject = Project.Project()
        myProject.add(iteration1)
        myCalendar = Calendar.Calendar()
        myCalendar.add(1, 10)
        myCalendar.add(2, 0)
        myCalendar.add(3, 30)
        self.assertIsInstance(Schedule.Schedule(project=myProject, calendar=myCalendar), Schedule.Schedule)
        
    def test100_020_ShouldConstructScheduleOtherValues(self):
        iteration1 = Iteration.Iteration(30, 1)
        iteration2 = Iteration.Iteration(60, 3)
        myProject = Project.Project()
        myProject.add(iteration1)
        myProject.add(iteration2)
        myCal = Calendar.Calendar()
        myCal.add(1, 10)
        myCal.add(2, 0)
        myCal.add(3, 30)
        myCal.add(4, 30)
        myCal.add(5, 60)
        myCal.add(6, 90)
        self.assertIsInstance(Schedule.Schedule(project=myProject, calendar=myCal), Schedule.Schedule)
        
    def test100_030_ShouldReturnDaysOfFinishJob(self):
        iteration1 = Iteration.Iteration(30, 1)
        iteration2 = Iteration.Iteration(60, 3)
        myProject = Project.Project()
        myProject.add(iteration1)
        myProject.add(iteration2)
        myCal = Calendar.Calendar()
        myCal.add(1, 10)
        myCal.add(2, 0)
        myCal.add(3, 30)
        myCal.add(4, 30)
        myCal.add(5, 60)
        myCal.add(6, 90)
        mySched = Schedule.Schedule(myProject,myCal)
        self.assertEquals(mySched.getLastDay(), 5)
        
    def test100_040_ShouldReturnBurnDown(self):
        iteration1 = Iteration.Iteration(30, 1)
        iteration2 = Iteration.Iteration(60, 3)
        myProject = Project.Project()
        myProject.add(iteration1)
        myProject.add(iteration2)
        myCal = Calendar.Calendar()
        myCal.add(1, 10)
        myCal.add(2, 0)
        myCal.add(3, 30)
        myCal.add(4, 30)
        myCal.add(5, 60)
        myCal.add(6, 90)
        mySched = Schedule.Schedule(myProject,myCal)
        self.assertEquals(mySched.getBurnDown(day=3), 50)
        
    def test100_050_ShouldReturnRemainingDays(self):
        iteration1 = Iteration.Iteration(30, 1)
        iteration2 = Iteration.Iteration(60, 3)
        myProject = Project.Project()
        myProject.add(iteration1)
        myProject.add(iteration2)
        myCal = Calendar.Calendar()
        myCal.add(1, 10)
        myCal.add(2, 0)
        myCal.add(3, 30)
        myCal.add(4, 30)
        myCal.add(5, 60)
        myCal.add(6, 90)
        mySched = Schedule.Schedule(myProject,myCal)
        self.assertEquals(mySched.getPV(day=3), 3)
        
#sad
    def test200_010_ShouldRaiseExceptionNoSufficientDays(self):
        iteration1 = Iteration.Iteration(30, 1)
        iteration2 = Iteration.Iteration(60, 3)
        myProject = Project.Project()
        myProject.add(iteration1)
        myProject.add(iteration2)
        myCal = Calendar.Calendar()
        myCal.add(1, 10)
        expectedString = "Schedule.__init__:"
        try:
            mySched = Schedule.Schedule(myProject,myCal)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test100_010_ShouldConstructSchedule']
    unittest.main()