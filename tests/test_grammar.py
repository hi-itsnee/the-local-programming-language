import unittest

import local
from . import grammar_test_in
from . import grammar_test_out


class TestAssign(unittest.TestCase):
    def setUp(self):
        print("Begin Assignment Testing")

    def test_assign(self):
        target_result = grammar_test_out.assign_test
        actual_result = local.tester(grammar_test_in.assign_test)
        self.assertEqual(target_result, actual_result)


class TestCond(unittest.TestCase):
    def setUp(self):
        print("Begin Conditional Testing")

    def test_if(self):
        # Test a single 'if' statement
        target_result = grammar_test_out.if_test
        actual_result = local.tester(grammar_test_in.if_test)
        self.assertEqual(target_result, actual_result)
        # verify that this is the correct python result by looking

    def test_ifelse(self):
        # Test an if statement that includes an else
        target_result = grammar_test_out.ifelse_test
        actual_result = local.tester(grammar_test_in.ifelse_test)
        self.assertEqual(target_result, actual_result)

    def test_nesting(self):
        # Test a nested if-else within an if-else
        target_result = grammar_test_out.nesting_test
        actual_result = local.tester(grammar_test_in.nesting_test)
        self.assertEqual(target_result, actual_result)


class TestCoord(unittest.TestCase):
    def setUp(self):
        print("Begin Coordinate Testing")

    def test_coord(self):
        target_result = grammar_test_out.coord_test
        actual_result = local.tester(grammar_test_in.coord_test)
        self.assertEqual(target_result, actual_result)


class TestDefs(unittest.TestCase):
    def setUp(self):
        print("Begin Definition Testing")

    def test_def(self):
        target_result = grammar_test_out.def_test
        actual_result = local.tester(grammar_test_in.def_test)
        self.assertEqual(target_result, actual_result)


class TestExcept(unittest.TestCase):
    def setUp(self):
        print("Begin Exception Testing")

    def test_except(self):
        target_result = grammar_test_out.except_test
        actual_result = local.tester(grammar_test_in.except_test)
        self.assertEqual(target_result, actual_result)


class TestExit(unittest.TestCase):
    def setUp(self):
        print("Begin Exit Testing")

    def test_exit(self):
        target_result = grammar_test_out.exit_test
        actual_result = local.tester(grammar_test_in.exit_test)
        self.assertEqual(target_result, actual_result)


class TestExpr(unittest.TestCase):
    def setUp(self):
        print("Begin Expression Testing")

    def test_binop(self):
        # Test all the binop statements
        target_result = grammar_test_out.binop_test
        actual_result = local.tester(grammar_test_in.binop_test)
        self.assertEqual(target_result, actual_result)

    def test_indices(self):
        # Test the array statement
        target_result = grammar_test_out.indices_test
        actual_result = local.tester(grammar_test_in.indices_test)
        self.assertEqual(target_result, actual_result)

    def test_unary(self):
        # Test all the unary statements
        target_result = grammar_test_out.unary_test
        actual_result = local.tester(grammar_test_in.unary_test)
        self.assertEqual(target_result, actual_result)


class TestIO(unittest.TestCase):
    def setUp(self):
        print("Begin I/O Testing")

    def test_io(self):
        # Test a file write expression
        target_result = grammar_test_out.io_test
        actual_result = local.tester(grammar_test_in.io_test)
        self.assertEqual(target_result, actual_result)


class TestIter(unittest.TestCase):
    def setUp(self):
        print("Begin Iteration Testing")

    def test_iter(self):
        target_result = grammar_test_out.iter_test
        actual_result = local.tester(grammar_test_in.iter_test)
        self.assertEqual(target_result, actual_result)


class TestJump(unittest.TestCase):
    def setUp(self):
        print("Begin Jump Testing")

    def test_jump(self):
        target_result = grammar_test_out.jump_test
        actual_result = local.tester(grammar_test_in.jump_test)
        self.assertEqual(target_result, actual_result)


class TestList(unittest.TestCase):
    def setUp(self):
        print("Begin List Testing")

    def test_list(self):
        target_result = grammar_test_out.list_test
        actual_result = local.tester(grammar_test_in.list_test)
        self.assertEqual(target_result, actual_result)


class TestMath(unittest.TestCase):
    def setUp(self):
        print("Begin Math Testing")

    def test_math(self):
        # Test a math expression
        target_result = grammar_test_out.math_test
        actual_result = local.tester(grammar_test_in.math_test)
        self.assertEqual(target_result, actual_result)


class TestPrint(unittest.TestCase):
    def setUp(self):
        print("Begin Print Testing")

    def test_print(self):
        target_result = grammar_test_out.print_test
        actual_result = local.tester(grammar_test_in.print_test)
        self.assertEqual(target_result, actual_result)


class TestString(unittest.TestCase):
    def setUp(self):
        print("Begin String Testing")

    def test_string(self):
        target_result = grammar_test_out.string_test
        actual_result = local.tester(grammar_test_in.string_test)
        self.assertEqual(target_result, actual_result)


if __name__ == '__main__':
    unittest.main()
