import yfinance as yf
import argparse
import fetchTicketSymbol  
from tabulate import tabulate
def main():
    parser=argparse.ArgumentParser()
    # parser.add_argument("--stockName", help="Stock Name",required=True) #OPTIONAL
    parser.add_argument("stockName", help="Stock Name") 
    argv = parser.parse_args()
    print("argv is",argv)
    print ("StockName is",argv.stockName)
    stockName=fetchTicketSymbol.getStockInfo(argv.stockName)

    stock=yf.Ticker(stockName)
    stockData=stock.history(period="1d")
    if stockData.empty:
        print("No data found for the given stock. possibly delisted")
        return
    stockDetails={
        "Open": stockData["Open"].iloc[0],
        "Close": stockData["Close"].iloc[0],
        "Low": stockData["Low"].iloc[0],
        "High": stockData["High"].iloc[0]
    }
    
    print(tabulate(stockDetails.items(), headers=["Metric", "Value"], tablefmt="pretty"))
    # print("This is a stock price module.",stockDetails)
if __name__ == "__main__":
    main()