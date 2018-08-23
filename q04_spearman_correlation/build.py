# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    x=pd.DataFrame(dataframe_1.SalePrice)
    y=pd.DataFrame(dataframe_2.SalePrice)
    xsorted=x.sort_values('SalePrice')
    xran=np.arange(len(x))
    xranked=pd.DataFrame(index=xsorted.index.values,data=xran)
    xranked.rename(columns={0:'Rank1'},inplace=True)
    x=x.join(xranked)

    ysorted=y.sort_values('SalePrice')
    xran=np.arange(len(x))
    yranked=pd.DataFrame(index=ysorted.index.values,data=xran)
    yranked.rename(columns={0:'Rank2'},inplace=True)
    y.rename(columns={'SalePrice':'SalePrice2'},inplace=True)
    y=y.join(yranked)
    x=x.join(y)
    d=pd.DataFrame(x.Rank1-x.Rank2)
    d2=d**2
    x=x.join(d)
    x.rename(columns={0:'d'},inplace=True)
    x=x.join(d2)
    x.rename(columns={0:'d2'},inplace=True)
    sprc=6*x.d2.sum()/(len(x)**3-len(x))
    return x[['SalePrice','SalePrice2']].corr()['SalePrice'][1]
    

spearman_correlation()

