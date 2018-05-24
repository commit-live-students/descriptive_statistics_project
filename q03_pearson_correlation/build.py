# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
sale_price1 = dataframe_1.loc[:, 'SalePrice']
sale_price2 = dataframe_2.loc[:, 'SalePrice']

# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    corsale1=np.corrcoef(sale_price2, sale_price1)[0,1]
    corsale=corsale1.astype(type('float', (float,), {}))#  create an anonymous type float
    corsale2='{0:.13f}'.format(round(corsale,13))
    return corsale2


