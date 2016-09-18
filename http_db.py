# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 23:25:44 2016

@author: thor
"""

from tornado.ioloop import IOLoop
from tornado import gen, web
from tornado_mysql import pools

connParam = { 'host': 'localhost', 'port': 3306, 'user': 'root',
             'passwd': 'zzzzzz', 'db': 'testdb' }

class GetUserHandler( web.RequestHandler ):
    POOL = pools.Pool(
            connParam,
            max_idle_connections=1,
            max_recycle_sec=3,
                )
    @gen.coroutine
    def get( self ):
        userid = self.get_argument( 'id' )
        cursor = yield self.POOL.execute( 'select name from user where id = %s', userid )
        if cursor.rowcount > 0:
            self.write( { "status": 1, "name": cursor.fetchone()[0] } )
        else:
            self.write( { "status": 0, "name": "" } )
        self.finish()
        
application = web.Application( [
                        ( r"/getuser", GetUserHandler ),
                                ], autoreload = True )

application.listen( 8765 )
IOLoop.current().start()