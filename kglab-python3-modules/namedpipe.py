#!/usr/bin/env python3
#------------------------------------------------------------------------------#
#                               namedpipe.py                                   #
#------------------------------------------------------------------------------#

'''Utility for named pipes
'''




#------------------------------- Dependencies ---------------------------------#

import os
import tempfile




#---------------------------- Class definitions -------------------------------#

class NamedPipe():
    '''Context manager for a named pipe'''
    
    def __init__(self, pipe_name):
        self.name = pipe_name
        os.mkfifo(pipe_name)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        os.remove(self.name)
        return False
    
    def __repr_(self):
        return "NamedPipe('{}')".format(self.name)




#---------------------------- Function definitions ----------------------------#

def temp_named_pipe():
    with tempfile.NamedTemporaryFile() as temp:
        pipe_name = temp.name
    return NamedPipe(pipe_name)
