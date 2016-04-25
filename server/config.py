__author__ = 'rcj1492'
__created__ = '2016.04'

'''
    a collection of constructors for the application and environmental variables

system_local_host
'192.168.99.100' # Docker
'ip-###-###-##-###' # AWS Image
'''

import os
import sys
import logging
from flask import Flask

class systemVariables(object):

    def __init__(self):
        self.ip = '192.168.99.100'
        if os.environ.get('SYSTEM_LOCAL_HOST'):
            ip_address = os.environ.get('SYSTEM_LOCAL_HOST')
            ip_address = ip_address.replace('ip-', '')
            ip_address = ip_address.replace('-', '.')
            self.ip = ip_address

# construct flask app object
flask_args = {
    'import_name': __name__
    # 'static_folder': 'assets',
    # 'template_folder': 'views'
}
app = Flask(**flask_args)

# establish debug reporting
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

# construct local system variables object
sysLocal = systemVariables()