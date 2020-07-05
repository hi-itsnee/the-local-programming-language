import os
import unittest

import local
from . import demo_testout


class TestCoffee(unittest.TestCase):
    def setUp(self):
        print("Begin Demo Testing: Time for Coffee?")

    def test_coffeetime(self):
        target_result = demo_testout.coffee_test
        path = os.path.dirname(__file__)
        path = os.path.join(path, "coffee.local")
        actual_result = local.tester(open(path).read())
        try:
            self.assertEqual(target_result, actual_result)
        except Exception:  # noqa
            print("TARGET:\n", target_result)
            print("=" * 79)
            print("ACTUAL:\n", actual_result)


if __name__ == "__main__":
    unittest.main()
