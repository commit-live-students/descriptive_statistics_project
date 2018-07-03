# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    sp1=dataframe_1.loc[:,'SalePrice']
    sp2=dataframe_2.loc[:,'SalePrice']
    r=np.corrcoef(sp1,sp2)[0,1]
    return r


