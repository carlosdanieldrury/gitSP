'''
Created on Sep 11, 2014

@author: drury
'''
import unittest
from CA02.prod import Repository as repository
from CA02.prod import Component as component

class RepositoryTest(unittest.TestCase):

    '''
    Class created to test the Repository class
    '''

    def setUp(self):
        self.testRepository = repository.Repository(2)
        
    def testInstantiateRep200(self):
        # test the creation of a repository with capacity=200
        testRepository = repository.Repository(200)    
    
    def testGetNumberComponents(self):
        #print self.testRepository.count() 
        #print self.testRepository.getCapacity()
        return self.testRepository.count()
    
    def testRepositoryNoParam(self):
        # test the creation of a repository without parameter
        self.testRepository = repository.Repository()
        #print self.testRepository.count()
        #print self.testRepository.getCapacity()
        
    def testRepositoryCap2(self):
        # test the creation of a repository with capacity=2
        self.testRepository = repository.Repository(2)
        #print self.testRepository.count()
        #print self.testRepository.getCapacity()
        
    def testAddComponent(self):
        # test the addition of a component
        self.testRepository = repository.Repository(2)
        C1 = component.Component("C1",4,20)
        self.testRepository.addComponent(C1)
        # print self.testRepository.count()
        # print self.testRepository.getCapacity()
        
    
        
    def testExceptionCapacity0(self):
        #Exception if the capacity is 0
        expectedString = "Repository.__init__: The capacity needs to be grand than 0"        
        try:
            testRepository = repository.Repository(0)
            self.fail("exception was not raised")
        except ValueError as raisedException:
            diagnosticString = raisedException.args[0]
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")    
    
    def testCompleteRepository2(self):
        C2 = component.Component("C2",4,40)
        C3 = component.Component("C3",1,20)
        self.testRepository.addComponent(C2)
        self.testRepository.addComponent(C3)
        #CC1= self.testRepository.repository.pop()
        #CC2= self.testRepository.repository.pop()
        #print CC2.getName()
        #print CC1.getName()
        #print self.testRepository.count()
        #print self.testRepository.getCapacity()
        
    def testValidCountRepository(self):
        #test valid count of components in the repository
        C2 = component.Component("C2",4,40)
        C3 = component.Component("C3",1,20)
        self.testRepository.addComponent(C2)
        self.testRepository.addComponent(C3)
        #print self.testRepository.validCount()
        return self.testRepository.validCount()
    
    def testExceptionAddComponentNoParam(self):
        #Exception if the parameter is missing
        expectedString = "Repository.addComponent: The method addComponent needs a parameter"        
        try:
            self.testRepository.addComponent()
            self.fail("exception was not raised")
        except ValueError as raisedException:
            diagnosticString = raisedException.args[0]
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
    
    
    
        
    def testRelativeSizes(self):
        #test the relative sizes of the components in the repository
        self.testRepository = repository.Repository(5)
        component1 = component.Component(name="Component01",methodCount=1,locCount=76)
        component2 = component.Component("Component02",locCount=116,methodCount=4)
        component3 = component.Component("Component03",7,locCount=113)
        component4 = component.Component("Component04",5,103)
        component5 = component.Component("Component5",0,10)
        self.testRepository.addComponent(component1)
        self.testRepository.addComponent(component2)
        self.testRepository.addComponent(component3)
        self.testRepository.addComponent(component4)
        self.testRepository.addComponent(component5)
        
        relativeSizes = self.testRepository.determineRelativeSizes()
        #print relativeSizes

    def test_02_21_001_ComponentSameName(self):
        self.testRepository = repository.Repository(5)
        component1 = component.Component(name="Component01",methodCount=1,locCount=76)
        component2 = component.Component("Component02",locCount=116,methodCount=4)
        component01 = component.Component("Component01",7,locCount=113)
        self.testRepository.addComponent(component1)
        self.testRepository.addComponent(component2)
        self.assertRaises(ValueError, self.testRepository.addComponent, component01)
        
    def test_02_21_002_SameComponent(self):
        self.testRepository = repository.Repository(5)
        component1 = component.Component(name="Component01",methodCount=1,locCount=76)
        component2 = component.Component("Component02",locCount=116,methodCount=4)
        self.testRepository.addComponent(component1)
        self.testRepository.addComponent(component2)
        self.assertRaises(ValueError, self.testRepository.addComponent, component1)    
        
    def test_02_22_001_getRelativeSizeComponent(self):
        self.testRepository = repository.Repository(5)
        component1 = component.Component(name="Component01",methodCount=1,locCount=76)
        component2 = component.Component("Component02",locCount=116,methodCount=4)
        component3 = component.Component(name="Component01",methodCount=1,locCount=76)
        self.testRepository.addComponent(component1)
        self.testRepository.addComponent(component2)
        self.testRepository.getRelativeSize(component3)
    
    def test_02_22_002_getRelativeSizeNoParam(self):
        self.assertRaises(ValueError, self.testRepository.getRelativeSize)
        
    def test_02_23_001_estimateByRelativeSize(self):
        self.testRepository = repository.Repository(5)
        component1 = component.Component("Component01",1,1)
        component2 = component.Component("Component02",2,4)
        component3 = component.Component("Component03",3,6)
        component4 = component.Component("Component04",4,8)
        component5 = component.Component("Component05",5,10)
        self.testRepository.addComponent(component1)
        self.testRepository.addComponent(component2)
        self.testRepository.addComponent(component3)
        self.testRepository.addComponent(component4)
        self.testRepository.addComponent(component5)
        ComponetNew = self.testRepository.estimateByRelativeSize("X",2,"L")
        #print "Name :".join(ComponetNew.getName())
        #print "Num Met :"
        #print ComponetNew.getMethodCount()
        #print "LOC :"
        #print ComponetNew.getLocCount()
    
    #sad
    def test_02_23_002_estimateByRelativeSizeExc1(self):
        self.testRepository = repository.Repository(5)
        component1 = component.Component("Component01",1,1)
        component2 = component.Component("Component02",2,4)
        component3 = component.Component("Component03",3,6)
        component4 = component.Component("Component04",4,8)
        component5 = component.Component("Component05",5,10)
        self.testRepository.addComponent(component1)
        self.testRepository.addComponent(component2)
        self.testRepository.addComponent(component3)
        self.testRepository.addComponent(component4)
        self.testRepository.addComponent(component5)
        self.assertRaises(ValueError, self.testRepository.estimateByRelativeSize, 1,2,"L")
        
    def test_02_23_003_estimateByRelativeSizeExc2(self):
        self.testRepository = repository.Repository(5)
        component1 = component.Component("Component01",1,1)
        component2 = component.Component("Component02",2,4)
        component3 = component.Component("Component03",3,6)
        component4 = component.Component("Component04",4,8)
        component5 = component.Component("Component05",5,10)
        self.testRepository.addComponent(component1)
        self.testRepository.addComponent(component2)
        self.testRepository.addComponent(component3)
        self.testRepository.addComponent(component4)
        self.testRepository.addComponent(component5)
        self.assertRaises(ValueError, self.testRepository.estimateByRelativeSize, "Component01",2,"L")
        
    def test_02_23_004_estimateByRelativeSizeExc3(self):
        self.testRepository = repository.Repository(5)
        component1 = component.Component("Component01",1,1)
        component2 = component.Component("Component02",2,4)
        component3 = component.Component("Component03",3,6)
        component4 = component.Component("Component04",4,8)
        component5 = component.Component("Component05",5,10)
        self.testRepository.addComponent(component1)
        self.testRepository.addComponent(component2)
        self.testRepository.addComponent(component3)
        self.testRepository.addComponent(component4)
        self.testRepository.addComponent(component5)
        self.assertRaises(ValueError, self.testRepository.estimateByRelativeSize, "X",0,"L")
        
    def test_02_23_004_estimateByRelativeSizeExc4(self):
        self.testRepository = repository.Repository(5)
        component1 = component.Component("Component01",1,1)
        component2 = component.Component("Component02",2,4)
        component3 = component.Component("Component03",3,6)
        component4 = component.Component("Component04",4,8)
        component5 = component.Component("Component05",5,10)
        self.testRepository.addComponent(component1)
        self.testRepository.addComponent(component2)
        self.testRepository.addComponent(component3)
        self.testRepository.addComponent(component4)
        self.testRepository.addComponent(component5)
        self.assertRaises(ValueError, self.testRepository.estimateByRelativeSize, "Y","X","L")
        
    def test_02_23_005_estimateByRelativeSizeExc5(self):
        self.testRepository = repository.Repository(5)
        component1 = component.Component("Component01",1,1)
        component2 = component.Component("Component02",2,4)
        component3 = component.Component("Component03",3,6)
        component4 = component.Component("Component04",4,8)
        component5 = component.Component("Component05",5,10)
        self.testRepository.addComponent(component1)
        self.testRepository.addComponent(component2)
        self.testRepository.addComponent(component3)
        self.testRepository.addComponent(component4)
        self.testRepository.addComponent(component5)
        self.assertRaises(ValueError, self.testRepository.estimateByRelativeSize, "Y",2 ,"X") 
        
    def test_02_23_006_estimateByRelativeSizeExc6(self):
        self.testRepository = repository.Repository(5)
        component1 = component.Component("Component01",1,1)
        component2 = component.Component("Component02",2,4)
        component3 = component.Component("Component03",3,6)
        component4 = component.Component("Component04",4,8)
        component5 = component.Component("Component05",5,10)
        self.testRepository.addComponent(component1)
        self.testRepository.addComponent(component2)
        self.testRepository.addComponent(component3)
        self.testRepository.addComponent(component4)
        self.testRepository.addComponent(component5)
        self.assertRaises(ValueError, self.testRepository.estimateByRelativeSize, "Y",2 ,2) 
        
    def test_02_23_007_estimateByRelativeSizeExc7(self):
        self.testRepository = repository.Repository(5)
        component1 = component.Component("Component01",1,1)
        component2 = component.Component("Component02",2,4)
        component3 = component.Component("Component03",3,6)
        component4 = component.Component("Component04",4,8)
        component5 = component.Component("Component05",5,10)
        self.testRepository.addComponent(component1)
        self.testRepository.addComponent(component2)
        self.testRepository.addComponent(component3)
        self.testRepository.addComponent(component4)
        self.testRepository.addComponent(component5)
        self.assertRaises(ValueError, self.testRepository.estimateByRelativeSize)
        
      

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()