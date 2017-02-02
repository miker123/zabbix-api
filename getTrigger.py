#!/usr/bin/env python

import os

#display hosts
command="./zhostfinder.py -A"
os.system(command)

#find a host
desire=raw_input("Please enter the name of the host to get the trigger for:")

#display the active triggers for the ubuntu client
print "Active triggers for host" + desire
c2r="./zhtrigfinder.py -A " + desire

os.system(c2r)
