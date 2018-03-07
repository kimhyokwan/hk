from pandas_datareader import data
import fix_yahoo_finance as yf

yf.pdr_override()

symbol = 'AMZN'
data_source = 'google'
start_date = '2018-01-01'
end_date = '2018-03-07'
df = data.get_data_yahoo(symbol, start_date, end_date)

print(df)