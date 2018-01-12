import pandas_datareader as pdr
import datetime
SEC = pdr.get_data_yahoo('005930.KS',
                          start=datetime.datetime(2017, 12, 1),
                          end=datetime.datetime(2017, 12, 19))
print(SEC)