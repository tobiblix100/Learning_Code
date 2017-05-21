import scraperwiki
import urllib
import lxml.html

def scrape_links(root):
  thumbimgs = root.cssselect("div.thumb-image-box")
  for thumbimg in thumbimgs:
    thumblink = thumbimg.cssselect("a")
    if thumblink:
      thumblinks = thumblink[0].attrib.get("href")
      thumburl = baseurl+thumblinks
      print thumburl
      
      
  

starting_url = "http://medcell.med.yale.edu/image_gallery/home.php"
baseurl = "http://medcell.med.yale.edu/image_gallery/"

def scrape_and_look_for_next_link(url):
  html = scraperwiki.scrape(url)
  root = lxml.html.fromstring(html)
  scrape_links(root)

scrape_and_look_for_next_link(starting_url)
