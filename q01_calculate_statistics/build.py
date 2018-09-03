# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
import statistics as s

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    '''Calculate statistics'''
    mean = sale_price.mean()
    mode = sale_price.mode()[0]
    median = sale_price.median()
    return mean, median, mode

#call the function
calculate_statistics()







