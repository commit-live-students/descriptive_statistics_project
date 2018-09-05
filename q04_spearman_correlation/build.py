# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import scipy.stats as s

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    
    X = dataframe_1['SalePrice']
    Y = dataframe_2['SalePrice']
    return s.spearmanr(X,Y)[0]


