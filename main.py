#!/usr/bin/env python

import multiprocessing as mp
import urllib2

# threaded function
def get_url(q, url):
	try:
		s = urllib2.urlopen(url).read()
		q.put(s) # different line, doesn't lock
	except (ValueError, urllib2.HTTPError) as e:
		q.put(e) # put error
	
# create que, cool for threading
q = mp.Queue()

# open file
try:
	f = open("ips.txt", "r")
except:
	print "Error: unable to open input file"

# create threads
threads = []
for line in f:
	try:
		t = mp.Process(target = get_url, args = (q, line))
		t.start()
		threads.append(t)
	except:
		print "Error: unable to start thread"


# close file
f.close()

# print urls
try:
	f = open("output.txt", "w")
except:
	print "Error: unable to open output file"

for t in threads:
	s = q.get()
	if type(s) is str:
		f.write(s)
	else:
		print "Error: %s" % s

f.close()
