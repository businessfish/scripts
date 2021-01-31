###
### author:     noah michaels nxm4189@rit.edu
### class:      csec 471 penetration testing
### assignment: homework 2 - email scraper
### date:       10/7/2019
### version:    1
###

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError
import re
import sys

# get url from command line
try:
    url = str(sys.argv[1])
except IndexError:
    print("usage: " + str(sys.argv[0]) + "<url> [number of addresses]")
    exit()
# number of emails we want to get
num_emails = 3
# if the number isnt provided, set default to 3
try:
    num_emails = int(sys.argv[2])
except IndexError:
    print("number of emails to harvest not specified - setting to default (3)")
# parse url for the domain we will be crawling
domain = urlparse(url).netloc

emails = []
# our links to visit, and the ones we have already visited
links = []
links_visited = []

###
### scrape_page:
###     scrape a given webpage for a tags containing links to the same domain
###     and store them along with any email addresses on the page
###
### param   url     url to connect to and scrape
###
### return  none
def scrape_page(url):
    # read page content and create a bs4 object for it
    try:
        conn = urlopen(url)
    except HTTPError:
        print("http error received, unable to access page.")
        return

    page = conn.read()
    conn.close()
    page_soup = soup(page, "lxml")

    # grab any email addresses on the page and save em
    email_search = re.compile("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    email_search = email_search.findall(str(page))
    # if we dont have the # of emails we want, keep getting them
    for email in email_search:
        if email not in emails and len(emails) < num_emails:
            # make sure we dont get those @2.png's
            if ".png" not in email and ".jpg" not in email:
                emails.append(email)
                #print(email)

    # find all links to other pages on this site
    for a in page_soup.findAll('a', attrs={'href': re.compile("^http?s://")}):
        link = a.get('href')
        # make sure we dont leave the domain
        if urlparse(link).netloc == domain:
            # if we haven't visited the link or already noted it, note it
            if link not in links and link not in links_visited:
                links.append(link)
                #print(link)
    return


scrape_page(url)
# make sure we get every link
while len(links) > 0:
    if len(emails) >= num_emails:
        break
    # scrape the links from the last page(s) we scraped
    for link in links:
        if len(emails) >= num_emails:
            break
        # visit the link
        links_visited.append(link)
        # remove it from links to visit
        links.remove(link)
        # scrape it
        scrape_page(link)
        #print(emails)
        #print(len(links))

# write our results to emails.txt - 1 addr per line
f = open("emails.txt", "w")
for email in emails:
    f.write(email + "\r\n")
f.close()