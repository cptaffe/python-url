#!/usr/bin/env python

import threading
import urllib2
import Queue

# threaded function
def get_url(q, url):
	try:
		q.put(urllib2.urlopen(url).read())
	except (ValueError), e:
		q.put(e) # put error
	
# create que, cool for threading
q = Queue.Queue()

# open file
try:
	f = open("ips.txt", "r")
except:
	print "Error: unable to open input file"

# create threads
threads = []
for line in f:
	try:
		t = threading.Thread(target = get_url, args = (q, line))
		t.start()
		threads.append(t)
	except:
		print "Error: unable to start thread"


# close file
f.close()

# wait for threads
for t in threads:
	t.join()

# print urls
try:
	f = open("output.txt", "w")
except:
	print "Error: unable to open output file"

for t in threads:
	s = q.get()
	if type(s) is ValueError:
		print "Error: %s" % s
	else:
		f.write(s)

f.close()
