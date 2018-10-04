# upsample to daily intervals
from pandas import read_csv
from pandas import datetime

def parser(x):
    return datetime.strptime('190'+x, '%Y-%m')

filename = 'shampoo-sales.csv'
series = read_csv(filename, header=0, index_col=0, parse_dates=True, squeeze=True, 
    date_parser=parser)
upsampled = series.resample('D').mean()
print(upsampled.head(32))