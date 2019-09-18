# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']


def calculate_statistics():
    Mean = sale_price.mean()
    Median = np.median(sale_price)
    Mode = sale_price.mode()
    # type(M)
    return Mean, Median, Mode[0]


