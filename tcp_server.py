# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:32:52 2016

@author: thor
"""

from tornado import ioloop, gen, iostream
from tornado.tcpserver import TCPServer

class MyTcpServer( TCPServer ):
    @gen.coroutine
    def handle_stream( self, stream, address ):
        try:
            while True:
                msg = yield stream.read_bytes( 20, partial = True )
                print msg, 'from', address
                yield gen.sleep( 0.005 )
                yield stream.write( msg[::-1] )
                if msg == 'over':
                    stream.close()
        except iostream.StreamClosedError:
            pass

if __name__ == '__main__':
    server = MyTcpServer()
    server.listen( 8760 )
    server.start()
    ioloop.IOLoop.current().start()

