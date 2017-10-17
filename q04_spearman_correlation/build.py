# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np
import scipy.stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here

def spearman_correlation():
    c= scipy.stats.spearmanr(dataframe_1['SalePrice'],dataframe_2['SalePrice']).correlation
    c.astype(float)
    return c
