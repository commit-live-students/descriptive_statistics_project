# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here


# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
def correlation():
    r = dataframe_1['SalePrice'].corr(dataframe_2['SalePrice'])
    return r
