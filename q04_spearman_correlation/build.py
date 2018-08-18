# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import math as mth

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    dataframe_1['rank']=dataframe_1['SalePrice'].rank(ascending=1)
    dataframe_2['rank']=dataframe_2['SalePrice'].rank(ascending=1)
    d=abs(dataframe_1['rank']-dataframe_2['rank'])
    df=pd.DataFrame(d**2)
    sum=df.sum()
    n=len(df)
    s_c=1 - 6*sum/(n*(n**2-1))
    return float(s_c)

spearman_correlation()





