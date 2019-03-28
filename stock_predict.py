import requests

API_KEY = '58SXCV92ZE1JUZ62'
STOCK_NAME = 'AAPL'

r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + STOCK_NAME + '&outputsize=full&apikey=' + API_KEY)

result = r.json()
dataForAllDays = result['Time Series (Daily)']
dataForSingleDate = dataForAllDays['2019-03-22']
x = dataForSingleDate['1. open']
y = x*1000
print(y)