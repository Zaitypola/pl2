import urllib2
import sys
from bs4 import BeautifulSoup


page = urllib2.urlopen('http://www.att.com/shop/wireless/plans-new.html#fbid=U-XD_DHOGEp').read()
soup = BeautifulSoup(page)

#find the container for all the plans
tabcontent = soup.find('div', {"id": "smartphonePlans", "class": "tabcontent"})
containers = tabcontent.findAll('div', {"class": "innerContainer"})

for plan in containers:
     planTitle = plan.find("div", {"class": "planTitle"})
     if planTitle:
          title = planTitle.find("a").text     
          print title          

     voiceBoxes = plan.find("div", {"class": "whiteBox"})     
     if voiceBoxes:
               box3 = voiceBoxes.findAll("div", {"class": lambda x: x and x.startswith("boxes_")})
               if box3:
                    for box in box3:
                         top = box.findAll("p")
                         minutes = u" ".join([tag.text for tag in top])
                         print "\t", minutes