'''
Created on Oct 21, 2014

@author: drury
'''
import unittest
import CA03.prod.PythonScript as PythonScript


class TestPythonScript(unittest.TestCase):


#Constructor
    # happy
    def test100_010_ShouldConstructorWorkPythonFile(self):
        testPythonScript = PythonScript.PythonScript(fileName="pythonFile.py")
        
    def test100_020_ShouldReceiveNameOfFile(self):
        testFileName = "pythonFile.py"
        testPythonScript = PythonScript.PythonScript(fileName="pythonFile.py")
        self.assertEquals(testFileName, testPythonScript.getFileName())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()