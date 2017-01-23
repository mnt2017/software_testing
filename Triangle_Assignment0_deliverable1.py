import unittest
import math

def classifytriangle(a,b,c):

       d = [a, b, c]  # create list of sides of triangle
       
       a_sq =math.pow(a,2)
       b_sq =math.pow(b,2)
       c_sq =math.pow(c,2)
       sum_sq = a_sq + b_sq
       res_flag = 0  # result flag
       if d[0] == 0 or d[1] == 0 or d[2] == 0:
          print "test for not a triangle"
          result ="Its not a triangle"
          print result
          res_flag = 1
       # test for equilateral
       if d[0] == d[2]:
          print "test for equilateral triangle"
          result = "equilateral "
          print result
          res_flag = 1
       # test for isosceles
       elif d[0] == d[1] or d[1] == d[2]:
          print "test for isosceles triangle"
          result = "isosceles "
          print result
          res_flag = 1
       # test pythagorean theorem to find right angle
       elif sum_sq == c_sq:
            print "test for right angled triangle"
            result = "right angle"
            print result
            res_flag = 1
       # test for scalene
       elif d[0]!=0 and d[1]!=0 and d[2]!=0:
            print "test for scalene triangle"
            result = "scalene "
            print result
            res_flag = 1
	     
      
       return res_flag
  
class Mytest(unittest.TestCase):

  def runTest(self):
    self.assertEqual(classifytriangle(0, 3, 1.5), 1)
    self.assertEqual(classifytriangle(3,0, 1.5), 1)
    self.assertEqual(classifytriangle(3, 1.5,0), 1)
    self.assertEqual(classifytriangle(2, 2, 5), 1)
    self.assertEqual(classifytriangle(2, 3, 2), 1)
    self.assertEqual(classifytriangle(2, 3, 1.5), 1)
    self.assertEqual(classifytriangle(3,4,5), 1)
  
if __name__ == '__main__':
    print"inside main"

else:
    print("its is being imported into another module done for future use")
    app= Mytest(); # object of Mytest
    app.runTest();  # method called from unittest 
    

    

    
  









