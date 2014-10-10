'''
Created on Sep 11, 2014

@author: drury
'''
from CA02.prod import Component as component
import math

class Repository(object):
    '''
    Repository class is a collection of Components 
    '''


    def __init__(self, capacity=None):
        '''
        Constructor
        '''
        self.repository = []
        self.ocupancy = 0
        if capacity == None:
            self.capacity = 100
        else:
            if capacity > 0:
                self.capacity = capacity
            else:
                raise ValueError("Repository.__init__: The capacity needs to be grand than 0")
        
    def count(self):
        '''
        Method count: used to return how many components are in the repository
        '''
        return len(self.repository)
    
    def getCapacity(self):
        '''
        Method getCapacity: returns the capacity of the repository
        '''
        return self.capacity
    
    def addComponent(self,Comp=None):
        '''
        Method addComponent - Add a component into the repository. Need a parameter.
        '''
        if Comp==None:
            raise ValueError("Repository.addComponent: The method addComponent needs a parameter")
        else:
            #check first if the repository is not full
            if (self.getCapacity() == self.ocupancy):
                self.ocupancy -= 1
                self.repository.popleft()
            
            for comp in self.repository:
                if (comp == Comp):
                    raise ValueError("Repository.addComponent: This component is already in the repository")
                if (comp.getName() == Comp.getName()):
                    raise ValueError("Repository.addComponent: There is a component with the same name inside the repository")
                 
            self.repository.append(Comp)
            self.ocupancy += 1

                
        
    def validCount(self):
        '''
        Method validCount: returns how many components have valid methods.
        '''
        cont = 0
        for comp in self.repository:
            if (comp.methodCount > 0):
                cont = cont + 1
        return cont
    
  
    def determineRelativeSizes(self):
        '''
        Method determineRelativeSizes: returns a list with what the size of very small, small, medium, large and very large methods.
        '''
        #variables 
        normalizedSize = 0

        avg = 0
        stdev = 0

        
        for comp in self.repository:
            if (comp.getMethodCount() == 0):
                pass
            else:
                try:
                    normalizedSize = math.log(comp.getLocCount() // comp.getMethodCount())
                    avg = avg + normalizedSize
                except:
                    print "Division by 0"
 
        #average    
        avg = avg / self.validCount()    
            
        for comp in self.repository:
            if (comp.getMethodCount() == 0):
                pass
            else:
                try:
                    normalizedSize = math.log(comp.getLocCount() // comp.getMethodCount())
                    stdev = stdev + ((math.pow(normalizedSize - avg, 2))/ (self.validCount() - 1))
                except:
                    print "Division by 0.."
        #stdev final calculation   
        stdev = math.sqrt(stdev)
        
        
        vs = math.ceil(math.exp(avg - 2*stdev))
        
        s =  math.ceil(math.exp(avg - stdev))
        
        m = math.ceil(math.exp(avg))
        
        l = math.ceil(math.exp(avg+stdev))
        
        vl = math.ceil(math.exp(avg + 2*stdev))
        
        return [vs,s,m,l,vl]
    
    
    def getRelativeSize(self, Comp=None):
        if len(self.repository) < 5:
            raise ValueError("Repository.getRelativeSize: There is no enough number of components")
        if Comp==None:
            raise ValueError("Repository.getRelativeSize: Missing a parameter of the component")
        for comp in self.repository:
            normalizedSize = 0
            avg = 0
            stdev = 0
            
            for subComp in self.repository:
                if (subComp.getMethodCount() == 0):
                    pass
                else:
                    try:
                        normalizedSize = math.log(subComp.getLocCount() // subComp.getMethodCount())
                        avg = avg + normalizedSize
                    except:
                        print "Division by 0"
     
            #average    
            avg = avg / self.validCount()    
                
            for subComp in self.repository:
                if (subComp.getMethodCount() == 0):
                    pass
                else:
                    try:
                        normalizedSize = math.log(subComp.getLocCount() // subComp.getMethodCount())
                        stdev = stdev + ((math.pow(normalizedSize - avg, 2))/ (self.validCount() - 1))
                    except:
                        print "Division by 0.."
            #stdev final calculation   
            stdev = math.sqrt(stdev)
            
        if Comp.getMethodCount != 0:
            sizeComp = Comp.getLocCount() / Comp.getMethodCount()
        else:
            raise ValueError("Repository.getRelativeSize: The component has 0 methodCount")
        
        #Relative Size
        vs = math.ceil(math.exp(avg - 1.5*stdev))
        if sizeComp <= vs:
            comp.setRelativeSize("VS")
        

        m1 = math.ceil(-0.5*math.exp(avg))
        m2 = math.ceil(0.5*math.exp(avg))
        if ((sizeComp > vs) and (sizeComp <= m1)):
            Comp.setRelativeSize("S")
            
        
        
        if ((sizeComp>m1) and (sizeComp<=m2)):
            Comp.setRelativeSize("M")

        vl = math.ceil(math.exp(avg + 2*stdev))
        if ((sizeComp>m2) and (sizeComp<=vl)):
            Comp.setRelativeSize("L")
            
        if (sizeComp>vl):
            Comp.setRelativeSize("VL")
                
        
        return Comp.getRelativeSize()
            
    def estimateByRelativeSize(self,name=None,methodCount=None,size=None):
        if len(self.repository) < 5:
            raise ValueError("Repository.getRelativeSize: There is no enough number of components")
        if name==None:
            raise ValueError("Repository.estimateByRelativeSize: The name is missing")
        if methodCount==None:
            raise ValueError("Repository.estimateByRelativeSize: The methodCount is missing")
        if size==None:
            raise ValueError("Repository.estimateByRelativeSize: The size is missing")
        
        for comp in self.repository:
            if comp.getName()==name:
                raise ValueError("Repository.estimateByRelativeSize: The name of the component is already in the repository")
        if methodCount==0:
            raise ValueError("Repository.estimateByRelativeSize: MethodCount equal to 0 makes the relative size equal to 0")
        listSizes = self.determineRelativeSizes()
        #print listSizes
        relativeSizes = {"VS":listSizes[0], "S":listSizes[1],
                         "M":listSizes[2], "L":listSizes[3],
                         "VL":listSizes[4]}
        if (relativeSizes.__contains__(size)):
            estimatedSize = methodCount * int(relativeSizes[size])
            componentNew = component.Component(name,methodCount,estimatedSize)
            return componentNew
        else:
            raise ValueError("Repository.estimateByRelativeSize: size needs to be VS, S, M, L or VL")
            