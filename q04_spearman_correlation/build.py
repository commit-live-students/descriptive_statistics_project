# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here

def spearman_correlation():
    SalePrice1 = dataframe_1['SalePrice']
    SalePrice2 = dataframe_2['SalePrice']
    return SalePrice1.corr(SalePrice2,method="spearman")
