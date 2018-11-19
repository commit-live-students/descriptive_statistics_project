# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd


# Your code here

def spearman_correlation():
    dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
    dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

    return dataframe_1.SalePrice.corr(dataframe_2.SalePrice, method = 'spearman')

s=spearman_correlation()


