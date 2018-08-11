# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
from statistics import mode
from numpy import int64

def calculate_statistics():
    data = pd.read_csv('data/house_prices_multivariate.csv')
    sale_price = data.loc[:, 'SalePrice']
    mean = np.mean(sale_price)
    median = np.median(sale_price)
    mod = mode(sale_price)
    median = float(median)
    mod = int64(mod)
    print(type(mod))
    return (mean, median, mod)

# Return mean,median & mode for the SalePrice Column
# Write your code here


calculate_statistics()


