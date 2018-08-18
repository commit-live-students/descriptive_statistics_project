# %load q01_calculate_statistics/build.py
# Default Imports

import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
def calculate_statistics():
    sale_price = data.loc[:, 'SalePrice']
    mean=np.mean(sale_price)
    median=sale_price.median()
    mode=sale_price.mode()
    return mean,median,mode[0]
mean,median,mode=calculate_statistics()




