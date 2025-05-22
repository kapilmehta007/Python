import requests
from bs4 import BeautifulSoup
import yfinance as yf
from tabulate import tabulate
from typing import List, Dict


data=[]

def getTicker(stockName: str) -> List[Dict[str, str | int]]:
    
    """
    Fetches the ticker symbol for a given stock name using Yahoo Finance.
    """
    url= f"https://finance.yahoo.com/lookup?s={stockName}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    a_tags = soup.select('table tbody tr td a')
    for i, a_tag in enumerate(a_tags[:11]):
        ticker = a_tag.text.strip()
        tickerName = a_tag.get("title","").strip()
        data.append({"index":i+1,"ticker":ticker,"name":tickerName})
    print(tabulate(data, headers="keys", tablefmt="pretty"))

    return data[0]['ticker'] if data else None
        
def getUserInput(data):
    """
    Prompts the user to select a ticker from the list.
    """
    getIndex= int(input("select the index of company you want to fetch:"))
    print("You selected: ",getIndex)
    if getIndex >0 and getIndex<11:
        print("selected ticker is: ",data[getIndex-1]['ticker'])
        return data[getIndex-1]['ticker']
    else:
        print("Invalid index. Please select a number between 1 and 10.")
        

def getStockInfo(stockName : str) -> str: 
    """
    Fetches the stock information for a given stock name.
    """
    getTicker(stockName)
    ticker= getUserInput(data)
    if ticker:
        stock = yf.Ticker(ticker)
        info = stock.info
        print(f"Company: {info.get('shortName')}")
        print(f"Ticker: {ticker}")
        return str(ticker)
    else:
        print(f"Could not find ticker for '{stockName}'.")
if __name__ == "__main__":
    getStockInfo()
     