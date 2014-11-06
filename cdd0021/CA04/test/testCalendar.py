'''
Created on Nov 5, 2014

@author: drury
'''
import unittest
import CA04.prod.Calendar as Calendar


class Test(unittest.TestCase):


    def test100_010_ShouldConstructCalendar(self):
        self.assertIsInstance(Calendar.Calendar(), Calendar.Calendar)

    def test100_020_ShouldAddDayEffort(self):
        myCalendar = Calendar.Calendar()
        day = 1
        effort = 60
        self.assertEquals(myCalendar.add(day,effort), 60)
        
    
    def test100_030_ShouldAddAnotherDayEffort(self):
        myCalendar = Calendar.Calendar()
        myCalendar.add(1,60)
        day = 5
        effort = 120
        self.assertEquals(myCalendar.add(day,effort), 180)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()