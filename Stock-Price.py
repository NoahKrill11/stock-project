import requests
from bs4 import BeautifulSoup
def scrape(url, file) :
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')
		for heading in soup.find_all(["h1"]):
			name =(heading.text.strip())
		price = soup.find_all('div',{'class':'D(ib) Mend(20px)'})[0].find('span').text
		print(name, "$", price)
		file.write(name +" $ "+ price +'\n')
	
url = 'https://finance.yahoo.com/quote/'

inputStock = input("Enter the stock you are looking for ") 
url+= inputStock
file = open("StockOutput.txt", "a+")
scrape(url, file)

