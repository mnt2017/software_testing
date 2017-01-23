# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.   
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr
"""

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      
      BEWARE: there may be a bug or two in this code
        
    """
    # require that the input values be > 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
        
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right'
    elif (a == b)  or  (b == c) or (a == c):
        return 'Isoceles'
    else:
        return 'Scalene'
        
        
def runClassifyTriangle(a, b, c):
    """ invoke buggyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c))

# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testClassifyTriangle1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testClassifyTriangle2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Isosceles')
        self.assertEqual(classifyTriangle(10,15,18),'Scalene','Should be Scalene')
        
    def testClassifyTriangle_Bounds(self): 
        #these are our tests
        #Test 200
        self.assertNotEqual(classifyTriangle(200,150,150),'InvalidInput', 'A is 200, Should not be Invalid')
        self.assertNotEqual(classifyTriangle(150,200,150),'InvalidInput', 'B is 200, Should not be Invalid')
        self.assertNotEqual(classifyTriangle(150,150,200),'InvalidInput', 'C is 200, Should not be Invalid')
        #Test >200
        self.assertEqual(classifyTriangle(250,150,150),'InvalidInput', 'A is greater than 200, Should be Invalid')
        self.assertEqual(classifyTriangle(150,250,150),'InvalidInput', 'B is greater than 200, Should be Invalid')
        self.assertEqual(classifyTriangle(150,150,250),'InvalidInput', 'C is greater than 200, Should be Invalid')
        #Test 0
        self.assertEqual(classifyTriangle(0,150,150),'InvalidInput', 'A is 0, Should be Invalid')
        self.assertEqual(classifyTriangle(150,0,150),'InvalidInput', 'B is 0, Should be Invalid')
        self.assertEqual(classifyTriangle(150,150,0),'InvalidInput', 'C is 0, Should be Invalid')
        #Test <0
        self.assertEqual(classifyTriangle(-5,150,150),'InvalidInput', 'A is less than 0, Should be Invalid')
        self.assertEqual(classifyTriangle(150,-5,150),'InvalidInput', 'B is less than 0, Should be Invalid')
        self.assertEqual(classifyTriangle(150,150,-5),'InvalidInput', 'C is less than 0, Should be Invalid') 
        #Test <0
        self.assertEqual(classifyTriangle(-5,150,150),'InvalidInput', 'A is less than 0, Should be Invalid')
        self.assertEqual(classifyTriangle(150,-5,150),'InvalidInput', 'B is less than 0, Should be Invalid')
        self.assertEqual(classifyTriangle(150,150,-5),'InvalidInput', 'C is less than 0, Should be Invalid') 

    def testClassifyTriangle_Int(self):
        self.assertEqual(classifyTriangle(150.5,150,100),'InvalidInput', 'A is not int, Should be Invalid') 
        self.assertEqual(classifyTriangle(150,150.5,100),'InvalidInput', 'B is not int, Should be Invalid') 
        self.assertEqual(classifyTriangle(150,100,150.5),'InvalidInput', 'C is not int, Should be Invalid') 
        
    def testClassifyTriangle_Valid(self):
        self.assertEqual(classifyTriangle(10,5,5),'NotATriangle', 'A is exactly too long, Should be NotATriangle') 
        self.assertEqual(classifyTriangle(5,10,5),'NotATriangle', 'B is exactly too long, Should be NotATriangle') 
        self.assertEqual(classifyTriangle(5,5,10),'NotATriangle', 'C is exactly too long, Should be NotATriangle') 

    def testClassifyTriangle_Type(self):
         self.assertEqual(classifyTriangle(5,5,5),'Equilateral', 'Should be Equilateral')
         self.assertEqual(classifyTriangle(5,5,7),'Isoceles', 'A & B are same, Should be Isoceles') 
         self.assertEqual(classifyTriangle(5,7,5),'Isoceles', 'A & C are same. Should be Isoceles')        
         self.assertEqual(classifyTriangle(7,5,5),'Isoceles', 'B & C are same. Should be Isoceles')
         self.assertEqual(classifyTriangle(3,4,5),'Right', 'Should be Right') 
         self.assertEqual(classifyTriangle(4,5,6),'Scalene', 'Should be Scalene') 

         
if __name__ == '__main__':
# examples of running the  code
#    runClassifyTriangle(1,2,3)
#    runClassifyTriangle(1,1,1)
#    runClassifyTriangle(3,4,5)
    
    print('Begin UnitTest')
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       