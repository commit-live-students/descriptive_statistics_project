# %load q01_calculate_statistics/build.py
# Default Imports

import pandas as pd
import numpy as np

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']



# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean=sale_price.mean()
    median=sale_price.median()
    mode=sale_price.mode()
    mode = np.dtype('int64').type(mode)
    print(type(mode[0]))
    
    
    return mean,median,mode[0]

calculate_statistics()











