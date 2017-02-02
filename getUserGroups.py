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


try:
  print zapi.usergroup.get(output="extend", status=0)
except ZabbixAPIException as e:
        print(e)
        sys.exit()
