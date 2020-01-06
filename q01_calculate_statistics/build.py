# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']

# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    sale_price_mean = np.mean(sale_price)
    sale_price_median = np.median(sale_price)
    sale_price_mode = pd.Series.mode(sale_price)

    return sale_price_mean, sale_price_median, sale_price_mode.values[0]
    
calculate_statistics()


