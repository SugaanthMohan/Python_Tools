#! /usr/bin/python3.5
"""
Process         : Execute Bash commands in a secure way by checking the output type
Author          : Suganth Mohan.
Created         : June 7 2019
Last Modified   : 




VERSION CONTROL :
_______________

subprocess : default inbuilt package (Python 3.5.2)
    NAME
        subprocess - subprocess - Subprocesses with accessible I/O streams

    MODULE REFERENCE
        https://docs.python.org/3.5/library/subprocess.html

        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.

    DESCRIPTION
        This module allows you to spawn processes, connect to their
        input/output/error pipes, and obtain their return codes.  This module
        intends to replace several older modules and functions:


"""


import subprocess


def ExecuteBashCommand(Command_):
    """
    EXECUTE BASH COMMANDS IN A FAIL-PROOF MECHANISM
    """


    Local_command = []


    print("EXECUTING SHELL COMMAND : " + Command_)


    Local_command.append(Command_)

    # GET THE PROCESS OUTPUT AND PIPE IT TO VARIABLE
    log = subprocess.Popen(Local_command,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # GET BOTH THE ERROR LOG AND OUTPUT LOG FOR IT
    stdout,stderr = log.communicate()

    # FORMAT THE OUTPUT
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')

    if stderr != "" :
        print("ERROR WHILE EXECUTING BASH COMMAND : " + Command_ + "\n\n\t" + stderr + "\n")
        exit(0)



def main():

    # VALID COMMAND
    ExecuteBashCommand("ls")

    # INVALID COMMAND
    ExecuteBashCommand("lf")




if __name__ == '__main__':
    main()
