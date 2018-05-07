# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np
from scipy import stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    pc1 = dataframe_1.loc[ :, 'SalePrice']
    pc2 = dataframe_2.loc[ :, 'SalePrice']
    return float(stats.spearmanr(pc1, pc2)[0])



