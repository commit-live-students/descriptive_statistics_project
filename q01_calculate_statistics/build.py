# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']
# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean1 = np.mean(sale_price)
    median1 = np.median(sale_price)
    mode1 = pd.Series.mode(sale_price)
    return mean1,median1,mode1.values[0]



