# moving average smoothing as feature engineering
from pandas import read_csv
from pandas import DataFrame
from pandas import concat

filename = 'daily-total-female-births.csv'
series = read_csv(filename, header=0, index_col=0, parse_dates=True, squeeze=True)
df = DataFrame(series.values)
width = 3
lag1 = df.shift(1)
lag3 = df.shift(width - 1)
window = lag3.rolling(window=width)
means = window.mean()
dataframe = concat([means, lag1, df], axis=1)
dataframe.columns = ['mean', 't', 't+1']
print(dataframe.head(10))