'''
Created on Sep 10, 2014

@author: drury
'''
import unittest
import CA02.prod.Component as component

class ComponentTest(unittest.TestCase):

    '''
    Class created to test the Component class
    '''

    def setUp(self):
        #Instantiate a component
        self.C1 = component.Component("C1",4,20)
        #return C1
    
    def testGetNameC1(self):
        #test the method getName
        return self.C1.getName()
    
    def testGetNumMetC1(self):
        #test the method getMethodCount
        return self.C1.getMethodCount()
    
    def testGetLocCount(self):
        #test the method getLocCount
        return self.C1.getLocCount()
    
        
    def testExceptionNameMissing(self):
        #test the exception when the name of component is missing
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
        #test the exception when the name of component is a number
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
        #test the exception when the methodCount of component is a negative number
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
        #test the exception when the methodCount of component is missing
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
        #test the exception when the methodCount of component is a string
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
        #test the exception when the locCount of component is missing
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
        #test the exception when the locCount of component is 0
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
        #test the exception when the locCount of component is a caracter
        expectedString = "Component.__init__: Invalid Value for locCount value, integer"
        try:
            testComponent = component.Component("C1",4,"X")
            self.fail("exception was not raised")
            
        except ValueError as raisedException:
            diagnosticString = raisedException.args[0]
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
            
    
    def test_02_11_001_setRelativeSizeVS(self):
        self.C1.setRelativeSize("VS")
        
    def test_02_11_002_setRelativeSizeVS(self):
        self.C1.setRelativeSize("S")   
        
    def test_02_11_003_setRelativeSizeVS(self):
        self.C1.setRelativeSize("M")
        
    def test_02_11_004_setRelativeSizeVS(self):
        self.C1.setRelativeSize("L")
     
    def test_02_11_005_setRelativeSizeVS(self):
        self.C1.setRelativeSize("VL")        
         
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()