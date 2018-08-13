# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np 
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def correlation():
    sale_price1= dataframe_1.loc[:,'SalePrice']
    sale_price2= dataframe_2.loc[: ,'SalePrice']
    cor= np.corrcoef(sale_price1,sale_price2)
    return float(cor[0,1])
 
# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here




