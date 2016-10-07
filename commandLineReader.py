import sys
import json
import requests
#import lob 



#lob.api_key = test_916af0497de9e4d57fabfc5fab86d6fc5ff
#lob.api_version = '2016-06-30'

text = ""
stopword = ""
address_list = []
while True:
	line = raw_input()
	if line.strip() == stopword:
		break
	text += "%s\n" % line
	address_list.append(line)
print text 
print address_list

#var = raw_input("Please enter something: ")
#print "you entered", var 

addr = address_list[1] + " " + address_list[3] + ", " + address_list[4] + " " + address_list[5]
print addr 

payload = {
	"address": addr
}

r = requests.get('https://www.googleapis.com/civicinfo/v2/representatives', params = payload)

print r 
