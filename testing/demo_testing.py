import os.path
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import local
import demo_testout


# RUN: python -m unittest demo_testing.TestCoffee.test_coffeetime
# RUN: python -m unittest demo_grammar_testing

# Comment in MacVim: 'v' --> :'<,'>s/^/#/g
# Uncomment in MacVim: 'v' --> :'<,'>s/^#//g


class TestCoffee(unittest.TestCase):
    def setUp(self):
        print("Begin Demo Testing: Time for Coffee?")

    def test_coffeetime(self):
        target_result = demo_testout.coffee_test
        actual_result = local.tester(open('coffee.local').read())
        try:
            self.assertEqual(target_result, actual_result)
        except Exception:
            print("TARGET:\n", target_result)
            print("=" * 79)
            print("ACTUAL:\n", actual_result)


if __name__ == '__main__':
    unittest.main()
