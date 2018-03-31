# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here

SalePrice1 = dataframe_1.loc[:, 'SalePrice']
SalePrice2 = dataframe_2.loc[:, 'SalePrice']
# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here

def spearman_correlation():
    return dataframe_1.SalePrice.corr(dataframe_2.SalePrice, method='spearman')
