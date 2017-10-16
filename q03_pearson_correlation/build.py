# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    s1,s2=(pearsonr(dataframe_1['SalePrice'],dataframe_2['SalePrice']))
    return(s1)


#correlation()
