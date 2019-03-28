import requests
import json
import matplotlib.pyplot as plt
import re
import numpy as np
import pandas as pd

API_KEY = '58SXCV92ZE1JUZ62'
STOCK_NAME = 'AAPL'

r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + STOCK_NAME + '&outputsize=full&apikey=' + API_KEY)
json_data = json.loads(r.text)
# print(json_data)
# print(json_data['Time Series (Daily)']['2019-03-22']['4. close'])

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
close = dataForSingleDate['4. close']
volume = dataForSingleDate['5. volume']

dates = []
closing_price = []
for x,y in dataForAllDays.items(): 
  dates.append(x)
  closing_price.append(float(y['4. close']))

# print(dates)

df = pd.DataFrame({
  'dates' : dates,
  'closing_price' : closing_price,
})

# print(df)
df = df.sort_values(by=['dates'])
print(df)

#GRADIENT DESCENT MODEL

theta0 = 1
theta1 = 1
alpha = 0.0001
y = np.array(df['closing_price'])[-10:]
x = np.array(range(1,len(y)+1))
m = len(y)
print(y)

for i in range(0,15):
    temp0 = theta0
    temp1 = theta1
    prediction = temp1 * x + temp0
    theta0 = temp0 - alpha * sum(prediction - y) / m
    theta1 = temp1 - alpha * sum((prediction - y) * np.transpose(x)) / m

print('\n',theta1 * 344 + theta0)

#GRADIENT DESCENT MODEL