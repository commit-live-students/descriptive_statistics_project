# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']

def calculate_statistics():
    mean=np.mean(sale_price)
    median=np.median(sale_price)
    mode=sale_price.mode()
    return mean,median,mode[0] #Returns numpy.int64 dtype for the mode

print calculate_statistics()
