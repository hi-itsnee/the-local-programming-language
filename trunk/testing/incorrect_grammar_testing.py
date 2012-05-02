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



if __name__ == '__main__':
    unittest.main()
