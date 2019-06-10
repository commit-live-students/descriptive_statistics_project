# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    salePrice1 = dataframe_1.loc[:,'SalePrice']
    salePrice2 = dataframe_2.loc[:,'SalePrice']
    combined = pd.concat([salePrice1,salePrice2],axis=1)
    return float(combined.iloc[:,0].corr(combined.iloc[:,1]))



