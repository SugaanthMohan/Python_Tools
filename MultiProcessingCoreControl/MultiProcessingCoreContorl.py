#! /usr/bin/python3.5

# USED FOR MULTIPROCESSING
import multiprocessing

#USED FOR SLEEP PROCESS
from time import sleep

# USE PERCENTAGE IN THE LITERAL SENSE AS SUCH ,
# 60% => 60/100 => 0.6
global TotalCoresUsage

TotalCoresUsage = 70/100 # A.K.A 70%


def main():


    # LIMIT THE TOTAL CPU USAGE BASED ON THE TOTAL CORES AVAILABLE AND THEN ALLOCATING THOSE CORES FOR THAT PROCESS
    # I HAVE SET THE LIMIT TO TOTAL CPU USAGE : 70 PERCENTAGE (NOTE : NOT EACH CORE) OF THE CPU SO THAT THE PROCESS DOES NOT GET AFFECTED

    TotalProcessCount = round( multiprocessing.cpu_count() * TotalCoresUsage )

    print("Total Cores Used : ",TotalProcessCount," Out of Total Cores : ",multiprocessing.cpu_count())



    # CREATE THE LIST FOR THE ARGUMENTS PARSING
    CombinedParser = []

    # PARSE EACH ARGUMENT ONE AFTER THE OTHER
    for Processing in ['1','2','3','4','5']:

        # SINCE ONLY SINGLE ARGUMENT CAN BE PARSED FOR MULTI-PROCESSING, IT IS PARSED AS A DICTIONARY
        DataParserArgs  =       {
                                'inputFile'         : 'Process_Input.txt',
                                'OutputFile'        : 'Process_Output.txt',
                                'Wait_Time_Loops'   : 9,
                                'Process'           : Processing
                                }

        CombinedParser.append(DataParserArgs)

    # INITIATE EACH PROCESS COUNT
    with multiprocessing.Pool(TotalProcessCount) as process:

        # GIVE THE FIRST ARGUMENT OF FUNCTION NAME AND SECOND ARGUMENT AS LIST OF INPUTS
        process.map(TimeLoop,CombinedParser)



def TimeLoop(ArgsDict_):
    InputFile_      = ArgsDict_['inputFile']
    OutputFile_     = ArgsDict_['OutputFile']
    Waiting_Time_   = ArgsDict_['Wait_Time_Loops']
    ProcessNo_      = ArgsDict_['Process']

    for timer in range(1,Waiting_Time_):
        sleep(1)
        print("Input File : "+str(InputFile_)+" Output File : "+str(OutputFile_)+" Process No. : "+str(ProcessNo_)+" Waiting for 1 sec @"+str(timer))


if __name__ == '__main__':
    main()
