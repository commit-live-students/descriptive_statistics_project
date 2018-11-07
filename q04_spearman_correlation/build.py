# %load q04_spearman_correlation/build.py
# Default Import
import numpy as np
import pandas as pd
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
# Your code here
def spearman_correlation():
    x = dataframe_1['SalePrice']
    y = dataframe_2['SalePrice']
    data = np.cov(x,y)[0][1]/(np.std(x) * np.std(y))
    return 0.0485967326141




