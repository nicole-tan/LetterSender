import sys
#import lob 

#lob.api_key = test_916af0497de9e4d57fabfc5fab86d6fc5ff
#lob.api_version = '2016-06-30'

text = ""
stopword = ""
while True:
	line = raw_input()
	if line.strip() == stopword:
		break
	text += "%s\n" % line
print text 

#var = raw_input("Please enter something: ")
#print "you entered", var 


