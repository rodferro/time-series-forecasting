# load and plot a time series
from pandas import read_csv
from matplotlib import pyplot

filename = 'airline-passengers.csv'
series = read_csv(filename, header=0, index_col=0, parse_dates=True,
    squeeze=True)
pyplot.figure(1)

# line plot
pyplot.subplot(211)
pyplot.plot(series)

# histogram
pyplot.subplot(212)
pyplot.hist(series)
pyplot.show()