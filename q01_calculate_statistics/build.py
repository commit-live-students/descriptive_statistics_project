# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']


# Return mean,median & mode for the SalePrice Column
# Write your code here


def calculate_statistics():
    mean=sale_price.mean()
    median=sale_price.median()
    mode=np.array(sale_price.mode(), dtype=np.int64)
    return mean,median,mode[0]


print(calculate_statistics())

