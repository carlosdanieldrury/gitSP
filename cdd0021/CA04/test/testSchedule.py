'''
Created on Nov 6, 2014

@author: drury
'''
import unittest
import CA04.prod.Schedule as Schedule
import CA04.prod.Project as Project
import CA04.prod.Calendar as Calendar

class Test(unittest.TestCase):


    def test100_010_ShouldConstructSchedule(self):
        myCalendar = Calendar.Calendar()
        myProject = Project.Project()
        self.assertIsInstance(Schedule.Schedule(project=myProject, calendar=myCalendar), Schedule.Schedule)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test100_010_ShouldConstructSchedule']
    unittest.main()