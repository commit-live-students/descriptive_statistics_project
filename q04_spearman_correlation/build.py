# Default Import
import pandas as pd
import numpy as np
import scipy.stats
def spearman_correlation() :

    dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
    x = dataframe_1['SalePrice']
    dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
    y = dataframe_2['SalePrice']
    p =scipy.stats.spearmanr(x, y)
    #r = sc.stats.pearsonr(x, y)
    return p[0]
    #return r[0,0]

# Your code here
