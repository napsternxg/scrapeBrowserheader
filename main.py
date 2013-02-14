import urllib2
import json
import re

from bs4 import BeautifulSoup
from collections import OrderedDict

def get_header_json(soup):
	headers = OrderedDict()
	print "Names of all browser versions:\n"
	for name in soup.select("#liste > h4"):
		print name.text;
		regex = re.compile("[\d+\.]+[\w\d]+")
		match_str = regex.search(name.text)	
		if match_str is None:
			header_version = "0.0"
		else:
			header_version = match_str.group(0)

		headers[header_version] = []
		user_agents = []
		for header in name.next_sibling.select("li > a"):
			user_agents.append(header.text)
		headers[header_version] = user_agents
	print "All Browser Info:\n"
	print json.dumps(headers)
	return headers

header_urls = {
	"IE" : "http://www.useragentstring.com/pages/Internet%20Explorer/", 
	"Firefox": "http://www.useragentstring.com/pages/Firefox/",
	"Chrome" : "http://www.useragentstring.com/pages/Chrome/",
	"Safari" : "http://www.useragentstring.com/pages/Safari/"
}

browsers = OrderedDict()

for key, value in header_urls.items():
	soup = BeautifulSoup(urllib2.urlopen(value).read())
	browsers[key] = get_header_json(soup)


with open('headers.json', 'wb') as fp:
	print "Generating header.json for browsers: ", browsers.keys()
	json.dump(browsers, fp, indent=4, sort_keys=False)


