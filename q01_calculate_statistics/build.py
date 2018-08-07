# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
from statistics import mode

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean1=float(sale_price.mean())
    median1 = float(sale_price.median())
    mode1 = np.int64(mode(sale_price))
    return mean1,median1,mode1
calculate_statistics()


