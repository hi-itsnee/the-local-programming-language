import unittest 
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import local
import testinputs
import testoutputs

# RUN: python -m unittest cond-test.TestCond.test_if
# RUN: python -m unittest cond-test

class TestCond(unittest.TestCase):
    def setUp(self):
	print "Begin Conditional Testing"

    def test_if(self):
    # Test a single 'if' statement
        target_result = testoutputs.if_test
#	target_result = open('cond_if.test').read().strip()
	actual_result = local.tester(testinputs.if_test)
#       actual_result = local.tester('if a\n    print("a is true");\nelse\n    print("a is false");')
	self.assertEqual(target_result, actual_result)
        # can verify that this is the correct python result by looking

    def test_ifelse(self):
    # Test an if statement that includes an else
#	target_result = open('cond_ifelse.test').read().strip()
        target_result = testoutputs.ifelse_test
	actual_result = local.tester(testinputs.ifelse_test)
	self.assertEqual(target_result, actual_result)

if __name__ == '__main__':
    unittest.main()
