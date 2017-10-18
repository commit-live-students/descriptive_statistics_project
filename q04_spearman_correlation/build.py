# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here

def spearman_correlation():
    return dataframe_1.loc[:,'SalePrice'].corr(dataframe_2.loc[:,'SalePrice'],'spearman')
