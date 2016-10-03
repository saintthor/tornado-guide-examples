# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:32:02 2016

@author: thor
"""

import socket
from time import time
from tornado import ioloop

loop = ioloop.IOLoop.current()

socks = [socket.socket( socket.AF_INET, socket.SOCK_STREAM ) for _ in range( 50 )]
[sock.connect(( 'localhost', 8760 )) for sock in socks]

SockD = { sock.fileno(): sock for sock in socks }

t0 = time()
n = 0

def OnEvent( fd, event ):
    if event == loop.READ:
        sock = SockD[fd]
        sock.recv( 99 )
        global n
        n += 1
        if n >= 1000:
            print 'time cost', time() - t0
            sock.close()
            loop.remove_handler( fd )
            loop.stop()
            return
        sock.send( 'test message.' )

for fd, sock in SockD.items():
    loop.add_handler( fd, OnEvent, loop.READ )
    sock.send( 'test message.' )
    
loop.start()
