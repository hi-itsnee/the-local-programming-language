# Filename:                Makefile
# Author:                  Team 13
# Description:             Makefile for setting up environment
# Supported Language(s):   GNUMake
# Time-stamp:              <2012-05-07 12:12:14 plt>

default: clean
	mkdir /home/plt/bin
	ln -s $(PWD)/local.py /home/plt/bin/
	ln -s $(PWD)/lclc /home/plt/bin/
	ln -s $(PWD)/lcl /home/plt/bin
	chmod +x /home/plt/bin/lclc
	chmod +x /home/plt/bin/lcl
	echo "PATH=$(PATH):/home/plt/bin" >> /home/plt/.bashrc
	# Note: You probably need to run 'source /home/plt/.bashrc'

clean:
	rm -rf /home/plt/bin
