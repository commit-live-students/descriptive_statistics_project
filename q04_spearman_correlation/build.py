# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np
from scipy.stats import spearmanr
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    f1 = dataframe_1['SalePrice']
    f2 = dataframe_2['SalePrice']
    # Your code here
    corr = float(format(spearmanr(f1,f2)[0],'.12'))
    return corr

spearman_correlation()

