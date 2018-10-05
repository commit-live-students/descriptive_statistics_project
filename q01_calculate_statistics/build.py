# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    arr = np.asarray(data.SalePrice.mode(), dtype=np.int64)
    a = np.int_(arr.item())
    return np.mean(data.SalePrice),np.median(data.SalePrice),a

#type(().astype(np.int64))
#type(np.array().astype(np.int64))
#type()

#type(a)
#type(np.int64(arr).item())


