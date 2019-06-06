# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    sp1=dataframe_1.loc[:,'SalePrice']
    sp2=dataframe_2.loc[:,'SalePrice']
    df1=pd.DataFrame(sp1)
    df1['c2']=sp2
    corr=df1.corr(method='spearman').iloc[0,1]
    return corr

