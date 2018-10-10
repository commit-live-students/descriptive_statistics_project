# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sp = data.loc[:, 'SalePrice'] #sale price


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean=np.mean(data.SalePrice)
    med=np.median(data.SalePrice)
    mod1 = np.asarray(data.SalePrice.mode(), dtype=np.int64)
    mod = np.int_(mod1.item())
    return mean,med,mod


calculate_statistics()






