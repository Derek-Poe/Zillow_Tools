from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

reqHeaders = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

zillowRequest = requests.Session()
zillowURL = "https://www.zillow.com/beauregard-parish-la/fsbo/?searchQueryState={%22pagination%22:{},%22mapBounds%22:{%22west%22:-94.08709973828121,%22east%22:-92.63141126171871,%22south%22:29.738740300239186,%22north%22:31.539331063455272},%22usersSearchTerm%22:%22Beauregard%20Parish%20LA%22,%22regionSelection%22:[{%22regionId%22:2886,%22regionType%22:4}],%22isMapVisible%22:true,%22mapZoom%22:9,%22filterState%22:{%22isPreMarketForeclosure%22:{%22value%22:false},%22isPreMarketPreForeclosure%22:{%22value%22:false},%22isMakeMeMove%22:{%22value%22:false},%22isForSaleByAgent%22:{%22value%22:false},%22isAuction%22:{%22value%22:false},%22isNewConstruction%22:{%22value%22:false},%22isForSaleForeclosure%22:{%22value%22:false},%22isComingSoon%22:{%22value%22:false}},%22isListVisible%22:true}"
#zillowURL = "https://www.zillow.com/homes/for_sale/?searchQueryState={%22pagination%22:{},%22mapBounds%22:{%22west%22:-93.65082257371114,%22east%22:-92.95181744675801,%22south%22:30.652397782528343,%22north%22:31.07617909906113},%22isMapVisible%22:true,%22filterState%22:{%22sortSelection%22:{%22value%22:%22days%22},%22isForRent%22:{%22value%22:true}},%22isListVisible%22:true,%22mapZoom%22:11}"
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
# - flooring *
# - appliances *
# - parkingFeatures *
# - hasGarage *
# - stories *
# - exteriorFeatures *
# - parcelNumber *
# - newConstruction *
# - sewerInformation *
# - sunscore ########
# - region *
# - hasHOAFee *
# - taxAssessedValue
# - annualTaxAmount
# - school
# - construction
# - roof
# - exterior
# - floor
# - walls
# - miscellaneous
# - style
# - water
# - fence
# - priceHistory
# - taxHistory
# - rentZestimate
# - propertyOwner


houses = []
y = 0
for x in houseLinks:
  print("#########################")
  #----------------------------------------------------------------------------------------------------------------
  zillowURL = "https://www.zillow.com/homedetails/164-Kidder-Loop-Merryville-LA-70653/106012997_zpid/"
  #zillowURL = x
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
  try:
    flooringContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Flooring")[0].parent.findAll("span")
    flooring = flooringContainer[0].text
    houses[y].flooring = flooring
  except IndexError:
    houses[y].flooring = "unavailable"
  #
  try:
    appliancesContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Appliances included in sale")[0].parent.findAll("span")
    appliances = appliancesContainer[0].text
    houses[y].appliances = appliances
  except IndexError:
    houses[y].appliances = "unavailable"
  #
  try:
    parkingFeaturesContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Parking features")[0].parent.findAll("div")
    parkingFeatures = parkingFeaturesContainer[0].text
    houses[y].parkingFeatures = parkingFeatures
  except IndexError:
    houses[y].parkingFeatures = "unavailable"
  #
  try:
    hasGarageContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Has garage")[0].parent.findAll("span")
    hasGarage = hasGarageContainer[0].text
    houses[y].hasGarage = hasGarage
  except IndexError:
    houses[y].hasGarage = "unavailable"
  #
  try:
    storiesContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Stories")[0].parent.findAll("span")
    stories = storiesContainer[0].text
    houses[y].stories = stories
  except IndexError:
    houses[y].stories = "unavailable"
  #
  try:
    exteriorFeaturesContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Exterior features")[0].parent.findAll("div")
    exteriorFeatures = exteriorFeaturesContainer[0].text
    houses[y].exteriorFeatures = exteriorFeatures
  except IndexError:
    houses[y].exteriorFeatures = "unavailable"
  #
  try:
    parcelNumberContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Parcel number")[0].parent.findAll("span")
    parcelNumber = parcelNumberContainer[0].text
    houses[y].parcelNumber = parcelNumber
  except IndexError:
    houses[y].parcelNumber = "unavailable"
  #
  try:
    newConstructionContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="New construction")[0].parent.findAll("span")
    newConstruction = newConstructionContainer[0].text
    houses[y].newConstruction = newConstruction
  except IndexError:
    houses[y].newConstruction = "unavailable"
  #
  try:
    sewerInformationContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Sewer information")[0].parent.findAll("span")
    sewerInformation = sewerInformationContainer[0].text
    houses[y].sewerInformation = sewerInformation
  except IndexError:
    houses[y].sewerInformation = "unavailable"
  #
  #try:
    #sunscoreContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Sunscore")[0].parent.findAll("div")
    #sunscore = sunscoreContainer[0].text
    #houses[y].sunscore = sunscore
  #except IndexError:
    #houses[y].sunscore = "unavailable"
  #
  try:
    regionContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Region")[0].parent.findAll("span")
    region = regionContainer[0].text
    houses[y].region = region
  except IndexError:
    houses[y].region = "unavailable"
  #
  try:
    hasHOAFeeContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Has HOA fee")[0].parent.findAll("span")
    hasHOAFee = hasHOAFeeContainer[0].text
    houses[y].hasHOAFee = hasHOAFee
  except IndexError:
    houses[y].hasHOAFee = "unavailable"
  #
  try:
    taxAssessedValueContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Tax assessed value")[0].parent.findAll("span")
    taxAssessedValue = taxAssessedValueContainer[0].text
    houses[y].taxAssessedValue = taxAssessedValue
  except IndexError:
    houses[y].taxAssessedValue = "unavailable"
  #
  try:
    annualTaxAmountContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Annual tax amount")[0].parent.findAll("span")
    annualTaxAmount = annualTaxAmountContainer[0].text
    houses[y].annualTaxAmount = annualTaxAmount
  except IndexError:
    houses[y].annualTaxAmount = "unavailable"
  #
  try:
    schoolContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="School")[0].parent.findAll("span")
    school = schoolContainer[0].text
    houses[y].school = school
  except IndexError:
    houses[y].school = "unavailable"
  #
  try:
    constructionContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Construction")[0].parent.findAll("span")
    construction = constructionContainer[0].text
    houses[y].construction = construction
  except IndexError:
    houses[y].construction = "unavailable"
  #
  try:
    roofContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Roof")[0].parent.findAll("span")
    roof = roofContainer[0].text
    houses[y].roof = roof
  except IndexError:
    houses[y].roof = "unavailable"
  #
  try:
    exteriorContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Exterior")[0].parent.findAll("span")
    exterior = exteriorContainer[0].text
    houses[y].exterior = exterior
  except IndexError:
    houses[y].exterior = "unavailable"
  #
  try:
    floorContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Floor")[0].parent.findAll("span")
    floor = floorContainer[0].text
    houses[y].floor = floor
  except IndexError:
    houses[y].floor = "unavailable"
  #
  try:
    wallsContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Walls")[0].parent.findAll("span")
    walls = wallsContainer[0].text
    houses[y].walls = walls
  except IndexError:
    houses[y].walls = "unavailable"
  #
  try:
    miscellaneousContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Miscellaneous")[0].parent.findAll("span")
    miscellaneous = miscellaneousContainer[0].text
    houses[y].miscellaneous = miscellaneous
  except IndexError:
    houses[y].miscellaneous = "unavailable"
  #
  try:
    styleContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Style")[0].parent.findAll("span")
    style = styleContainer[0].text
    houses[y].style = style
  except IndexError:
    houses[y].style = "unavailable"
  #
  try:
    waterContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Water")[0].parent.findAll("span")
    water = waterContainer[0].text
    houses[y].water = water
  except IndexError:
    houses[y].water = "unavailable"
  #
  try:
    fenceContainer = houses[y].findAll("div",{"class":"ds-home-facts-and-features reso-facts-features"})[0].findAll("td",string="Miscellaneous: Fence (Cyc/Wd)")[0].parent.findAll("span")
    fence = fenceContainer[0].text
    houses[y].fence = fence
  except IndexError:
    houses[y].fence = "unavailable"
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
  print("Flooring: " + houses[y].flooring)
  print("Appliances: " + houses[y].appliances)
  print("Parking Features: " + houses[y].parkingFeatures)
  print("Has Garage: " + houses[y].hasGarage)
  print("Stories: " + houses[y].stories)
  print("Exterior Features: " + houses[y].exteriorFeatures)
  print("Parcel Number: " + houses[y].parcelNumber)
  print("New Construction: " + houses[y].newConstruction)
  print("Sewer Information: " + houses[y].sewerInformation)
  #print("Sunscore: " + houses[y].sunscore)
  print("Region: " + houses[y].region)
  print("Has HOA Fee: " + houses[y].hasHOAFee)
  print("Tax Assessed Value: " + houses[y].taxAssessedValue)
  print("Annual Tax Amount: " + houses[y].annualTaxAmount)
  print("School: " + houses[y].school)
  print("Construction: " + houses[y].construction)
  print("Roof: " + houses[y].roof)
  print("Exterior: " + houses[y].exterior)
  print("Floor: " + houses[y].floor)
  print("Walls: " + houses[y].walls)
  print("Miscellaneous: " + houses[y].miscellaneous)
  print("Style: " + houses[y].style)
  print("Water: " + houses[y].water)
  print("Fence: " + houses[y].fence)
  
  print("#########################")
  #y += 1
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
