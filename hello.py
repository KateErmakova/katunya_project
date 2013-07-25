#!/usr/bin/python

import datetime
import sys
import os

print "Hello world! Current time is %s" % datetime.datetime.strftime(datetime.datetime.now(), format="%d.%m.%Y") 
print "agruments are", ", ".join(sys.argv[1:])
for i in sys.argv:
	print "argument:", i 