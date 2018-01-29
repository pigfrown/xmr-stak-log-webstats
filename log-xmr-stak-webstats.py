#!/usr/bin/python3
#dirty hack to log XMR_STAK web stats in an attemp to discover which card is crashing

import requests
from bs4 import BeautifulSoup

def get_page(url):
	#TODO exception handling
	req = requests.get("http://{}".format(url))
	return req.text

def parse_page(html):
	#The page contains a table
	#The table has 3 coloums.. current hashrate, 60sec hashrate, 15minute hashrate
	#We only care about current hashrate, column 1
	#So get a list of all current hashrates (for all threads) and return it
	soup = BeautifulSoup(html, "lxml")
	table = soup.find("table")
	hashrates = []
	for row in table.find_all("tr"):
		#Just look for the first cell in this row (current hashrate)
		hashrates.append(row.find("td"))
	
	#The last 2 rows are totals. We don't care about them
	#The first row appears to be NONE.. we don't care about that either
	return hashrates[1:-2]

def print_as_table(data, maxnamelength=5):
	"""
	Stolen from a stackoverflow post by Israel Unterman
	Pretty prints data as a table.
	data should be a list of lists, where each sub list is a table row
	maxnamelength should be adjusted correctly (TODO: auto find best value)
	"""
	for i, d in enumerate(data):
		line = "|".join(str(x).ljust(maxnamelength) for x in d)
		print(line)
		if i == 0:
			print('-' * len(line))



def print_thread_hashrates(hashrate_data):
	#Get the number of threads
	#The data we will send to "print_as_table"
	#Each sublist is a row in the outputted table
	table_data = []
	table_data.append([ hashrate.get_text() for hashrate in hashrate_data ])
	print_as_table(table_data)

	
def main(url, interval):
	from time import sleep
	import sys
	while True:
		print_thread_hashrates(parse_page(get_page(url)))
		sys.stdout.flush()
		sleep(interval)
	
if __name__ == "__main__": 
	import argparse
	import sys
	DEFAULT_INTERVAL=1
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--url", help="Url to scrape")
	parser.add_argument("-i", "--interval",  help="Time (in seconds) between each query")
#	parser.add_argument("-l", "--log-file", help="Log file name")

	args = parser.parse_args()

	if not args.url:
		print("Need to pass the --url (-u) option AT LEAST")
		sys.exit(1)
	else:
		url = args.url

	if not args.interval:
		interval = DEFAULT_INTERVAL
	else:
		interval = args.interval

	main(url, int(interval))

	

	

	
