'''
Created on Nov 5, 2014

@author: drury
'''
import unittest
import CA04.prod.Calendar as Calendar


class Test(unittest.TestCase):

#happy
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

    def test100_040_ShouldGetLength(self):
        myCal = Calendar.Calendar()
        myCal.add(2, 60)
        myCal.add(5, 120)
        self.assertEquals(myCal.getLength(), 5)
        
    def test100_050_SouldRetrieveDay(self):
        myCal = Calendar.Calendar()
        myCal.add(2, 60)
        myCal.add(5, 120)
        self.assertEquals(myCal.get(day=2), 60)
        
    def test100_060_SouldRetrieveDayNoEffort(self):
        myCal = Calendar.Calendar()
        myCal.add(2, 60)
        myCal.add(5, 120)
        self.assertEquals(myCal.get(day=4), 0)
        
        
#sad
    def test200_010_ShouldRaiseExceptionInvalidDay(self):
        myCal = Calendar.Calendar()
        expectedString = "Calendar.add:  "
        try:
            myCal.add(0,30)                                              
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test200_020_ShouldRaiseExceptionInvalidEffort(self):
        myCal = Calendar.Calendar()
        expectedString = "Calendar.add:  "
        try:
            myCal.add(1,-30)                                              
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test200_030_ShouldRaiseExceptionGetDayString(self):
        myCal = Calendar.Calendar()
        expectedString = "Calendar.get:  "
        try:
            myCal.get("X")                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
        
    def test200_040_ShouldRaiseExceptionInvalidDay(self):
        myCal = Calendar.Calendar()
        expectedString = "Calendar.add:  "
        try:
            myCal.add("X",30)                                              
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")             
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()