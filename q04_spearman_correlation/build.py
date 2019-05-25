# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    x=dataframe_1['SalePrice']
    y=dataframe_2['SalePrice']
    r=pd.concat([x,y], axis=1).corr(method="spearman").iloc[-2,-1]
    r1=float(r)
    return r1
