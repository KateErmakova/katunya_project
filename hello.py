#!/usr/bin/python

import datetime
import sys

print "Hello world! Current time is %s" % datetime.datetime.strftime(datetime.datetime.now(), format="%d.%m.%Y") 
print "agruments are %s" % ", ".join(sys.argv[1:])