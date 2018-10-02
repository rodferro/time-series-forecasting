# create a histogram plot
from pandas import read_csv
from matplotlib import pyplot

filename = 'daily-minimum-temperatures.csv'
series = read_csv(filename, header=0, index_col=0, parse_dates=True, squeeze=True)
series.hist()
pyplot.show()