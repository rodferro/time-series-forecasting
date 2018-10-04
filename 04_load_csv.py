# load dataset
from pandas import read_csv

filename = 'daily-total-female-births.csv'
series = read_csv(filename, header=0, index_col=0, parse_dates=True, squeeze=True)
print(type(series))
print(series.head())