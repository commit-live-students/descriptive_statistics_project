# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean=np.mean(sale_price)
    median=np.median(sale_price)
    values,count=np.unique(sale_price,return_counts=True)
    mode=values[np.argmax(count)]
    return mean,median,mode



