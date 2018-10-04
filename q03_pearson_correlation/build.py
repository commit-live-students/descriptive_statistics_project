# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def correlation():
    sale_price1 = dataframe_1['SalePrice']
    sale_price2 = dataframe_2['SalePrice']
    r = np.corrcoef(sale_price1,sale_price2).astype(float)
    return r[0,1]
correlation()
 
# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here



