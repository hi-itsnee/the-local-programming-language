import unittest 
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import local
import pt_testin
import pt_testout

# RUN: python -m unittest program_testing.TestHelloWorld.test_hw
# RUN: python -m unittest program_testing

# Comment in MacVim: 'v' --> :'<,'>s/^/#/g
# Uncomment in MacVim: 'v' --> :'<,'>s/^#//g

     
class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        print "Begin Hello World Test"

    def test_hw(self):
        target_result = pt_testout.helloworld_test
        actual_result = local.tester(pt_testin.helloworld_test)
	self.assertEqual(target_result, actual_result)  

class Example1(unittest.TestCase):
    def setUp(self):
        print "Begin Example 1"

    def test_example1(self):
        target_result = pt_testout.example1_test
        actual_result = local.tester(pt_testin.example1_test)
	self.assertEqual(target_result, actual_result)    

class Tutorial2(unittest.TestCase):
    def setUp(self):
        print "Begin Tutorial Test #2: Variables & Arithmetic Expressions"

    def test_tutorial2(self):
        target_result = pt_testout.tutorial2_test
        actual_result = local.tester(pt_testin.tutorial2_test)
	self.assertEqual(target_result, actual_result)    

class Tutorial3(unittest.TestCase):
    def setUp(self):
        print "Begin Tutorial Test #3: Loops"

    def test_tutorial3(self):
        target_result = pt_testout.tutorial3_test
        actual_result = local.tester(pt_testin.tutorial3_test)
	self.assertEqual(target_result, actual_result)    

class Tutorial4(unittest.TestCase):
    def setUp(self):
        print "Begin Tutorial Test #4: Input/Output"

    def test_tutorial4(self):
        target_result = pt_testout.tutorial4_test
        actual_result = local.tester(pt_testin.tutorial4_test)
	self.assertEqual(target_result, actual_result)    

class Tutorial5(unittest.TestCase):
    def setUp(self):
        print "Begin Tutorial Test #5: Functions"

    def test_tutorial5(self):
        target_result = pt_testout.tutorial5_test
        actual_result = local.tester(pt_testin.tutorial5_test)
	self.assertEqual(target_result, actual_result)    

if __name__ == '__main__':
    unittest.main()
