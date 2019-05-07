~ SYNOPSIS :
        The Error Message Capture is more of a automation apporach/ passive monitoring approach where,
        you can trigger how you wish to handle an alert or an error while your script runs.

        - Alerts :
                - The Alerts could be emails.
                - The Alerts could be SMS.
                - The Alerts could be a call.
                - The Alerts have an endless possibility.


        - BACKGROUND PROCESSES:

                - Instead of leaving your background processes open, you can stop them.

                        Example :
                                - Closing DB Connection.
                                - Closing FTP Connection.
                                - Clearing the Cache files created by it.


        - CACHE PROCESS PROGRESS :

                - You can even cache your background processes and use them accordingly,

                        - You could pickle your processes and make them continue from where they left off, and thereby saving the run time.
                        - You could also write your log pointers incase you are reading a file and processing something.


~ PYTHON VERSION : PYTHON 3.5

~ PYTHON PACKAGES :

        import sys
        import linecache

~ SCRIPT NAME : ErrorMessageCapturing.py

~ CONSTRAINTS :

        - The program exitting must be internal and not external, like you sending kill or interrupt signal to it.
        - The Program catches only last part of the error and not the whole pythonic way from start function to where it is present pin-pointing.
        - The program requires the exception breif and mydie module along with the try and except block.
