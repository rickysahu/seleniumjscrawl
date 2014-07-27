import random
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lxml.html as lh
from lxml import etree

START_PAGE = "http://www.facebook.com/directory/people/A"
EXTRACT_PAGES = "directory\/people\/" + letter.upper()
ONLY_FOLLOW = "directory\/people\/" + letter.upper()
DOWNLOAD_DELAY = 1
PAUSE_TEXT = "Security Check Required | Facebook"







ONLY_FOLLOW_regex = re.compile(ONLY_FOLLOW).search
EXTRACT_regex = re.compile(EXTRACT_PAGES).search



urls_didcrawl = {}
urls_willcrawl = [START_PAGE]





# gets pages that match the ONLY_FOLLOW pattern
def getOnlyFollowURLs(urls):
  return [ l for l in urls for m in (ONLY_FOLLOW_regex(l),) if m]


# gets a url with the driver and allows you to clear the captcha
def getPage(url,driver):
  page_source = PAUSE_TEXT
  while PAUSE_TEXT in page_source:
    driver.get(url)
    page_source = driver.page_source
    if PAUSE_TEXT in page_source:
      breakCaptcha(driver)
      page_source = driver.page_source
    else:
      print "rate lmit / captcha overcome."
    if PAUSE_TEXT in page_source:
      print ("Clear the CAPTCHA or wait till your burn out the rate limit.")
      # continue to see if the page has changed
      while PAUSE_TEXT in page_source:
        time.sleep(2)
        page_source = driver.page_source
  return page_source


# add urls if not already crawled
def addNewURLsToCrawl(urls):
  for url in urls:
    if url not in urls_didcrawl:
      urls_willcrawl.append(url)


# navigate around captcha / rate limit
def breakCaptcha(driver):
  '''
  use this to wait for the rate lmit or input the 
  capthca and wait for raw_input() or other logic
  '''
  return


# what to do when an extracted page is found
def parsePage(url, urls, page_source, lhtml, driver):
  ''' 
  use url, urls, page_source, lhtml, and the selenium 
  driver to get the content rendered via javascript
  '''
  return




driver = webdriver.Firefox()


# crawl
while len(urls_willcrawl) > 0:
  url = urls_willcrawl.pop(0)
  try:
    page_source = getPage(url, driver)
    lhtml = lh.fromstring(page_source) #using lxml because it's faster
  except Exception, R:
    print R
    urls_didcrawl[url] = 1
    continue
    pass
  urls = list(set(lhtml.xpath("//a/@href")))
  # if this is a url that should be extracted, then parse the page for data
  if EXTRACT_regex(url) is not None:
    items = parsePage(url, urls, page_source, lhtml, driver)
  urls_didcrawl[url] = 1
  addNewURLsToCrawl(getOnlyFollowURLs(urls))
  time.sleep(DOWNLOAD_DELAY*random.random()*2)
  print 'crawled: ', len(urls_didcrawl), '/', len(urls_willcrawl) , url





































