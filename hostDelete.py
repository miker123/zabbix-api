#!/usr/bin/env python

"""
Looks up a host based on its name, and then adds an item to it
"""

from pyzabbix import ZabbixAPI, ZabbixAPIException
import sys
import os

# The hostname at which the Zabbix web interface is available
# Replace with url to interface. Keep the quotes.
ZABBIX_SERVER = 'Zabbix Web Interface URL'

zapi = ZabbixAPI(ZABBIX_SERVER)

# Login to the Zabbix API
#replace username and password with the appropriate data. Keep the quotes around the data.
zapi.login('username', 'password')


command="./zhostfinder.py -e -A"
os.system(command)

hostID=raw_input("What host ID will we be using:")

#Delete the host from the console
hosts = zapi.host.delete((hostID))
