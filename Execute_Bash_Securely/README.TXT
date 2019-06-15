~ SYNOPSIS : 

	The main usage of this command is to capture background errors while running another program/script in your environment, 
	and see if it is working properly, which allows us to use this as a wrapper script (OR) you can use it to create an
	alternate case or way of handling errors, if the case occurs
	

~ PYTHON VERSION : PYTHON 3.5

~ PYTHON PACKAGES :
	
	import sys
	import subprocess

~ SCRIPT NAME :	Secure_Bash.py

~ CONSTRAINTS :

	- The main constraint on using STDERR or STANDARD ERROR OUTPUT is that some commands use stderr as a normal stdout,
	  which makes the script vulnerable while executing and it has to be kept in mind.

	  E.g. dos2unix command uses stderr to print out that the conversion was done successfully, which makes it a
	  bit more troublesome to use it there.
