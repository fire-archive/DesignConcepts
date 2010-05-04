#!/usr/bin/python

import sys 
from urlparse import urlparse

url = sys.argv[1]
slashparts = url.split('/')
print slashparts[-2]
