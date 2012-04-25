import unittest
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import local

# RUN: python -m unittest helloworldtest

class TestHW(unittest.TestCase):
    def setUp(self):
        print "Test local for Hello World"

    def test_prgm(self):
        target_result = '''print "Hello, world!"'''
        actual_result = local.tester(open('hello.local').read().strip())
        self.assertEqual(target_result, actual_result)

if __name__ == '__main__':
    unittest.main()
