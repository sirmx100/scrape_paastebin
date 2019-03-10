#!/usr/bin/env python
# Andrew
# https://github.com/sirmx100
##########################################

tor_enable = False
tor_proxy_ip = "127.0.0.1"
tor_proxy_port = 9151

if tor_enable:
	import socks
	import socket
	def create_connection(address, timeout=None, source_address=None):
	    sock = socks.socksocket()
	    sock.connect(address)
	    return sock

	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, tor_proxy_ip, tor_proxy_port)

	socket.socket = socks.socksocket
	socket.create_connection = create_connection

import urllib2
import os
import time

# Size of a Folder
def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_lasts_bin():
	pastebin_list = []
	start_read = False
	downloaded_data  = urllib2.urlopen('http://pastebin.com/archive/')
	print "System is stable"
	for line in downloaded_data:
		if start_read:
			tag_data = line.split('href="')
			for tag in tag_data:
				href_info = tag.split('"')[0]
				if href_info.startswith('/'):
					pastebin_list.append(href_info.split('/')[1])

			if "</ul>" in line:
				start_read = False
		if "<div id=\"menu_2\">" in line:
			start_read = True
	return pastebin_list

def get_raw_data(bin_url):
	downloaded_data = urllib2.urlopen('http://pastebin.com/raw/' + bin_url)
	print "{0} loaded successsfully".format('http://pastebin.com/raw/' + bin_url)
	return downloaded_data.read()

	
			
def main():
	lasts_bin = get_lasts_bin()
	for bins in lasts_bin:
		data = get_raw_data(bins)
		f = open('pastebin/' + bins + '.txt',"w+")
		f.write(data)

if __name__ == "__main__":
	while(1):
	    try:
	    	main()
	    	print "Waiting 4 seconds to re-query"
	    	time.sleep(4)
	    except Exception, e:
		    print e.__doc__
		    print e.message
