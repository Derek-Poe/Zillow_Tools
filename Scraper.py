from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

reqHeaders = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

zillowRequest = requests.Session()
zillowURL = "https://www.zillow.com/beauregard-parish-la/fsbo/?searchQueryState={%22pagination%22:{},%22mapBounds%22:{%22west%22:-94.08709973828121,%22east%22:-92.63141126171871,%22south%22:29.738740300239186,%22north%22:31.539331063455272},%22usersSearchTerm%22:%22Beauregard%20Parish%20LA%22,%22regionSelection%22:[{%22regionId%22:2886,%22regionType%22:4}],%22isMapVisible%22:true,%22mapZoom%22:9,%22filterState%22:{%22isPreMarketForeclosure%22:{%22value%22:false},%22isPreMarketPreForeclosure%22:{%22value%22:false},%22isMakeMeMove%22:{%22value%22:false},%22isForSaleByAgent%22:{%22value%22:false},%22isAuction%22:{%22value%22:false},%22isNewConstruction%22:{%22value%22:false},%22isForSaleForeclosure%22:{%22value%22:false},%22isComingSoon%22:{%22value%22:false}},%22isListVisible%22:true}"
zillowSession = zillowRequest.get(zillowURL, headers=reqHeaders)
zillowContent = zillowSession.content
zillowSoup = soup(zillowContent, "html.parser")
zillowSession.close()

photoTilesContainer = zillowSoup.findAll("ul", {"class":"photo-cards"})
photoTiles = photoTilesContainer[0].findAll("article")

#Need to Account for Ad Tilesfor
houseLinks = []
for x in photoTiles:
  houseLinks.append(x.a["href"])

  
###House Info###
# 0 - Address
# 1 - Price
#


houses = [[]]
y = 0
for x in houseLinks:
  zillowURL = x
  zillowSession = zillowRequest.get(zillowURL, headers=reqHeaders)
  zillowContent = zillowSession.content
  zillowSoup = soup(zillowContent, "html.parser")
  zillowSession.close()
  
  houses.append(zillowSoup)
  
  priceContainer = houses[y].findAll("span",{"class":"ds-value"})
  price = price[0].text
  
  houses[y].append(price)
  
  y += 1
  break

  
#fileName = "products.csv"
#f = open(fileName, "w")
#headers = "brand, product_name, shipping\n"
#f.write(headers)

#containers = pageSoup.findAll("div",{"class":"item-container"})
#for container in containers:
  #brand = container.div.div.a.img["title"]
  #titleContainer = container.findAll("a", {"class":"item-title"})
  #productName = titleContainer[0].text
  #shippingContainer = container.findAll("li", {"class":"price-ship"})
  #shipping = shippingContainer[0].text.strip()
  
  #print("brand: " + brand)
  #print("productName: " + productName)
  #print("shipping: " + shipping)
  
  #f.write(brand + "," + productName.replace(",", "|") + "," + shipping + "\n")
  
#f.close()
