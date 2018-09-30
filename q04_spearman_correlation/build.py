# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    dataframe_1['Rank1'] = dataframe_1['SalePrice'].rank()
    dataframe_2['Rank2'] = dataframe_2['SalePrice'].rank()
    dataframe_1['d'] = (dataframe_1['Rank1'] - dataframe_2['Rank2'])**2
    sum_d_squared = dataframe_1.d.sum()
    n = len(dataframe_1.axes[0])
    spearman_correlation_coeff = 1 - ((6 * sum_d_squared)/(n*((n**2)-1)))
    return spearman_correlation_coeff


