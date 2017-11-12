# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
house_price = dataframe_1.loc[:,'SalePrice']
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
house_price2 = dataframe_2.loc[:,'SalePrice']

# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    a = np.corrcoef(house_price,house_price2)
    b = a[0,1]
    return b
