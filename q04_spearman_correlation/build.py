# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
from pandas import DataFrame

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    x=pd.DataFrame(dataframe_1['SalePrice'])
    y=pd.DataFrame(dataframe_2['SalePrice'])
    
    x['rank']=x['SalePrice'].rank(ascending=True)
    y['rank']=y['SalePrice'].rank(ascending=True)
    
    dsquare=(x['rank']-y['rank'])**2
    n=dsquare.shape[0]
    
    num=float(6*sum(dsquare))
    den=n*(n**2-1)
    
    spear_coeff=(1-num/den)
    return spear_coeff

