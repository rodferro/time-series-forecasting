# create a lag feature
from pandas import read_csv
from pandas import DataFrame
from pandas import concat

filename = 'daily-minimum-temperatures.csv'
series = read_csv(filename, header=0, index_col=0, parse_dates=True, squeeze=True)
temps = DataFrame(series.values)
dataframe = concat([temps.shift(1), temps], axis=1)
dataframe.columns = ['t', 't+1']
print(dataframe.head(5))