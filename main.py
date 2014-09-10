#!/usr/bin/env python
import socket, httplib
import multiprocessing as mp
import urllib2

# threaded function
def get_url(url):
	try:
		s = str(urllib2.urlopen(url).read()) #headers
	except Exception, e: s = e # put error
	print "proc done"
	log(s, url)

def log(ret, url):
	try: outf.write(ret)
	except Exception, x: print "Error: %s: %s" % (url, x)

# open file
try: inf = open("ips.txt", "r")
except: print "Error: unable to open input file"

# open file
try: outf = open("output.txt", "w")
except: print "Error: unable to open output file"

# create procs
p = mp.Pool(100)
pool = p.map_async(get_url, inf)

inf.close() # close file

pool.get() # block until processes finish

# close file
outf.close()