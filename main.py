import urllib2
import json

from bs4 import BeautifulSoup


def get_header_json(soup):
	headers = dict()
	print "Names of all browser versions:\n"
	for name in soup.select("#liste > h4"):
		print name.text;
		headers[name.text] = []
		for header in name.next_sibling.select(" a"):
			headers[name.text].append(header.text)
	print "All Browser Info:\n"
	print json.dumps(headers)
	return headers
header_urls = {
	"IE" : "http://www.useragentstring.com/pages/Internet%20Explorer/", 
	"Firefox": "http://www.useragentstring.com/pages/Firefox/",
	"Chrome" : "http://www.useragentstring.com/pages/Chrome/",
	"Safari" : "http://www.useragentstring.com/pages/Safari/"
}

browsers = dict()

for key, value in header_urls.items():
	soup = BeautifulSoup(urllib2.urlopen(value).read())
	browsers[key] = get_header_json(soup)


with open('headers.json', 'wb') as fp:
	json.dump(browsers, fp, indent=4)


