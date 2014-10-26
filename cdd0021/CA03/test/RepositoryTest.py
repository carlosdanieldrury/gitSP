import unittest
import CA03.prod.Repository as Repository
import CA03.prod.Component as Component

class TestRepository(unittest.TestCase):

# Constructor
    #100_0xx ... happy 
    def test100_010_ShouldConstructRepositoryExplicitCapacity(self):
        self.assertIsInstance(Repository.Repository(capacity=100), Repository.Repository)
        
    def test100_020_ShouldConstructRepositoryDefaultCapacity(self):
        self.assertIsInstance(Repository.Repository(), Repository.Repository)
        
    #100_9xx ... sad path
    def test100_910_ShouldRaiseExceptionOnNonIntCapacity(self):
        expectedString = "Repository.__init__:  "
        try:
            myRepository = Repository.Repository("a")                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
    
    def test100_920_ShouldRaiseExceptionOnInvalidCapacity(self):
        expectedString = "Repository.__init__:  "
        try:
            myRepository = Repository.Repository(capacity=0)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  

    
# addComponent
    #200_0xx ... happy path
    def test200_010_shouldAddComponent(self):
        maxCapacity = 2
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            self.assertEquals(i+1, theRepository.addComponent(Component.Component("C"+str(i), i+1, i+1)))
            
    def test200_020_shouldAddComponentPastCapacity(self):
        maxCapacity = 2
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), i+1, i+1))
            
        self.assertEquals(maxCapacity, theRepository.addComponent(Component.Component("overflow", 1, 10)))
        
    def test200_020_shouldDeleteOldestPastCapacity(self):
        maxCapacity = 2
        theRepository = Repository.Repository(maxCapacity)
        # Add maxCapacity+1 components
        # Ensure the first one has a zero method count, all others have non-zero method count
        # We infer that the first component -- the only component with a non-zero method count -- has
        # been deleted if validCount() == 2
        for i in range(maxCapacity+1):
            theRepository.addComponent(Component.Component("C"+str(i), i, i+1))
        self.assertEquals(2, theRepository.validCount())
        
    def test200_910_shouldRaiseExceptionIfComponentMissing(self):
        expectedString = "Repository.addComponent:  "
        theRepository = Repository.Repository()
        try:                                             
            theRepository.addComponent()
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
            
         
# count
    #300_0xx ... happy path
    def test300_010_shouldReturnInt(self):
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), i+1, i+1))
        self.assertIsInstance(theRepository.count(), int)
            
        self.assertEquals(maxCapacity, theRepository.addComponent(Component.Component("overflow", 1, 10)))    
    def test300_020_shouldReturnCount(self):
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), i+1, i+1))
            self.assertEqual(i+1, theRepository.count())
        self.assertEquals(maxCapacity, theRepository.addComponent(Component.Component("overflow", 1, 10)))
        
        
# validCount
    #400_0xx ... happy path
    def test400_010_shouldReturnInt(self):
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), i+1, i+1))
        self.assertIsInstance(theRepository.validCount(), int)  
         
    def test500_010_shouldReturnValidCount(self):
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), 0, i+1))
            self.assertEqual(0, theRepository.validCount())
        
# detereminedetermineRelativeSizes
    #600_0xx . . . happy path
    def test600_010_shouldReturnIntList(self):
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        methodCounts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        locCounts = [42, 19, 58, 60, 70, 82, 57, 89, 80, 128]
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), methodCounts[i], locCounts[i]))
        listOfSizes = theRepository.determineRelativeSizes()
        self.assertIsInstance(listOfSizes, list)
        for size in listOfSizes:
            self.assertIsInstance(size, int)
        
    def test600_020_shouldReturnSizeList(self):
        # test set:
        #name methods LOC   ln(loc/methods)
        #C0    0    42    NA
        #C1    1    19    2.944438979
        #C2    2    58    3.36729583
        #C3    3    60    2.995732274
        #C4    4    70    2.862200881
        #C5    5    82    2.797281335
        #C6    6    57    2.251291799
        #C7    7    89    2.542726221
        #C8    8    80    2.302585093
        #C9    9    128    2.654805687
        #          avg = 2.746484233
        #          stdev = 0.352645834
        #  This yields [8, 11, 16, 23, 32]
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        methodCounts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        locCounts = [42, 19, 58, 60, 70, 82, 57, 89, 80, 128]
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), methodCounts[i], locCounts[i]))
        self.assertListEqual([8, 11, 16, 23, 32], theRepository.determineRelativeSizes())        
        
    def test600_030_shouldReturnSizeList(self):
        # test set:
        #name methods LOC   ln(loc/methods)
        #C0    0    42    NA
        #C1    1    19    2.944438979
        #C2    2    58    3.36729583
        #C3    3    60    2.995732274
        #C4    4    70    2.862200881
        #C5    5    82    2.797281335
        #C6    6    57    2.251291799
        #C7    7    89    2.542726221
        #C8    8    80    2.302585093
        #C9    9    128    2.654805687
        #          avg = 2.746484233
        #          stdev = 0.352645834
        #  This yields [8, 11, 16, 23, 32]
        maxCapacity = 4
        theRepository = Repository.Repository(maxCapacity)
        methodCounts = [1, 4, 7, 5]
        locCounts = [76, 116, 113, 103]
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), methodCounts[i], locCounts[i]))
        self.assertListEqual([8, 15, 30, 58, 115], theRepository.determineRelativeSizes())        
        
    #600_9xx . . . sad path
    def test600_910_shouldRaiseExceptionOnSmallCapacity(self):  
        expectedString = "Repository.determineRelativeSizes:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("LoneComponent", 1, 10))
        try:
            theRepository.determineRelativeSizes()                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
            
    def test600_920_shouldRaiseExceptionOnTooFewValidComponents(self):  
        expectedString = "Repository.determineRelativeSizes:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("NonZero", 1, 10))
        theRepository.addComponent(Component.Component("Zero", 0, 10))
        try:
            theRepository.determineRelativeSizes()                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
            
#---------------- CA02 -------------------------    
# addComponent       
    def test200_920_shouldObjectToDuplicateComponent(self):
        expectedString = "Repository.addComponent:  "
        theRepository = Repository.Repository()
        theComponent = Component.Component("X", 5, 100)
        duplicateComponent = Component.Component("X", 1, 10)
        theRepository.addComponent(theComponent)
        try:                                             
            theRepository.addComponent(duplicateComponent)
            self.fail()                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
            
# estimateRelativeSize(name, methodCount, size)       
    def test700_010_shouldReturnInstanceOfComponent(self):
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), i+1, i+10))   
        self.assertIsInstance(theRepository.estimateByRelativeSize("a",3, "M"), Component.Component)    
        
    def test700_020_shouldEstimateRelativeSize(self):
        theRepository = Repository.Repository()
        sizeList = ["VS", "S", "M", "L","VL"]
        methodCounts = [1, 4, 7, 5]
        locCounts = [76, 116, 113, 103]
        expectedSizes = [8, 15, 30, 58, 115]
        for i in range(len(methodCounts)):
            theRepository.addComponent(Component.Component("C"+str(i), methodCounts[i], locCounts[i]))
        newMethodCount = 10
        newRelativeSize = "L"
        newComponent = theRepository.estimateByRelativeSize("New", newMethodCount, newRelativeSize)
        self.assertEquals(newMethodCount*expectedSizes[sizeList.index(newRelativeSize)], newComponent.getLocCount()) 
        
    def test700_030_ShouldEstimateRelativeSizeWithDefaultSize(self):
        theRepository = Repository.Repository()
        sizeList = ["VS", "S", "M", "L","VL"]
        methodCounts = [1, 4, 7, 5]
        locCounts = [76, 116, 113, 103]
        expectedSizes = [8, 15, 30, 58, 115]
        for i in range(len(methodCounts)):
            theRepository.addComponent(Component.Component("C"+str(i), methodCounts[i], locCounts[i]))
        newMethodCount = 10
        newRelativeSize = "M"
        newComponent = theRepository.estimateByRelativeSize("New", newMethodCount)
        self.assertEquals(newMethodCount*expectedSizes[sizeList.index(newRelativeSize)], newComponent.getLocCount()) 
        
    def test700_910_ShouldObjectToMissingName(self):
        expectedString = "Repository.estimateByRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        theRepository.addComponent(Component.Component("C2", 1, 10))
        try:
            theRepository.estimateByRelativeSize(methodCount = 1, size = "M")                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  

    def test700_920_ShouldObjectToNonStringName(self):
        expectedString = "Repository.estimateByRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        theRepository.addComponent(Component.Component("C2", 1, 10))
        try:
            theRepository.estimateByRelativeSize(name = 42, methodCount = 1, size = "M")                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
            
    def test700_930_ShouldObjectToEmptyStringName(self):
        expectedString = "Repository.estimateByRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        theRepository.addComponent(Component.Component("C2", 1, 10))
        try:
            theRepository.estimateByRelativeSize(name = "", methodCount = 1, size = "M")                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
        
    def test700_940_ShouldObjectToMissingMethodCount(self):
        expectedString = "Repository.estimateByRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        theRepository.addComponent(Component.Component("C2", 1, 10))
        try:
            theRepository.estimateByRelativeSize(name = "New", size = "M")                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
            
    def test700_950_ShouldObjectToZeroMethodCount(self):
        expectedString = "Repository.estimateByRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        theRepository.addComponent(Component.Component("C2", 1, 10))
        try:
            theRepository.estimateByRelativeSize(name = "New", methodCount = 0, size = "M")                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
            
    def test700_960_ShouldObjectToNonIntMethodCount(self):
        expectedString = "Repository.estimateByRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        theRepository.addComponent(Component.Component("C2", 1, 10))
        try:
            theRepository.estimateByRelativeSize(name = "New", methodCount = "a", size = "M")                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  

    def test700_970_ShouldObjectToBadSize(self):
        expectedString = "Repository.estimateByRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)  
        theRepository.addComponent(Component.Component("C1", 1, 10))
        theRepository.addComponent(Component.Component("C2", 1, 10))
        try:
            theRepository.estimateByRelativeSize(name = "New", methodCount = 5, size = "VVL")                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
        
    def test700_980_ShouldObjectToSmallRepository(self):
        expectedString = "Repository.estimateByRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        try:
            theRepository.estimateByRelativeSize(name = "New", methodCount = 5, size = "M")                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
            
    def test700_985_ShouldObjectToSmallRepository(self):
        expectedString = "Repository.estimateByRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        theRepository.addComponent(Component.Component("C2", 0, 10))
        try:
            theRepository.estimateByRelativeSize(name = "New", methodCount = 5, size = "M")                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  

    def test700_990_ShouldObjectToDuplicateName(self):
        expectedString = "Repository.estimateByRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        theRepository.addComponent(Component.Component("C2", 1, 10))
        try:
            theRepository.estimateByRelativeSize(name = "C1", methodCount = 5, size = "M")                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
            
            
# getRelativeSize(component)
    def test800_010_ShouldReturnRelativeSize(self):
        theRepository = Repository.Repository()
        sizeList = ["VS", "S", "M", "L","VL"]
        methodCounts = [1, 4, 7, 5]
        locCounts = [76, 116, 113, 103]
        expectedSizes = [8, 15, 29, 58, 115]
        for i in range(len(methodCounts)):
            theRepository.addComponent(Component.Component("C"+str(i), methodCounts[i], locCounts[i]))
        newComponent = Component.Component("New", 1, 30)
        newRelativeSize = "M"
        self.assertEquals(newRelativeSize, theRepository.getRelativeSize(newComponent))
        
    def test800_020_ShouldReturnRelativeSizeEdgeCase(self):
        theRepository = Repository.Repository()
        sizeList = ["VS", "S", "M", "L","VL"]
        methodCounts = [1, 4, 7, 5]
        locCounts = [76, 116, 113, 103]
        midPointSizes = [8, 15, 30, 58, 115]
        lowerEdge = [0,11,21,42,82]
        upperEdge = [11, 21, 42, 82, "big"]
        for i in range(len(methodCounts)):
            theRepository.addComponent(Component.Component("C"+str(i), methodCounts[i], locCounts[i]))
        newComponent = Component.Component("New", 1, 42)
        newRelativeSize = "L"
        self.assertEquals(newRelativeSize, theRepository.getRelativeSize(newComponent))
        
    def test800_900_ShouldObjectToMissingComponent(self):
        expectedString = "Repository.getRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        theRepository.addComponent(Component.Component("C2", 1, 10))
        try:
            theRepository.getRelativeSize()                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
            
    def test800_910_ShouldObjectToZeroMethodComponents(self):
        expectedString = "Repository.getRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        theRepository.addComponent(Component.Component("C2", 1, 10))
        try:
            theRepository.getRelativeSize(Component.Component("New", 0, 10))                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  
            
    
    def test800_920_ShouldObjectToSmallRepository(self):
        expectedString = "Repository.getRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        try:
            theRepository.getRelativeSize(Component.Component("New", 0, 10))                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  

    def test800_930_ShouldObjectToSmallRepository(self):
        expectedString = "Repository.getRelativeSize:  " 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("C1", 1, 10))
        theRepository.addComponent(Component.Component("C2", 0, 10))
        try:
            theRepository.getRelativeSize(Component.Component("New", 0, 10))                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))  

if __name__ == '__main__':
    unittest.main()
            