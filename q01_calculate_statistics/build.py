# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']


def calculate_statistics():
    return (float(np.mean(sale_price)), float(np.median(sale_price)), sale_price.mode()[0])


