# downsample to quarterly intervals
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot

def parser(x):
    return datetime.strptime('190'+x, '%Y-%m')

filename = 'shampoo-sales.csv'
series = read_csv(filename, header=0, index_col=0, parse_dates=True, squeeze=True,
    date_parser=parser)
resample = series.resample('Q')
quarterly_mean_sales = resample.mean()
print(quarterly_mean_sales)
quarterly_mean_sales.plot()
pyplot.show()