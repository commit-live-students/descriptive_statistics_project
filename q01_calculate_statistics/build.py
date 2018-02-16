# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']

def calculate_statistics():
    Mean = sale_price.mean()
    Median = sale_price.median()
    Mode = sale_price.mode().iloc[0]
    return Mean, Median, Mode 


# Return mean,median & mode for the SalePrice Column
# Write your code here




