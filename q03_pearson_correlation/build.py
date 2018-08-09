# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here

def correlation():
    sale1 =pd.Series(dataframe_1['SalePrice'])
    sale2 = pd.Series(dataframe_2['SalePrice'])
    corr = np.corrcoef(sale1,sale2)[0,1]
    return corr

correlation()
  




