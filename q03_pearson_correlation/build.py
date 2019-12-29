# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
import numpy as np
import matplotlib.pyplot as plt
def correlation():
    coef = np.corrcoef(x = dataframe_1['SalePrice'], y = dataframe_2['SalePrice'])
    return coef[0][1]


