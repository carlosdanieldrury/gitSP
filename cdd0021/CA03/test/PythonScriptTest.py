'''
Created on Oct 21, 2014

@author: drury
'''
import unittest
import CA03.prod.PythonScript as PythonScript
import os


class TestPythonScript(unittest.TestCase):


#Constructor
    # happy
    def test100_010_ShouldConstructorWorkPythonFile(self):
        testPythonScript = PythonScript.PythonScript(fileName="pythonFile.py")
        
    def test100_020_ShouldReceiveNameOfFile(self):
        testFileName = "pythonFile.py"
        testPythonScript = PythonScript.PythonScript(fileName=testFileName)
        self.assertEquals(testFileName, testPythonScript.getFileName())
        
    def test100_030_ShouldReturnFilePath(self):
        testFileName = "pythonFile.py"
        testFilePath = os.path.abspath(testFileName)
        testPythonScript = PythonScript.PythonScript(fileName=testFileName)
        self.assertEquals(testFilePath, testPythonScript.getFilePath())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()