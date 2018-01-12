import numpy as np
import pandas as pd
import pandas_datareader.data as web
#font setting for window
#font setting for mac (AppleGothic)
import datetime
from datetime import date, timedelta

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

today = date.today()
startday = date.today() - timedelta(720)
yesterday = date.today() - timedelta(1)
#startday = '3/14/2014'
#yesterday = '4/14/2016'
print(yesterday)
#GoogleDailyReader??

SEC = web.DataReader("005930.KS", "yahoo", startday, yesterday)
print(SEC)

print(SEC.tail())

SEC['Log_Ret'] = np.log(SEC['Close']) / SEC['Close'].shift(1)
SEC['Volatility'] = SEC['Log_Ret'].rolling(window=252,center=False).std() * np.sqrt(252)

#%matplotlib inline
SEC[['Close','Volatility']].plot(subplots=True, color='blue',figsize=(8,6))

plt.show()