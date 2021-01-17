from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def EBCheck():
	print("EB GAMES STOCK:")
	
	for type in range(2):

		if type == 0:
			url = 'https://www.ebgames.ca/SearchResult/QuickSearchHeaderPlatform?platform=453&rootGenre=74'
		else:
			url = 'https://www.ebgames.ca/SearchResult/QuickSearch?platform=453&productType=3'
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()

		page_soup = soup(page_html, "html.parser")

		products = page_soup.findAll("div",{"class":"singleProduct"})

		for product in products:
			prod_name = product.div.a.text.strip()
			available = "Out of Stock"
			try:
				if product.find("div","prodBuy").p.a["class"][2] == "cartAddNoRadio":
					available = "In Stock"

			except AttributeError:
				None

			print("Name: " + prod_name)
			print("Availability: " + available + "\n")

			f.write(prod_name + "," + available + "\n")

def ShoppersCheck():
	print("SHOPPERS DRUG MART STOCK:")

	url = 'https://www1.shoppersdrugmart.ca/en/food-and-home/playstation5'

	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()

	page_soup = soup(page_html, "html.parser")

	product = page_soup.findAll("div",{"class":"layout-wrapper module-console-preorder-banner__heading"})

	if product[0].text == 'Out of stock':
		print("Availability: Out of Stock")
		available = "Out of Stock"
	else:
		print("Page Change - Please Check Webiste")
		available = "Check Site"

	f.write("PS5" + "," + available + "\n")


filename = "PS5_Products.csv"
f = open(filename, "w")
headers = "Product, Availability\n"
f.write(headers)

EBCheck()
print("\n\n\n\n")
ShoppersCheck()

f.close()