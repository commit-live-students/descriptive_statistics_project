# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
import scipy
def spearman_correlation():
    d =  - dataframe_1['SalePrice']
    d_squared = d ** 2
    return pd.concat([dataframe_2['SalePrice'],dataframe_1['SalePrice']], axis=1).corr(method='spearman')['SalePrice'].iloc[0,1]



