__author__ = 'rcj1492'
__created__ = '2015.10'

from server.launch import *

# unit tests
with app.test_request_context('/login/', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello/'
    assert request.method == 'POST'