'''
Created on Nov 5, 2014

@author: drury
'''
import unittest
import CA04.prod.Project as Project


class Test(unittest.TestCase):


    def test100_010_ShouldConstructProject(self):
        self.assertIsInstance(Project.Project(), Project.Project)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test100_010_ShouldConstructProject']
    unittest.main()