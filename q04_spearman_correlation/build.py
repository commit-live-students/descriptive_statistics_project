# %load q04_spearman_correlation/build.py
# Default Import
import numpy as np
import pandas as pd
import scipy.stats
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    x = dataframe_1['SalePrice']
    y = dataframe_2['SalePrice']
    xranks = pd.Series(x).rank()
    yranks = pd.Series(y).rank()
    r = list(scipy.stats.pearsonr(xranks, yranks))
    return r[0]
spearman_correlation()
(spearman_correlation())

