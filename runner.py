'''
#TODO: Start
#TODO: Store PID in runner.pid
#TODO: Read Config File
#TODO: Check for errors
#TODO: Build a list of "run" records that specifies a time and program to run.
#TODO: Define up the function to catch the USR1 signal and print run records
#TODO: Sort run records by time
#TODO: Start Background Process
#TODO: Take the next record off the list and wait for that time, then run the program
#TODO: Add a record to the "result" list
#TODO: If this was an "every" record", add an adjusted record to the "run" list
#TODO: Repeat until no more to records on the "run" list
#TODO: Exit
'''
#!/usr/bin/env python3
# -*- coding: ascii -*-

import sys
import os
import time
import datetime
import signal

class Command:
    def __init__(self, timespec, programPath, parameters):
        self.timespec    = timespec
        self.programPath = programPath
        self.parameters  = parameters
    def __str__(self) -> str:
        return f" {self.timespec} | {self.programPath} | {self.parameters}"



runRecords = []

if __name__ == "__main__":

    #Write PID to File
    with open("runner.pid", 'w') as pidfile:
        pidfile.write(str(os.getpid()))
    
    #Read Config Files
    with open("runner.conf") as configFile:
        line = configFile.readline().strip().split()

        while len(line) > 0:
            run = line.index('run')

            if len(line[run+1:])<=1:
                params = ''
            else:
                params = ' '.join(line[run+2:])
            
            runRecords.append(
                Command(
                    timespec    = line[0:run],
                    programPath = line[run+1],
                    parameters  = params
                )
            )
            line = configFile.readline().strip().split()
        
    print(*runRecords, sep="\n")
