'''
Created on Oct 21, 2014

@author: drury
'''
import unittest
import CA03.prod.PythonScript as PythonScript
import os
import CA03.prod.Component as Component


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
        
    def test100_040_ShouldReturnNumberOfLines(self):
        numberOfLines = 11
        testFileName = "pythonFile.py"
        testPythonScript = PythonScript.PythonScript(fileName=testFileName)
        self.assertEquals(numberOfLines, testPythonScript.countLine())
        
    def test100_050_ShouldReturnAListWithCompInfo(self):
        list = '[[Component("ClassA",2,5), Component("ClassB",1,3)], [Component("Func",1,2)]]'
        testFileName = "pythonFile.py"
        file = open(testFileName, 'r')
        testPythonScript = PythonScript.PythonScript(fileName=testFileName)
        self.assertEquals(list, testPythonScript.extractDesign().__repr__())
        
    def test100_060_ShouldCountLineOfEmptyFile(self):
        numberOfLines = 0
        testFileName = "file.py"
        testPythonScript = PythonScript.PythonScript(fileName=testFileName)
        self.assertEquals(numberOfLines, testPythonScript.countLine())
        
    def test100_070_ShouldReturnEmptyListCompInfo(self):
        list = '[[], []]'
        testFileName = "file.py"
        testPythonScript = PythonScript.PythonScript(fileName=testFileName)
        self.assertEquals(list, testPythonScript.extractDesign().__repr__())
    
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()