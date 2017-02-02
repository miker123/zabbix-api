#!/usr/bin/env python

import os
from pyzabbix import ZabbixAPI, ZabbixAPIException
import sys

# The hostname at which the Zabbix web interface is available
# Replace with url to interface. Keep the quotes.
ZABBIX_SERVER = 'Zabbix Web Interface URL'

zapi = ZabbixAPI(ZABBIX_SERVER)

# Login to the Zabbix API
#replace username and password with the appropriate data. Keep the quotes around the data.
zapi.login('username', 'password')

#print out all of the users. Will need some additional sorting to clean up the data.
try:
  print zapi.user.get(output="extend")
except ZabbixAPIException as e:
        print(e)
        sys.exit()

