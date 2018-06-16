# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import scipy
import scipy.stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    dataframe_1['d']=dataframe_1.loc[:,'SalePrice']
    dataframe_2['d']=dataframe_2.loc[:,'SalePrice']
    
    rs= scipy.stats.spearmanr(dataframe_1['d'],dataframe_2['d'])
    return rs[0]

spearman_correlation()




