import unittest 
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import local
import gt_testin
import gt_testout

# RUN: python -m unittest grammar_testing.TestCond.test_if
# RUN: python -m unittest grammar_testing

# Comment in MacVim: 'v' --> :'<,'>s/^/#/g
# Uncomment in MacVim: 'v' --> :'<,'>s/^#//g


class TestAssign(unittest.TestCase):
    def setUp(self):
        print "Begin Assignment Testing"

    def test_assign(self):
        target_result = gt_testout.assign_test
        actual_result = local.tester(gt_testin.assign_test)
	self.assertEqual(target_result, actual_result)   

class TestCond(unittest.TestCase):
    def setUp(self):
	print "Begin Conditional Testing"

    def test_if(self):
    # Test a single 'if' statement
        target_result = gt_testout.if_test
	actual_result = local.tester(gt_testin.if_test)
	self.assertEqual(target_result, actual_result)
        # verify that this is the correct python result by looking

    def test_ifelse(self):
    # Test an if statement that includes an else
        target_result = gt_testout.ifelse_test
	actual_result = local.tester(gt_testin.ifelse_test)
	self.assertEqual(target_result, actual_result)

    def test_nesting(self):
    # Test a nested if-else within an if-else
        target_result = gt_testout.nesting_test
	actual_result = local.tester(gt_testin.nesting_test)
	self.assertEqual(target_result, actual_result)    

#class TestCoord(unittest.TestCase):
    def setUp(self):
        print "Begin Coordinate Testing"

    def test_coord(self):
        target_result = gt_testout.coord_test
        actual_result = local.tester(gt_testin.coord_test)
	self.assertEqual(target_result, actual_result)   

#class TestExit(unittest.TestCase):
    def setUp(self):
        print "Begin Exit Testing"

    def test_exit(self):
        target_result = gt_testout.exit_test
        actual_result = local.tester(gt_testin.exit_test)
	self.assertEqual(target_result, actual_result)   

class TestExpr(unittest.TestCase):
    def setUp(self):
        print "Begin Expression Testing"
    
    def test_binop(self):
        # Test all the binop statements
        target_result = gt_testout.binop_test
        actual_result = local.tester(gt_testin.binop_test)
        self.assertEqual(target_result, actual_result)  
    
    def test_indices(self):
        # Test the array statement
        target_result = gt_testout.indices_test
        actual_result = local.tester(gt_testin.indices_test)
        self.assertEqual(target_result, actual_result)  

    def test_unary(self):
        # Test all the unary statements
        target_result = gt_testout.unary_test
        actual_result = local.tester(gt_testin.unary_test)
        self.assertEqual(target_result, actual_result)  
       
class TestIO(unittest.TestCase):
    def setUp(self):
        print "Begin I/O Testing"

    def test_io(self):
    # Test a file write expression
        target_result = gt_testout.io_test
        actual_result = local.tester(gt_testin.io_test)
	self.assertEqual(target_result, actual_result)
 
class TestMath(unittest.TestCase):
    def setUp(self):
        print "Begin Math Testing"

    def test1_math(self):
    # Test a math expression
        target_result = gt_testout.math_test1
        actual_result = local.tester(gt_testin.math_test1)
	self.assertEqual(target_result, actual_result)

if __name__ == '__main__':
    unittest.main()
