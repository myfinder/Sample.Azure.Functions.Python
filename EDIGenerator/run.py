"""
    Azure Functions HTTP Example Code for Python
    
    Created by Anthony Eden
    http://MediaRealm.com.au/
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'lib')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'env/Lib/site-packages')))

import json
from AzureHTTPHelper import HTTPHelper

import base64
import hashlib
import random
import sys
import time

from Crypto.Cipher import AES
from Crypto.Util import number
import hkdf
from pprint import pprint

# This is a little class used to abstract away some basic HTTP functionality
http = HTTPHelper()

# All data to be returned to the client gets put into this dict
returnData = {
    #HTTP Status Code:
    "status": 200,
    
    #Response Body:
    "body": pprint(http),
    
    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "application/json"
    }
}

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))
