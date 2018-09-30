# create date time features of a dataset
from pandas import read_csv
from pandas import DataFrame

filename = 'daily-minimum-temperatures.csv'
series = read_csv(filename, header=0, index_col=0, parse_dates=True, squeeze=True)
dataframe = DataFrame()
dataframe['month'] = [series.index[i].month for i in range(series.size)]
dataframe['day'] = [series.index[i].day for i in range(series.size)]
dataframe['temperature'] = [series[i] for i in range(series.size)]
print(dataframe.head(5))