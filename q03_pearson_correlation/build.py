# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

SalePrice1 = dataframe_1.loc[:, 'SalePrice']
SalePrice2 = dataframe_2.loc[:, 'SalePrice']
# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here

# Return the correlation value between the SalePrice column for the two loaded datasets
def correlation():
    return dataframe_1.SalePrice.corr(dataframe_2.SalePrice, method='pearson')
