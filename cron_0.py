# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:32:52 2016

@author: thor
"""

from tornado import ioloop, gen

@gen.coroutine
def Count():
    print '1 second has gone.'
    
if __name__ == '__main__':
    ioloop.PeriodicCallback( Count, 1000 ).start()
    ioloop.IOLoop.current().start()

