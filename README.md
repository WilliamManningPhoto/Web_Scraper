# Libraries installation
The **requests** library is a Python tool used to send HTTP requests to websites and retrieve their responses,
such as HTML content or data. It allows your code to act like a browser, making it easy to download and interact with web pages or APIs.
To install this library type **pip install requests** into the VSCode terminal.

**BeautifulSoup4** is a Python library used to parse and navigate HTML or XML content, making it easy to search for and extract specific elements from a webpage.
It turns raw HTML into a structured tree so you can access data. To install the library type **pip install beautifulsoup4** into the VSCode terminal.

# Practical use
The test website used is https://quotes.toscrape.com/, a mock site created for practicing web scraping.
It contains structured data such as quotes, authors, and tags, making it ideal for learning how to extract information from HTML.
Shown below is my example of running a web scraper to collect quotes from the example website:
```python
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
```
