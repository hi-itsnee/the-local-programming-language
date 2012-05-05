import unittest 
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import local
import ig_testin
import ig_testout

# RUN: python -m unittest incorrect_grammar_testing.TestCond.test_if
# RUN: python -m unittest incorrect_grammar_testing

# Comment in MacVim: 'v' --> :'<,'>s/^/#/g
# Uncomment in MacVim: 'v' --> :'<,'>s/^#//g
     

class TestAssign(unittest.TestCase):
    def setUp(self):
        print "Begin Incorrect Assignment Testing"

    def test_assign(self):
        target_result = ig_testout.assign_test
        actual_result = local.tester(ig_testin.assign_test)
	self.assertEqual(target_result, actual_result)   

class TestCond(unittest.TestCase):
    def setUp(self):
	print "Begin Incorrect Conditional Testing"

    def test_if(self):
    # Test a single 'if' statement
        target_result = ig_testout.if_test
	actual_result = local.tester(ig_testin.if_test)
	self.assertEqual(target_result, actual_result)
        # verify that this is the correct python result by looking

#    def test_ifelse(self):
#    # Test an if statement that includes an else
#        target_result = ig_testout.ifelse_test
#	actual_result = local.tester(ig_testin.ifelse_test)
#	self.assertEqual(target_result, actual_result)
#
#    def test_nesting(self):
#    # Test a nested if-else within an if-else
#        target_result = ig_testout.nesting_test
#	actual_result = local.tester(ig_testin.nesting_test)
#	self.assertEqual(target_result, actual_result)    
#
#class TestCoord(unittest.TestCase):
#    def setUp(self):
#        print "Begin Coordinate Testing"
#
#    def test_coord(self):
#        target_result = ig_testout.coord_test
#        actual_result = local.tester(ig_testin.coord_test)
#	self.assertEqual(target_result, actual_result)   
#
#class TestDefs(unittest.TestCase):
#    def setUp(self):
#        print "Begin Definition Testing"
#
#    def test_def(self):
#        target_result = ig_testout.def_test
#        actual_result = local.tester(ig_testin.def_test)
#	self.assertEqual(target_result, actual_result)   
#
#class TestExcept(unittest.TestCase):
#    def setUp(self):
#        print "Begin Exception Testing"
#
#    def test_except(self):
#        target_result = ig_testout.except_test
#        actual_result = local.tester(ig_testin.except_test)
#	self.assertEqual(target_result, actual_result)   
#
#class TestExit(unittest.TestCase):
#    def setUp(self):
#        print "Begin Exit Testing"
#
#    def test_exit(self):
#        target_result = ig_testout.exit_test
#        actual_result = local.tester(ig_testin.exit_test)
#	self.assertEqual(target_result, actual_result)   
#
#class TestExpr(unittest.TestCase):
#    def setUp(self):
#        print "Begin Expression Testing"
#    
#    def test_binop(self):
#        # Test all the binop statements
#        target_result = ig_testout.binop_test
#        actual_result = local.tester(ig_testin.binop_test)
#        self.assertEqual(target_result, actual_result)  
#    
#    def test_indices(self):
#        # Test the array statement
#        target_result = ig_testout.indices_test
#        actual_result = local.tester(ig_testin.indices_test)
#        self.assertEqual(target_result, actual_result)  
#
#    def test_unary(self):
#        # Test all the unary statements
#        target_result = ig_testout.unary_test
#        actual_result = local.tester(ig_testin.unary_test)
#        self.assertEqual(target_result, actual_result)  
#       
#class TestIO(unittest.TestCase):
#    def setUp(self):
#        print "Begin I/O Testing"
#
#    def test_io(self):
#        # Test a file write expression
#        target_result = ig_testout.io_test
#        actual_result = local.tester(ig_testin.io_test)
#	self.assertEqual(target_result, actual_result)
# 
#class TestIter(unittest.TestCase):
#    def setUp(self):
#        print "Begin Iteration Testing"
#
#    def test_iter(self):
#        target_result = ig_testout.iter_test
#        actual_result = local.tester(ig_testin.iter_test)
#	self.assertEqual(target_result, actual_result)
#
#class TestJump(unittest.TestCase):
#    def setUp(self):
#        print "Begin Jump Testing"
#
#    def test_jump(self):
#        target_result = ig_testout.jump_test
#        actual_result = local.tester(ig_testin.jump_test)
#	self.assertEqual(target_result, actual_result)
#
#class TestList(unittest.TestCase):
#    def setUp(self):
#        print "Begin List Testing"
#
#    def test_list(self):
#        target_result = ig_testout.list_test
#        actual_result = local.tester(ig_testin.list_test)
#	self.assertEqual(target_result, actual_result)
#
#class TestMath(unittest.TestCase):
#    def setUp(self):
#        print "Begin Math Testing"
#
#    def test_math(self):
#        # Test a math expression
#        target_result = ig_testout.math_test
#        actual_result = local.tester(ig_testin.math_test)
#	self.assertEqual(target_result, actual_result)
#
#class TestPrint(unittest.TestCase):
#    def setUp(self):
#        print "Begin Print Testing"
#
#    def test_print(self):
#        target_result = ig_testout.print_test
#        actual_result = local.tester(ig_testin.print_test)
#	self.assertEqual(target_result, actual_result)
#
#class TestString(unittest.TestCase):
#    def setUp(self):
#        print "Begin String Testing"
#
#    def test_string(self):
#        target_result = ig_testout.string_test
#        actual_result = local.tester(ig_testin.string_test)
#	self.assertEqual(target_result, actual_result)
#
if __name__ == '__main__':
    unittest.main()
