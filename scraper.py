import scraperwiki
import urllib
import lxml.html

def scrape_picsandname(new_root):
  histology = new_root.cssselect("div.thumb-image-box")
  for info in histology:
    imgs = info.cssselect("")

def scrape_content(linkurl):
  links = scrape_links
  for link in links:
    new_html = scraperwiki.scrape(link)
    new_root = lxml.html.fromstring(new_html)
    scrape_picsandname(new_root)

def scrape_urls(root):
  thumbimgs = root.cssselect("div.thumb-image-box")
  for thumbimg in thumbimgs:
    thumblink = thumbimg.cssselect("a")
    if thumblink:
      thumblinks = thumblink[0].attrib.get("href")
      thumburl = baseurl+thumblinks
      print thumburl
      return thumburl
      
      
  

starting_url = "http://medcell.med.yale.edu/image_gallery/home.php"
baseurl = "http://medcell.med.yale.edu/image_gallery/"

def scrape_link(url):
  html = scraperwiki.scrape(url)
  root = lxml.html.fromstring(html)
  scrape_urls(root)

scrape_link(starting_url)
scrape_content(scrape_links)
