# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']


# Return mean,median & mode for the SalePrice Column
# Write your code here

def calculate_statistics():
    a_mean = np.mean(sale_price)
    a_median = np.median(sale_price)
    a_mode = sale_price.mode()
    b = a_mode.astype('int64')
    return a_mean, a_median,np.array(b)[0]





