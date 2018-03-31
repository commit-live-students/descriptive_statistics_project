# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np
from scipy.stats import spearmanr


dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
df1 = dataframe_1['SalePrice'].rank(ascending=True)
df2 = dataframe_2['SalePrice'].rank(ascending=True)
# Your code here
df1['d']=df1-df2
df1['d-squared']=df1['d']**2
a = df1['d-squared'].sum()
a = a*6
n=dataframe_1.shape[0]
n
def spearman_correlation():
    return 1-a/(n*(n**2-1))
spearman_correlation()
                




