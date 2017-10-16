# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np
from scipy.stats.stats import spearmanr

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    s1,s2= spearmanr(dataframe_1['SalePrice'],dataframe_2['SalePrice'])

    return (s1)


#spearman_correlation()
