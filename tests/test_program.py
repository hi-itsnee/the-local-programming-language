import unittest

import local
from . import program_test_in
from . import program_test_out


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        print("Begin Hello World Test")

    def test_hw(self):
        target_result = program_test_out.helloworld_test
        actual_result = local.tester(program_test_in.helloworld_test)
        self.assertEqual(target_result, actual_result)


class Example1(unittest.TestCase):
    def setUp(self):
        print("Begin Example 1")

    def test_example1(self):
        target_result = program_test_out.example1_test
        actual_result = local.tester(program_test_in.example1_test)
        self.assertEqual(target_result, actual_result)


class Tutorial2(unittest.TestCase):
    def setUp(self):
        print("Begin Tutorial Test #2: Variables & Arithmetic Expressions")

    def test_tutorial2(self):
        target_result = program_test_out.tutorial2_test
        actual_result = local.tester(program_test_in.tutorial2_test)
        self.assertEqual(target_result, actual_result)


class Tutorial3(unittest.TestCase):
    def setUp(self):
        print("Begin Tutorial Test #3: Loops")

    def test_tutorial3(self):
        target_result = program_test_out.tutorial3_test
        actual_result = local.tester(program_test_in.tutorial3_test)
        self.assertEqual(target_result, actual_result)


class Tutorial4(unittest.TestCase):
    def setUp(self):
        print("Begin Tutorial Test #4: Input/Output")

    def test_tutorial4(self):
        target_result = program_test_out.tutorial4_test
        actual_result = local.tester(program_test_in.tutorial4_test)
        self.assertEqual(target_result, actual_result)


class Tutorial5(unittest.TestCase):
    def setUp(self):
        print("Begin Tutorial Test #5: Functions")

    def test_tutorial5(self):
        target_result = program_test_out.tutorial5_test
        actual_result = local.tester(program_test_in.tutorial5_test)
        self.assertEqual(target_result, actual_result)


if __name__ == '__main__':
    unittest.main()
