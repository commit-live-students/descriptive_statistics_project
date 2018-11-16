# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
import statistics as s

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']
# sale_price = np.array(sale_price)

# Return mean,median & mode for the SalePrice Column
# Write your code here

def calculate_statistics():
    mean = np.mean(sale_price)
    median = np.median(sale_price)
    mode = sale_price.mode()
    
    return mean, median, mode[0]

calculate_statistics()


calculate_statistics


