'''
Created on Sep 10, 2014

@author: drury
'''
import unittest
#from prod import Component
import CA01.prod.Component as component

class ComponentTest(unittest.TestCase):

    '''
    Class created to test the Component class
    '''

    def setUp(self):
        self.C1 = component.Component("C1",4,20)
        #return C1
    
    def testGetNameC1(self):
        return self.C1.getName()
    
    def testGetNumMetC1(self):
        return self.C1.getMethodCount()
    
    def testGetLocCount(self):
        return self.C1.getLocCount()
    
        
    def testExceptionNameMissing(self):
        expectedString = "Component.__init__: The Component needs a name"        
        
        try:
            testComponent = component.Component(methodCount=4,locCount=20)
            self.fail("exception was not raised")
            
        except ValueError as raisedException:
            diagnosticString = raisedException.args[0]
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
    def testExceptionNameError(self):
        expectedString = "Component.__init__:"        
        
        try:
            testComponent = component.Component(2,4,20)
            self.fail("exception was not raised")
            
        except ValueError as raisedException:
            diagnosticString = raisedException.args[0]
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")

        
    def testExceptionMetNumber(self):
        expectedString = "Component.__init__: methodCount needs to be grand than or equal to 0"
        try:
            testComponent = component.Component("C1",-1,20)
            self.fail("exception was not raised")
            
        except ValueError as raisedException:
            diagnosticString = raisedException.args[0]
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
    
    def testExceptionMetMissing(self):
        expectedString = "Component.__init__: MethodCount Missing"
        try:
            testComponent = component.Component("C1",locCount=20)
            self.fail("exception was not raised")
            
        except ValueError as raisedException:
            diagnosticString = raisedException.args[0]
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)])
        except Exception as e:
            print e
            self.fail("incorrect exception was raised")      
            
    
            
    def testExceptionMetCaracter(self):
        expectedString = "Component.__init__: Invalid value for methodCount, it needs to be a number grand than or equal to 0"
        try:
            testComponent = component.Component("C1","X",20)
            self.fail("exception was not raised")
            
        except ValueError as raisedException:
            diagnosticString = raisedException.args[0]
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
            
    def testExceptionLOCMissing(self):
        expectedString = "Component.__init__: Missing locCount value"
        try:
            testComponent = component.Component("C1",methodCount=4)
            self.fail("exception was not raised")
            
        except ValueError as raisedException:
            diagnosticString = raisedException.args[0]
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
    
    def testExceptionLOCNumber(self):
        expectedString = "Component.__init__:Invalid Value for the locCount, integer grand than 0"
        try:
            testComponent = component.Component("C1",4,0)
            self.fail("exception was not raised")
            
        except ValueError as raisedException:
            diagnosticString = raisedException.args[0]
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")


    

    def testExceptionLOCCaracter(self):
        expectedString = "Component.__init__: Invalid Value for locCount value, integer"
        try:
            testComponent = component.Component("C1",4,"X")
            self.fail("exception was not raised")
            
        except ValueError as raisedException:
            diagnosticString = raisedException.args[0]
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
         
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()