'''
Created on Nov 5, 2014

@author: drury
'''
import unittest
import CA04.prod.Project as Project
import CA04.prod.Iteration as Iteration


class Test(unittest.TestCase):


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

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test100_010_ShouldConstructProject']
    unittest.main()