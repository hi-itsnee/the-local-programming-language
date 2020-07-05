import os
import sys

basepath = os.getcwd() + os.path.sep
sys.path.append(basepath + 'libs')
sys.path.append(basepath + 'functions')
sys.path.append(basepath + 'statements')
print("Hello, world!")
