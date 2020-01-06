# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

def calculate_statistics():
    data = pd.read_csv('data/house_prices_multivariate.csv')
    sale_price = data.loc[:, 'SalePrice']

    return sale_price.mean(),sale_price.median(),sale_price.mode()[0]

calculate_statistics()


