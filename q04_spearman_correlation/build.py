# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np
import scipy.stats as stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here

def spearman_correlation():
    d1=dataframe_1.SalePrice
    d2=dataframe_2.SalePrice
    return stats.spearmanr(d1,d2).correlation











