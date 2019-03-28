import requests
import json
import matplotlib.pyplot as plt

API_KEY = '58SXCV92ZE1JUZ62'
STOCK_NAME = 'AAPL'

r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + STOCK_NAME + '&outputsize=full&apikey=' + API_KEY)

result = r.json()
dataForAllDays = result['Time Series (Daily)'] 
#     key: '2019-03-22' 
#     value: {
#     "1. open": "188.9500",
#     "2. high": "189.5500",
#     "3. low": "187.8200",
#     "4. close": "188.4400",
#     "5. volume": "7570388"
# }
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

dates = []
closing_price = []
for x,y in dataForAllDays.items(): 
  dates.append(x)
  closing_price.append(float(y['4. close']))

plt.plot(closing_price[5000:])
plt.show()

#TEST TEST