# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    s_1=dataframe_1.loc[:,'SalePrice']
    s_2=dataframe_2.loc[:,'SalePrice']
    df1=pd.DataFrame(s_1)
    df1['c2']=s_2
    corr=df1.corr(method='spearman').iloc[0,1]
    return corr


