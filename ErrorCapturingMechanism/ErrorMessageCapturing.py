#! /usr/bin/python3.5


import sys
import linecache


def main():

        prin("HELLO THERE")


# >>>>>>>>>>>>>>>>>>>>>>> MYDIE MODULE USED HERE <<<<<<<<<<<<<<<<<<<<<<<<<<<<
def mydie(exitCont_):

    print(exitCont_)

    print("*** ERROR OCCURRED *** : ROLL BACK PROCEDURES EXECUTING BELOW")

    # DEFINE DB DISCONNECT HERE

    print("*** ROLL BACK *** : CLOSING DB CONNECTION")

    # DEFINE CLOSE FTP CONNECTION HERE

    # DEFINE CLEARING THE TEMPORARY FILES HERE

    # DEFINE CREATING A PICKLE HERE

    sys.exit(0)


# >>>>>>>>>>>>>>>>>>>>>>> EXCEPTION BRIEFER USED HERE <<<<<<<<<<<<<<<<<<<<<<<<<<<<
def ExceptionBrief():

    # CREATE EXCEPTION REPORT
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION CAPTURED : ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)


def main():

    prit("hellow world")


# >>>>>>>>>>>>>>>>>>>>>>> DECLARE THE MAIN FUNCTION ERROR CATCH MECHANISM HERE  <<<<<<<<<<<<<<<<<<<<<<<<<<<<

if __name__=="__main__":

    try:
        main()
    # check the type of the exception
    # use hash attribute to print of hash type values
    # and if it is a non hash type attribute,
    # you can print the exception normally
    except KeyboardInterrupt:
        full_execption_report = ExceptionBrief()
        full_execption_report = full_execption_report+" Program Interrupted By External Source"
        mydie(full_execption_report)

    except :
        full_execption_report=ExceptionBrief()

        # DO NOTHING, USED AS DEFAULT EXIT FOR PROGRAM
        if full_execption_report != 0:
            mydie(full_execption_report)