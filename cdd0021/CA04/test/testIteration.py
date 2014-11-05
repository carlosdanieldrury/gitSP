'''
Created on Nov 4, 2014

@author: drury
'''
import unittest
import CA04.prod.Iteration as Iteration


class Test(unittest.TestCase):


#Constructor
#happy
    def test100_010_ShouldConstructIteration(self):
        #myIteration = Iteration.Iteration(effort=120, plannedVelocity=3)
        self.assertIsInstance(Iteration.Iteration(effort=120, plannedVelocity=3), Iteration.Iteration)

    def test100_020_ShouldGetEffort(self):
        myIteration = Iteration.Iteration(effort=120, plannedVelocity=3)
        self.assertEquals(myIteration.getEffort(), 120)

    def test100_030_ShouldGetPV(self):
        myIteration = Iteration.Iteration(effort=120, plannedVelocity=3)
        self.assertEquals(myIteration.getPV(), 3)
        
#sad 
    def test200_010_ShouldRaiseExceptionInvalidEffort(self):
        expectedString = "Iteration.__init__:  "
        try:
            myIteration = Iteration.Iteration(0,3)                                          
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")   
            
    def test200_011_ShouldRaiseExceptionInvalidEffortNegative(self):
        expectedString = "Iteration.__init__:  "
        try:
            myIteration = Iteration.Iteration(-1,3)                                          
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")   
            
    def test200_012_ShouldRaiseExceptionInvalidEffortString(self):
        expectedString = "Iteration.__init__:  "
        try:
            myIteration = Iteration.Iteration("X",3)                                          
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")       
            
    def test200_020_ShouldRaiseExceptionInvalidPV(self):
        expectedString = "Iteration.__init__:  "
        try:
            myIteration = Iteration.Iteration(120, 0)                                          
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
    def test200_021_ShouldRaiseExceptionInvalidPVNegative(self):
        expectedString = "Iteration.__init__:  "
        try:
            myIteration = Iteration.Iteration(120, -1)                                          
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
            
    def test200_022_ShouldRaiseExceptionInvalidPVString(self):
        expectedString = "Iteration.__init__:  "
        try:
            myIteration = Iteration.Iteration(120, "X")                                          
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
    def test200_030_ShouldRaiseExceptionNoParameters(self):
        expectedString = "Iteration.__init__:  "
        try:
            myIteration = Iteration.Iteration()                                          
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
    
        
         

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()