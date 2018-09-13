# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
import numpy as np
def correlation():
    list_1 = [dataframe_1['SalePrice']]
    list_2 = [dataframe_2['SalePrice']]
    corr_eff = np.corrcoef(list_1, list_2)[1,0]
    return corr_eff
    
corr_eff = correlation()

