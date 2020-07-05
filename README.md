# The local programming language
Written in 2012 for Professor Aho's Programming Languages and Translators final assignment by Michael Costello, Neeraja Ramanan, and Julianna Eum. 

As academic project code, it's not practical, but it does provide a comprehensive example of using PLY.

It takes the local language and translates it to Python 3, which is then intended to be executed with Python.  Besides the exercise of understanding lexing and parsing, it's novelty is the introduction of native coordinate data types.

# Installation
```shell script
python3 -m venv .
activate venv/bin/python3
pip3 install -r requirements.txt
pip3 install -r requirements-test.txt
```
# Running
To run,
```shell script
python3 local.py PROGNAME
```
where `PROGNAME` is the name of the .local program you wish to compile

If you want the output saved to a file that you can then execute with Python,
run
```shell script
python3 local.py PROGNAME > TARGNAME
```
where `TARGNAME` is the name of the target Python file

For example,
```shell script
python3 local.py hello.local > hello.py
```

You can then run hello.py with Python.
```shell script
python3 hello.py
```

local.py also supports the following options:

-d : Enables debugging of the parsing and AST walk (lex debugging must be
     enabled in the code manually)

-p : Forces the compiler to quit immediately after parsing without walking
     the AST. This is useful for testing production rules with no associated
     actions.

# Testing
To run the suite of tests
```shell script
pytest
```

# Demo
The demo is designed to be run as if one were starting from Mudd Building 
on Columbia's Morningside Campus, coordinates are (40.809343, -73.959811)
Give yourself a reasonable amount of time, such as 30-45 minutes until your
next event.  Those coffee lines are long!

# Developing
To compile a working copy of our code for testing, do the following steps:
1. Create your new file in local statements or functions (e.g., statements/assign_stmt.py).
2. Create a test script and testing input and output in tests.
3. Run pytest tests/test_assign_stmt.py.
