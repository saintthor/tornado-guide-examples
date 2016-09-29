# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:32:52 2016

@author: thor
"""

from tornado import ioloop, gen
from time import time

@gen.coroutine
def Ring():
    print 'it\'s time to get up.'
    
if __name__ == '__main__':
    loop = ioloop.IOLoop.current()
    loop.call_at( time() + 5, Ring )
    loop.start()

