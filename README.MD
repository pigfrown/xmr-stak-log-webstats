Requirements:

Python3

beautiful soup
lxml
requests

Arguments:

-u/--url 	URL to parse. Including port. Required
-i/--interval	Interval between URL scrapes in seconds. Defaults to 1 second

Usage:

If there is a xmr-stak webserver on 192.168.1.100:8080 then the following command would be used:

./log-xmr-stak-webstats.py -u "192.168.1.100:8080" 

To change the default interval to 5 seconds:

./log-xmr-stak-webstats.py -u "192.168.1.100:8080" -i 5

Bugs:

Probably a lot.
