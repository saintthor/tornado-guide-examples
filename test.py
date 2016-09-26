# -*- coding: utf-8 -*-
"""
@author: thor
"""
from tornado.testing import gen_test, AsyncTestCase
from tornado.httpclient import AsyncHTTPClient
import unittest

class MyAsyncTest( AsyncTestCase ):
    @gen_test
    def test_xx( self ):
        client = AsyncHTTPClient( self.io_loop )
        path = 'http://localhost:8765/example?delay=2'
        responses = yield [client.fetch( path, method = 'GET' ) for _ in range( 10 )]
        for response in responses:
            print response.body
        
if __name__ == '__main__':
    unittest.main()
