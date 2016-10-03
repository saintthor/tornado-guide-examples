# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 23:25:44 2016

@author: thor
"""

from tornado.ioloop import IOLoop
from tornado import gen, web

class LoginHandler( web.RequestHandler ):
    @gen.coroutine
    def get( self ):
        self.set_secure_cookie( 'username', 'Tom' )
        self.write( 'login ok.' )
        self.finish()
        
class LogoutHandler( web.RequestHandler ):
    @gen.coroutine
    def get( self ):
        self.clear_cookie( 'username' )
        self.write( 'logout ok.' )
        self.finish()
        
class WhoHandler( web.RequestHandler ):
    def get_current_user( self ):
        return self.get_secure_cookie( 'username' ) or 'unknown'
    @gen.coroutine
    def get( self ):
        self.write( 'you are ' + self.current_user )
        self.finish()
        
        
application = web.Application( [
                        ( r"/login", LoginHandler ),
                        ( r"/logout", LogoutHandler ),
                        ( r"/whoami", WhoHandler ),
                                ],
                            autoreload = True,
                            cookie_secret="feljjfesrh48thfe2qrf3np2zl90bmw",
                                )

application.listen( 8765 )
IOLoop.current().start()