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
        myIteration = Iteration.Iteration(effort=120, plannedVelocity=3)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()