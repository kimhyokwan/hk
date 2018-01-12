import pandas_datareader.data as web
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

SEC = web.DataReader("005930.KS", "yahoo", start, yesterday)
SEC['Close'].plot(style='--')
plt.title('삼성전자 종가 시세')
plt.show()

print("chart ok")
