import requests
from bs4 import BeautifulSoup

def scrape():

    url = "https://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    print(soup.title.text)
    
    for quote in quotes:
        
        # Extract the quote text and author
        print(quote.find("span", class_="text").text)
        print(quote.find("small", class_="author").text)
        print("-" * 50)

if __name__ == '__main__':
    scrape()