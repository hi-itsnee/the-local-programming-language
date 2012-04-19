import unittest
from plugh import *

# RUN: python -m unittest plugh-test.PlughUT.test_joy
# RUN: python -m unittest plugh-test

class PlughUT(unittest.TestCase):
    def setUp(self):
	print "Get ready"

    def test_happy(self):
	target_result = open('happy.test').read().strip()
	actual_result = happy()
	self.assertEqual(target_result, actual_result)

    def test_joy(self):
	target_result = open('joy.test').read().strip()
	actual_result = joy()
	self.assertEqual(target_result, actual_result)

class PlughBadUT(unittest.TestCase):
    def setUp(self):
	print "2nd class"

if __name__ == "__main__":
    unittest.main()
