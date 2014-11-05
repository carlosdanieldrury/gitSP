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


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test100_010_ShouldConstructProject']
    unittest.main()