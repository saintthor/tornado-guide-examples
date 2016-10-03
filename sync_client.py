# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:32:02 2016

@author: thor
"""

import socket
from time import time

sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
sock.connect(( 'localhost', 8760 ))

t0 = time()

for _ in range( 1000 ):
    sock.send( 'test message.' )
    sock.recv( 99 )
    
print 'time cost', time() - t0

sock.close()
    
