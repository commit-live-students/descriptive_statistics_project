# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    salePrice1 = dataframe_1.loc[:,'SalePrice']
    salePrice2 = dataframe_2.loc[:,'SalePrice']
    combined = pd.concat([salePrice1,salePrice2], axis=1)
    return float(combined.corr('spearman').iloc[0,1])


