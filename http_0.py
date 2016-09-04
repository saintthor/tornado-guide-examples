# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 23:25:44 2016

@author: thor
"""

from tornado.ioloop import IOLoop
from tornado import gen, web


class ExampleHandler( web.RequestHandler ):
    @gen.coroutine
    def get( self ):
        delay = self.get_argument( 'delay', 5 )
        yield gen.sleep( int( delay ))
        self.write( { "status": 1, "msg": "success" } )
        self.finish()
        
#    @gen.coroutine
#    def post( self ):
#        pass
        
application = web.Application( [
                        ( r"/example", ExampleHandler ),
                        #( r"/other", OtherHandler ),
                                ], autoreload = True )

application.listen( 8765 )
IOLoop.current().start()