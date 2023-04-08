# import library
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.request import Request
import re

# connect to website redfin and read html file
url_test = 'https://www.redfin.com/city/29470/IL/Chicago'
site = url_test
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site, headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page)


# extract data for feature home (number bads, number baths, area)
feature_homes = soup.findAll('div', attrs={'class':'HomeStatsV2 font-size-small'})
# extract data for prices
prices = soup.findAll('span', attrs={'class':"homecardV2Price"})
# extract data for address
address_s = soup.findAll('div',attrs={'class':'homeAddressV2'})

beds = []    
baths = []    
area_Sq = []
price_li = []
address_li = []


for i in range(len(feature_homes)):
    
    item = feature_homes[i]
    price = prices[i]
    address = address_s[i]
    
    address_s__  = address.text
    address_s_l = address_s__.split(',')[-2]
    address_li.append(address_s_l)
    
    price = price.text
    price_ =  re.sub('\$', '', str(price))
    price_ =  re.sub(',', '.', str(price_))
    price_li.append(price_)
    
    beds_item = item.findAll('div', attrs={'class':'stats'})[0].string
    baths_items = item.findAll('div', attrs={'class':'stats'})[1].string
    area_Sq_item = item.findAll('div', attrs={'class':'stats'})[2].string
    
    beds_item = re.sub(' Beds', '', beds_item)
    beds_item = re.sub(' Bed', '', beds_item)
    
    baths_items = re.sub(' Baths', '', baths_items)
    baths_items = re.sub(' Bath', '', baths_items)
    
    area_Sq_item = re.sub(' Sq. Ft.', '', str(area_Sq_item))
    area_Sq_item = re.sub(',', '.', str(area_Sq_item))

    baths.append(baths_items)
    beds.append(beds_item)
    area_Sq.append(area_Sq_item)





















