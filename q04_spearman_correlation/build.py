# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import scipy.stats as stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    s=stats.spearmanr(dataframe_1['SalePrice'],dataframe_2['SalePrice'])
    return s[0]
spearman_correlation()


