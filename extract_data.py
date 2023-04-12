# import library
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.request import Request
import re
from database_connect import insert_data



for page_number in range(1,10):

    # connect to website redfin and read html file
    url_test = f'https://www.redfin.com/city/29470/IL/Chicago/page-{page_number}'
    # url_test = f'https://www.redfin.com/city/29470/IL/Chicago/page-'

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
        
        
    for count in range(len(feature_homes)):
            
        item = feature_homes[count]
        price = prices[count]
        address = address_s[count]
        
        # extract city or region in address text
        address_s__  = address.text
        address_s_l = address_s__.split(',')[-2]
        
        # convert price string format to similar int
        price = price.text
        price_ =  re.sub('\$', '', str(price))
        price_ =  re.sub(',', '.', str(price_))
        
        # extract number bads, number baths, area from feature_homes 
        beds_item = item.findAll('div', attrs={'class':'stats'})[0].string
        baths_items = item.findAll('div', attrs={'class':'stats'})[1].string
        area_Sq_item = item.findAll('div', attrs={'class':'stats'})[2].string
        
        # convert price string format to similar int
        beds_item = re.sub(' Beds', '', str(beds_item))
        beds_item = re.sub(' Bed', '', beds_item)
        
        # convert price string format to similar int
        baths_items = re.sub(' Baths', '', str(baths_items))
        baths_items = re.sub(' Bath', '', baths_items)
        
        # convert price string format to similar int
        area_Sq_item = re.sub(' Sq. Ft.', '', str(area_Sq_item))
        area_Sq_item = re.sub(',', '.', str(area_Sq_item))

        # insert_data(area=area_Sq_item, number_bedrooms=beds_item, number_bath=baths_items, property_address=address_s_l, price=price_)


