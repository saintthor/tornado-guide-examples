# -*- coding: utf-8 -*-
"""
Created on 2018-06-08
@author: thor
"""

from tornado.ioloop import IOLoop
from tornado import gen, web

class ExampleHandler( web.RequestHandler ):
    @gen.coroutine
    def get( self ):
        for _ in range( 5 ):
            yield gen.sleep( 1 )
            self.write( 'zzzzzzzzzzzz<br>' )
            self.flush()
        self.finish()

application = web.Application( [
                        ( r"/example", ExampleHandler ),
                                ], autoreload = True )

application.listen( 8765 )
IOLoop.current().start()
