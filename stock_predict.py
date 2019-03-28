import requests
import json

API_KEY = '58SXCV92ZE1JUZ62'
STOCK_NAME = 'AAPL'

r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + STOCK_NAME + '&outputsize=full&apikey=' + API_KEY)

result = r.json()
dataForAllDays = result['Time Series (Daily)']
dataForSingleDate = dataForAllDays['2019-03-22']
opening = dataForSingleDate['1. open']
high = dataForSingleDate['2. high']
low = dataForSingleDate['3. low']
average = (float(high) + float(low))/2
# print(high)
# print(low)
# print(average)
close = dataForSingleDate['4. close']
volume = dataForSingleDate['5. volume']
y = opening*1000
#print(y)
for x,y in dataForAllDays.items(): 
  print(y['1. open'])


#TEST TEST