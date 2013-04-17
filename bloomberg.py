from bs4 import BeautifulSoup
import urllib2,re, time
start = time.time()
# Find Bloomberg Brent Price
rawBloomData = urllib2.urlopen("http://www.bloomberg.com/energy/").read()
BloomSoup = BeautifulSoup(rawBloomData)
brent = BloomSoup.findAll('tr')[14]
BloomPrice = float(re.search(re.compile (r"\d+\.\d*"),str(brent.contents)).group())
# Find FT Brent Price
rawFTData = urllib2.urlopen("http://markets.ft.com/tearsheets/performance.asp?s=1054972").read()
FTsoup = BeautifulSoup(rawFTData)
FT = FTsoup.findAll('tr')[0]
FTPrice = float(re.search(re.compile (r"\d+\.\d*"),str(FT)).group())
# Find BBC Brent Price
rawBBCData = urllib2.urlopen("http://www.bbc.co.uk/news/business/market_data/commodities/default.stm").read()
BBCSoup = BeautifulSoup(rawBBCData)
oyell = BBCSoup.findAll('tr')[14]
BBCPrice = float(re.search(re.compile (r"\d+\.\d*"),str(oyell)).group())
# Compile for display
print " "
print " Brent Crude ($/Brl)"
print " ------------------------"
print " Bloomberg : %.2f" %(BloomPrice)
print " Financial Times : %.2f" %(FTPrice)
print " BBC : %.2f" %(BBCPrice)
print " ------------------------"
print " Average : %.2f" %((BloomPrice+FTPrice+BBCPrice)/3)
print " ------------------------"
print " "
# Write to files
OutputPath = "C:\\Test\\"
open(OutputPath+"Bloomberg.txt","wb").write("%.2f" %(BloomPrice))
open(OutputPath+"FT.txt","wb").write("%.2f" %(FTPrice))
open(OutputPath+"BBC.txt","wb").write("%.2f" %(BBCPrice))
open(OutputPath+"Average.txt","wb").write("%.2f" %((BloomPrice+FTPrice+BBCPrice)/3))
print "\n"
time.sleep(10)