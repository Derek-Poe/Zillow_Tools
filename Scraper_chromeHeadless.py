from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
#chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent="+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0")
#chrome_options.add_argument("accept="+"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3")
#chrome_options.add_argument("accept-encoding="+"gzip, deflate, br")
#chrome_options.add_argument("accept-language="+"en-US,en;q=0.5")
chrome_options.add_argument("proxy-server="+"localhost:8080")
chrome_options.add_argument("remote-debugging-port="+"9222")
browser = webdriver.Chrome('d:\headless\chromedriver.exe',   options=chrome_options)


userURL = "https://www.zillow.com/beauregard-parish-la/fsbo/?searchQueryState={%22pagination%22:{},%22mapBounds%22:{%22west%22:-94.08709973828121,%22east%22:-92.63141126171871,%22south%22:29.738740300239186,%22north%22:31.539331063455272},%22usersSearchTerm%22:%22Beauregard%20Parish%20LA%22,%22regionSelection%22:[{%22regionId%22:2886,%22regionType%22:4}],%22isMapVisible%22:true,%22mapZoom%22:9,%22filterState%22:{%22isPreMarketForeclosure%22:{%22value%22:false},%22isPreMarketPreForeclosure%22:{%22value%22:false},%22isMakeMeMove%22:{%22value%22:false},%22isForSaleByAgent%22:{%22value%22:false},%22isAuction%22:{%22value%22:false},%22isNewConstruction%22:{%22value%22:false},%22isForSaleForeclosure%22:{%22value%22:false},%22isComingSoon%22:{%22value%22:false}},%22isListVisible%22:true}"
#userURL = "https://www.google.com"
zillowURL = userURL
browser.get(zillowURL)

test = browser.find_element_by_css_selector("html").get_attribute("innerHTML")
print(test)

photoTiles = browser.find_elements_by_css_selector("#grid-search-results > ul > li > article > a")
houseLinks = []
for tile in photoTiles:
  houseLinks.append(tile.get_attribute("href"))

  
browser.close()

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
# - taxAssessedValue *
# - annualTaxAmount *
# - school *
# - construction *
# - roof *
# - exterior *
# - floor *
# - walls *
# - miscellaneous *
# - style *
# - water *
# - fence *
# - priceHistory
# - taxHistory
# - rentZestimate #####################
# - propertyOwner 


houses = []
y = 0
for x in houseLinks:
  print("#########################")
  #----------------------------------------------------------------------------------------------------------------
  #zillowURL = "https://www.zillow.com/homedetails/164-Kidder-Loop-Merryville-LA-70653/106012997_zpid/"
  zillowURL = x
  #----------------------------------------------------------------------------------------------------------------
  
  browser = webdriver.Chrome('d:\headless\chromedriver.exe',   options=chrome_options)
  browser.get(zillowURL)
  
  #houses.append(zillowSoup)
  try:
    zestimate = browser.find_element_by_css_selector("#ds-home-values > div > div.ds-expandable-card-section-default-padding > div.Spacer-sc-157sur-0.djMjuF > div.Flex-sc-1qcb5a7-0.fcGJAS > div > div > p").text
  except:
    continue
	
  browser.close()
  
  print("Zestimate: " + zestimate)
  
  print("#########################")
  #y += 1
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
