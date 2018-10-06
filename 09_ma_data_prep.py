# moving average smoothing as data preparation
from pandas import read_csv
from matplotlib import pyplot

filename = 'daily-total-female-births.csv'
series = read_csv(filename, header=0, index_col=0, parse_dates=True, squeeze=True)

# tail-rolling average transform
rolling = series.rolling(window=3)
rolling_mean = rolling.mean()
print(rolling_mean.head(10))

# plot original and transformed dataset
series.plot()
rolling_mean.plot(color='red')
pyplot.show()

# zoomed plot original and transformed dataset
series[:100].plot()
rolling_mean[:100].plot(color='red')
pyplot.show()