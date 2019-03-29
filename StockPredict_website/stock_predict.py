import requests
import json
import matplotlib.pyplot as plt
import re
import numpy as np
import pandas as pd

API_KEY = '58SXCV92ZE1JUZ62'

STOCK_NAME = 'AAPL'

def gradient_descent(alpha, x, y, m, day):
  theta0 = 1
  theta1 = 1

  prevJ = 2
  J = 0

  while abs(J - prevJ) > 1:
    temp0 = theta0
    temp1 = theta1
    prediction = theta1 * x + theta0

    # print(prediction)

    #check J function for convergence
    J = sum(np.square(prediction - y)) / 2 / m
    # if abs(J - prevJ) <= 0.1:
    #     break

    dJ0 = sum(prediction - y) / m
    dJ1 = sum((prediction - y) * np.transpose(x)) / m
    theta0 -= alpha * dJ0
    theta1 -= alpha * dJ1
    prevJ = J

  return theta1 * day + theta0

def getStock(stock_name, api_key): 
  r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stock_name + '&outputsize=full&apikey=' + api_key)
  json_data = json.loads(r.text)

  result = r.json()
  dataForAllDays = result['Time Series (Daily)'] 
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
  # print(df)

  #GRADIENT DESCENT MODEL

  alpha = 0.015
  y = np.array(df['closing_price'])[-10:]
  x = np.array(range(1,len(y)+1))
  day = 11
  m = len(y)

  return round(gradient_descent(alpha, x, y, m, day), 2)

value_aapl = getStock('AAPL', 'GZYB3BJNXMLWVDWY')
value_asxxro = 0#getStock('ASX:XRO', '58SXCV92ZE1JUZ62')
value_chase = 0#getStock('JPM', '58SXCV92ZE1JUZ62')
value_nintendo = 0#getStock('TYO', '58SXCV92ZE1JUZ62')
value_netflix = 0#getStock('NFLX', '58SXCV92ZE1JUZ62')


from flask import Flask, render_template             
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html", apple=value_aapl, xero=value_asxxro, chase=value_chase, nintendo=value_nintendo, netflix=value_netflix)

if __name__ == "__main__":
    app.run(debug=True)