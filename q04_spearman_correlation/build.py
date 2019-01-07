# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np
import scipy as sc

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
saleprice1 = dataframe_1.loc[:, 'SalePrice']
saleprice2 = dataframe_2.loc[:, 'SalePrice']

def spearman_correlation():
    
    df = pd.concat([saleprice1,saleprice2], axis=1).corr(method='spearman').iloc[0,-1]
    return df


