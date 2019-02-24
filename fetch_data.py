from bs4 import BeautifulSoup
import urllib2
# -- coding: utf-8

### The Criminal Minds Season14 Episode Guide on TV.com


def getURL(url):
  print "Enter getURL"
  html=urllib2.urlopen(url)	
  soup=BeautifulSoup(html,'html.parser')
  print soup.get_text()," ==========================="
  return soup.get_text(). 