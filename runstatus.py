"""
#TODO: Start
#TODO: Read PID from runner.pid
#TODO: Give an error message if file not found or bad pid
#TODO: Send USR1 Signal to runner.py (Through PID)
#TODO: Read runner.status
#TODO: Give output
#TODO: Open runner.status
#TODO: If Errors Retry for 5 seconds. 
#TODO: Truncate the File to zero length
#TODO: Close File
#TODO: Stop
"""
#!/usr/bin/env python3
# -*- coding: ascii -*-

import sys
import os

pidfile = ".runner-pid"
statusfilename = ".runner.status"
