# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean=data.loc[:, 'SalePrice'].mean()
    median=data.loc[:, 'SalePrice'].median()
    mode=data.loc[:, 'SalePrice'].mode()
    return mean,median,mode

calculate_statistics()
data.loc[:, 'SalePrice'].mean()
data.loc[:, 'SalePrice'].median()
data.loc[:, 'SalePrice'].mode()

