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

  
#House Info#
# - address *
# - price *
# - beds *
# - baths *
# - fullBaths *
# - halfBaths *
# - sqft *
# - zestimate #####################
# - timeOnZillow *
# - views *
# - saves *
# - type *
# - yearBuilt *
# - heating *
# - cooling *
# - parking *
# - lot *
# - priceSqft *
# - flooring
# - appliances
# - stories
# - exterior
# - parcelNumber
# - zoning
# - roof
# - newConstruction
# - sunScore
# - region
# - hasHOAFee
# - taxAssessedValue
# - annualTaxAmount
# - MLSID
# - school
# - priceHistory
# - taxHistory
# - rentZestimate
# - propertyOwner


houses = []
y = 0
for x in houseLinks:
  print("#########################")
  #----------------------------------------------------------------------------------------------------------------
  #zillowURL = "https://www.zillow.com/homedetails/164-Kidder-Loop-Merryville-LA-70653/106012997_zpid/"
  zillowURL = x
  #----------------------------------------------------------------------------------------------------------------
  zillowSession = zillowRequest.get(zillowURL, headers=reqHeaders)
  zillowContent = zillowSession.content
  zillowSoup = soup(zillowContent, "html.parser")
  zillowSession.close()
  
  houses.append(zillowSoup)
  
  try:
    addressContainer = houses[y].findAll("h1",{"class":"ds-address-container"})[0].findAll("span")
    address = addressContainer[0].text + addressContainer[1].text
    houses[y].address = address
  except IndexError:
    houses[y].address = "unavailable"
  #
  try:
    priceContainer = houses[y].findAll("span",{"class":"ds-value"})
    price = priceContainer[0].text
    houses[y].price = price
  except IndexError:
    houses[y].price = "unavailable"
  #
  try:
    bedsContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Bedrooms")[0].parent.findAll("span")
    beds = bedsContainer[0].text
    houses[y].beds = beds
  except IndexError:
    houses[y].beds = "unavailable"
  #
  try:
    bathsContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Bathrooms")[0].parent.findAll("span")
    baths = bathsContainer[0].text
    houses[y].baths = baths
  except IndexError:
    houses[y].baths = "unavailable"
  #
  try:
    fullBathsContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Full bathrooms")[0].parent.findAll("span")
    fullBaths = fullBathsContainer[0].text
    houses[y].fullBaths = fullBaths
  except IndexError:
    houses[y].fullBaths = "unavailable"
  #
  try:
    halfBathsContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="1/2 bathrooms")[0].parent.findAll("span")
    halfBaths = halfBathsContainer[0].text
    houses[y].halfBaths = halfBaths
  except IndexError:
    houses[y].halfBaths = "unavailable"
  #
  try:
    sqftContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Total interior livable area")[0].parent.findAll("span")
    sqft = sqftContainer[0].text
    houses[y].sqft = sqft
  except IndexError:
    houses[y].sqft = "unavailable"
  #
  #try:
    #zestimateContainer = houses[y].findAll("p",{"class":"Text-sc-1vuq29o-0 sc-1w7ie4j-1 sc-111s858-8 fFiQLD"})
    #zestimate = zestimateContainer[0].text
    #houses[y].zestimate = zestimate
  #except IndexError:
    #houses[y].zestimate = "unavailable"
  #
  try:
    timeOnZillowContainer = houses[y].findAll("div",{"class":"ds-overview-stat-value"})
    timeOnZillow = timeOnZillowContainer[0].text
    houses[y].timeOnZillow = timeOnZillow
  except IndexError:
    houses[y].timeOnZillow = "unavailable"
  #
  try:
    viewsContainer = houses[y].findAll("div",{"class":"ds-overview-stat-value"})
    views = viewsContainer[1].text
    houses[y].views = views
  except IndexError:
    houses[y].views = "unavailable"
  #
  try:
    savesContainer = houses[y].findAll("div",{"class":"ds-overview-stat-value"})
    saves = savesContainer[2].text
    houses[y].saves = saves
  except IndexError:
    houses[y].saves = "unavailable"
  #
  try:
    typeContainer = houses[y].findAll("span",{"class":"ds-body ds-home-fact-value"})
    type = typeContainer[0].text
    houses[y].type = type
  except IndexError:
    houses[y].type = "unavailable"
  #
  try:
    yearBuiltContainer = houses[y].findAll("span",{"class":"ds-body ds-home-fact-value"})
    yearBuilt = yearBuiltContainer[1].text
    houses[y].yearBuilt = yearBuilt
  except IndexError:
    houses[y].yearBuilt = "unavailable"
  #
  try:
    heatingContainer = houses[y].findAll("span",{"class":"ds-body ds-home-fact-value"})
    heating = heatingContainer[2].text
    houses[y].heating = heating
  except IndexError:
    houses[y].heating = "unavailable"
  #
  try:
    coolingContainer = houses[y].findAll("span",{"class":"ds-body ds-home-fact-value"})
    cooling = coolingContainer[3].text
    houses[y].cooling = cooling
  except IndexError:
    houses[y].cooling = "unavailable"
  #
  try:
    parkingContainer = houses[y].findAll("span",{"class":"ds-body ds-home-fact-value"})
    parking = parkingContainer[4].text
    houses[y].parking = parking
  except IndexError:
    houses[y].parking = "unavailable"
  #
  try:
    lotContainer = houses[y].findAll("span",{"class":"ds-body ds-home-fact-value"})
    lot = lotContainer[5].text
    houses[y].lot = lot
  except IndexError:
    houses[y].lot = "unavailable"
  #
  try:
    priceSqftContainer = houses[y].findAll("span",{"class":"ds-body ds-home-fact-value"})
    priceSqft = priceSqftContainer[6].text
    houses[y].priceSqft = priceSqft
  except IndexError:
    houses[y].priceSqft = "unavailable"
  #
  
  
  print("Address: " + houses[y].address)
  print("Price: " + houses[y].price)
  print("Beds: " + houses[y].beds)
  print("Baths: " + houses[y].baths)
  print("Full Baths: " + houses[y].fullBaths)
  print("Half Baths: " + houses[y].halfBaths)
  print("Sqft: " + houses[y].sqft)
  #print("Zestimate: " + houses[y].zestimate)
  print("Time on Zillow: " + houses[y].timeOnZillow)
  print("Views: " + houses[y].views)
  print("Saves: " + houses[y].saves)
  print("Type: " + houses[y].type)
  print("Year Built: " + houses[y].yearBuilt)
  print("Heating: " + houses[y].heating)
  print("Cooling: " + houses[y].cooling)
  print("Parking: " + houses[y].parking)
  print("Lot: " + houses[y].lot)
  print("Price/SqFt: " + houses[y].priceSqft)
  
  print("#########################")
  y += 1
  #break
  

  
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
