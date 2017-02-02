#!/usr/bin/env python

import os
from twilio.rest import TwilioRestClient

accountSID = 'AC# Here'
authToken = 'Auth Toekn'
myNumber = '+1 My Number'
twilioNumber = '+1 Twilio Number'

#Goal of program is to figure out when a new item has been added into the system and then send a text when that occurs.

#get all of the hosts in the environment
os.system('./zgetinventory.py --all-hosts -A > newhosts2.txt')
#write command to file.

with open('allhosts.txt') as f:
	file1=len(f.readlines())
with open('newhosts2.txt') as f2:
	file2=len(f2.readlines())
	print file2

#if 2 files are equal and there are no new hosts added.
if file1 == file2:
	os.system("rm newhosts2.txt")

#if there are new entries in the file
if file1 < file2:
	message='There is a new Zabbix agent in the environment'
	twilioCli = TwilioRestClient(accountSID, authToken)
	twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
	#send test

	#renaming and moving files!
	os.system("rm allhosts.txt")
	os.system("mv newhosts2.txt allhosts.txt")
	os.system("rm newhosts2.txt")
