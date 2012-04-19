import unittest 
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import local
import testinputs
import testoutputs

# RUN: python -m unittest module-testing.TestCond.test_if
# RUN: python -m unittest module-testing

class TestCond(unittest.TestCase):
    def setUp(self):
	print "Begin Conditional Testing"

    def test_if(self):
    # Test a single 'if' statement
        target_result = testoutputs.if_test
	actual_result = local.tester(testinputs.if_test)
	self.assertEqual(target_result, actual_result)
        # verify that this is the correct python result by looking

    def test_ifelse(self):
    # Test an if statement that includes an else
        target_result = testoutputs.ifelse_test
	actual_result = local.tester(testinputs.ifelse_test)
	self.assertEqual(target_result, actual_result)

class TestMath(unittest.TestCase):
    def setUp(self):
        print "Begin Math Testing"

    def test1_math(self):
    # Test a math expression
        target_result = testoutputs.math_test1
        actual_result = local.tester(testinputs.math_test1)
	self.assertEqual(target_result, actual_result)

if __name__ == '__main__':
    unittest.main()
