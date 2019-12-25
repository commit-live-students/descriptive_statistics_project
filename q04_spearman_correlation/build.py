# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

from scipy.stats import spearmanr
# Your code here

def spearman_correlation():
    result=spearmanr(dataframe_1['SalePrice'],dataframe_2['SalePrice'])
    return(result[0])
spearman_correlation()

