# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np
import scipy.stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    
    return scipy.stats.pearsonr(dataframe_1['SalePrice'],dataframe_2['SalePrice'])[0]
    
correlation()



