#! /usr/bin/python3.5

# USED FOR THE datetime printing
import datetime

# USED IN LOGGER FOR DETAILED PRINT STATEMENT
import inspect


# >>>>>>>>>>>>>>>>>>>>>>> DEFINE THE USED SUB-ROUTINES <<<<<<<<<<<<<<<<<<<<<<<<<<<<
def Tlog(printer_):
     '''
     Can only accept one string arugment
     printer_ => - Is a single argument that is being passed to the function definition
		 - Must be of string type
     '''
     now = datetime.datetime.now()

     print("\n\t[INFO] ::"+str(now).split('.')[0]+"::"+str(__file__)+"::"+str(inspect.currentframe().f_back.f_code.co_name)+"::"+str(inspect.currentframe().f_back.f_lineno)+"::"+str(printer_)+"::\n")

def main():
	Tlog("Hellow world")


if __name__ == '__main__':
	main()
