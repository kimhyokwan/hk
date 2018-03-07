import pandas_datareader.data as web
import fix_yahoo_finance as yf
yf.pdr_override()
import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt
#font setting for window
#font setting for mac (AppleGothic)
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

today = date.today()
start = date.today() - timedelta(14)
yesterday = date.today() - timedelta(1)
print(yesterday)
# data_source = 'google'
# 005930.KS
SEC = web.get_data_yahoo("GOOG", start, yesterday)
SEC['Close'].plot(style='--')
plt.title('삼성전자 종가 시세')
plt.show()

print("chart ok")
