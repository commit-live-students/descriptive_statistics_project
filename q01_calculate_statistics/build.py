# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']

#
    

# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean1=sale_price.mean()
    median1=sale_price.median()
    mode1=sale_price.mode()
    mode2=np.int64(mode1[0])
    return mean1, median1, mode2


