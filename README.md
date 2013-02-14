scrapeBrowserheader
===================

Scrape Browser Header information for major browsers and store then in JSON file.

Uses http://www.useragentstring.com for getting user agent information for various browsers.

Output is stored in `headers.json` file

Usage
-----

- Clone the project into your directory
- Install beautifulSoup4 library using `easy_install beautifulsoup4`
- In `main.py` edit the `header_url` by editing the list with the Key and URL for the browsers whose user agents you want to scrape. Get links from: [http://www.useragentstring.com]
- Run the file `python main.py`
- Get your information in `headers.json`

