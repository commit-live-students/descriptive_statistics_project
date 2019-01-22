# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
from scipy import stats
#import statistics 
#stats.mode(expenditure)

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']


# Return mean,median & mode for the SalePrice Column
# Write your code here


print(sale_price)
mean = np.average(list(map(float, sale_price)))

print(mean)
median = np.median(list(map(float, sale_price)))

def calculate_statistics():
#    mode_series = pd.Series()
    mean = np.average(list(map(float, sale_price)))
    median = np.median(list(map(float, sale_price)))
  # mode = pd.Series(list(stats.mode(sale_price)))
    mode = pd.Series.mode(sale_price)
    return mean , median ,mode[0]
    
calculate_statistics()


