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
        target_result = testoutputs.helloworld_test
        actual_result = local.tester(testinputs.helloworld_test)
	self.assertEqual(target_result, actual_result)  

class Example1(unittest.TestCase):
    def setUp(self):
        print "Begin Example 1"

    def test_example1(self):
        target_result = testoutputs.example1_test
        actual_result = local.tester(testinputs.example1_test)
	self.assertEqual(target_result, actual_result)    

class TestLogic(unittest.TestCase):
    def setUp(self):
        print "Begin Logic Test"

    def test_example1(self):
        target_result = pt_testout.example1_test
        actual_result = local.tester(open('./local_files/logic-test.local').read().strip())
	self.assertEqual(target_result, actual_result)    

if __name__ == '__main__':
    unittest.main()
