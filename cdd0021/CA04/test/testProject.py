'''
Created on Nov 5, 2014

@author: drury
'''
import unittest
import CA04.prod.Project as Project
import CA04.prod.Iteration as Iteration


class Test(unittest.TestCase):

#Happy
    def test100_010_ShouldConstructProject(self):
        self.assertIsInstance(Project.Project(), Project.Project)
        
    def test100_020_ShouldAddIteration(self):
        myProject = Project.Project()
        self.assertEquals(myProject.add(iteration = Iteration.Iteration(120,3)), 1)
        
    def test100_030_ShouldGetIterationCount(self):
        myIteration = Iteration.Iteration(30,4)
        myProject = Project.Project()
        myProject.add(myIteration)
        self.assertEquals(myProject.getIterationCount(), 1)
    
    def test100_040_ShouldGetIteration(self):
        myIteration = Iteration.Iteration(30,4)
        myProject = Project.Project()
        myProject.add(myIteration)
        self.assertEquals(myProject.getIteration(iterationNumber=1), "<Iteration(30,4)>")
         
    def test100_050_ShouldGetEffortProject(self):
        myIteration = Iteration.Iteration(30,4)
        myProject = Project.Project()
        myProject.add(myIteration)
        self.assertEquals(myProject.getEffort(), 30)
        
    def test100_060_ShouldGetPVProject(self):
        myIteration = Iteration.Iteration(30,4)
        myProject = Project.Project()
        myProject.add(myIteration)
        self.assertEquals(myProject.getPV(), 4)

#sad
    def test200_010_ShouldRaiseExceptionGetIterationInvalid(self):
        myIteration = Iteration.Iteration(100,10)
        myProject = Project.Project()
        myProject.add(myIteration)
        expectedString = "Project.getIteration:  "
        try:
            myProject.getIteration(42)                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
        
    def test200_020_ShouldRaiseExceptionAddNoParam(self):
        myProject = Project.Project()
        expectedString = "Project.add:  "
        try:
            myProject.add()                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")   
            
    def test200_030_ShouldRaiseExceptionGetIterationInvalidValue(self):
        myIteration = Iteration.Iteration(100,10)
        myProject = Project.Project()
        myProject.add(myIteration)
        expectedString = "Project.getIteration:  "
        try:
            myProject.getIteration(0)                                        
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")   
            
    def test200_040_ShouldRaiseExceptionGetIterationString(self):
        myIteration = Iteration.Iteration(100,10)
        myProject = Project.Project()
        myProject.add(myIteration)
        expectedString = "Project.getIteration:  "
        try:
            myProject.getIteration("X")                                        
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")     



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test100_010_ShouldConstructProject']
    unittest.main()