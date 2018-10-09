# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    dataframe_1['rank1']=dataframe_1['SalePrice'].rank(ascending=True)
    dataframe_2['rank2']=dataframe_2['SalePrice'].rank(ascending=True)
    d=pd.concat([dataframe_1, dataframe_2], axis=1)
    d['d']=d['rank1']-d['rank2']
    d['ds']=d['d']**2
    n=6*sum(d['ds'].values)
    d=len(d['d'].values)*(len(d['d'].values)**2-1)
    spear_corr=1-(n/d)
    return spear_corr


