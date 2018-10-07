# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
import statistics

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']
sale_price
def calculate_statistics():
    mean1=np.mean(sale_price)
    median1=np.median(sale_price)
    series1=np.array(sale_price)
    mode1=statistics.mode(series1)
    return(mean1,median1,np.int64(mode1))

calculate_statistics()
# Return mean,median & mode for the SalePrice Column
# Write your code here



