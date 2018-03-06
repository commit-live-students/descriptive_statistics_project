# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def correlation():
    x = dataframe_1.loc[:,'SalePrice']
    y = dataframe_2.loc[:,'SalePrice']
    return dataframe_1.SalePrice.corr(dataframe_2.SalePrice, method ='pearson')

correlation()
# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
