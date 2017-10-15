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

#if getting certification errors, the line below is required
zapi.session.verfy=False 
requests.packages.urllib3.disable_warnings()


# Login to the Zabbix API
#replace username and password with the appropriate data. Keep the quotes around the data.
zapi.login('username', 'password')

#prints alerts. The number 1 can be changed to denote the alert #
print zapi.alert.get("extend","1")
