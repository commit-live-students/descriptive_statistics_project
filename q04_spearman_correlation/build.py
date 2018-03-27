# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
from scipy.stats import spearmanr

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    SCC = spearmanr(dataframe_1['SalePrice'],dataframe_2['SalePrice'])
    return (SCC[0])
spearman_correlation()


