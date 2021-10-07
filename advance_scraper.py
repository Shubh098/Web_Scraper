#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:51:42 2021

@author: shubham
"""



import pandas as pd
import numpy as np
import re



'''
link=["/hotels/fabhotel-nachiappa-ra-puram-hotel-in-chennai-3985175342096055412/",
      "/hotels/fabhotel-hiland-suites-gandhinagar-hotel-in-bengaluru-1641170124329269502/",
      "/hotels/fabhotel-grd-dlf-square-hotel-in-gurgaon-6214633264638625045/",
      "/hotels/fabhotel-kamran-palace-railway-station-hotel-in-ahmedabad-4139853241733106526/",
      "/hotels/fabhotel-capital-residency-brigade-rd-hotel-in-bengaluru-6383830869265393868/",
      " "]
'''
f = open("go1", "r")
link=[]
for j in f:
  j=j+"#"
  raw_target_link=j.split("/", 1) 
  new_target_link=raw_target_link[1].split("*",1)
  link.append(new_target_link[0])

import urllib.request

hotels = []
prices = []
ratings = []
for i in link:
  hyper="https://www.goibibo.com/"+i
  try:
   with urllib.request.urlopen(hyper) as response:
    html = response.read()
  except:
    continue
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html, 'html.parser')

#https://www.goibibo.com/hotels/hotels-in-chennai-ct/
#https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2
#<div class="HotelCardstyles__HotelNameWrapperDiv-sc-1s80tyk-11 hiiHjq">
  city_name_extract=i.split("in-",1)
  city_name=city_name_extract[1].split("-",1)
  hotels.append(" ")
  prices.append(" ")
  ratings.append(" ")
  hotels.append("**************************************************")
  prices.append(city_name[0].upper())
  ratings.append("********")
  hotels.append(" ")
  prices.append(" ")
  ratings.append(" ")
  
  for t in soup.findAll('div', attrs={'class':'HotelCardstyles__HotelCardInfoWrapperDiv-sc-1s80tyk-6 dfmysf'}):
    name=t.find('div', attrs={'class':'HotelCardstyles__HotelNameWrapperDiv-sc-1s80tyk-11 hiiHjq'})
    price=t.find('div', attrs={'class':'HotelCardstyles__CurrentPriceTextWrapper-sc-1s80tyk-26 idchau'})
    rating=t.find('div', attrs={'itemprop':'aggregateRating'})
    try:
     x=rating.text
     u=x.split("/", 1)
     ans=u[0]
    except:
     ans="N/A"
    #rating =2
    #price = re.sub("[^0-9]", "", price)
    #ReviewAndRatingsstyles_ReviewAndRatingOuterContainer-sc-lnxmeoo-2 fRbbKg
#    print(rating)
    hotels.append(name.a.text)
    prices.append(price.text)
    ratings.append(ans)

data = {'Hotel Name' : hotels, 'Price': prices, 'Rating': ratings}
df = pd.DataFrame(data)
df.to_csv('goibibo.csv', index=False,encoding='utf-8')

