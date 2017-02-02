"""
Looks up a host based on its name, and then adds an item to it
"""
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
        item = zapi.proxy.get(
            output="extend",
            selectInterface="extend"
        )
except ZabbixAPIException as e:
        print(e)
        sys.exit()
print("If there was no output, then there was no proxy")
