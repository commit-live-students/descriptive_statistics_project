# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here

def spearman_correlation():
    df1= (dataframe_1.loc[:,['SalePrice']]).rank()
    df1['SalePrice2']= (dataframe_2.loc[:,['SalePrice']]).rank()
    df1['d']=df1['SalePrice']-df1['SalePrice2']
    df1['d2']=df1['d']**2
    n=df1['d2'].count()
    s= df1['d2'].sum()
    e= 1-(6*s/(n*(n**2-1)))
    return e

spearman_correlation()
#0.0485967326141


