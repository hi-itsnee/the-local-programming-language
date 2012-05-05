all: basic tutorial demo

basic:
	python -m unittest grammar_testing
	
tutorial: basic
	python -m unittest program_testing

demo: basic tutorial
	python -m unittest demo_testing
