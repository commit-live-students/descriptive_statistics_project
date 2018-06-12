# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
from pandas import DataFrame

def spearman_correlation():
    sales_price =DataFrame()
    sales_price['x']= dataframe_1['SalePrice']
    sales_price['y']= dataframe_2['SalePrice']
    sales_price.index= range(dataframe_1['SalePrice'].count())

    sales_price['x-rank']= sales_price['x'].rank(ascending=True)
    sales_price['y-rank']= sales_price['y'].rank(ascending=True)

    sales_price['d'] = sales_price['x-rank']- sales_price['y-rank']
    sales_price['d-squared'] =sales_price['d']**2

    d_squared_sum =sales_price['d-squared'].sum()
    n = sales_price['x'].count()
    r= 1 - (6*d_squared_sum/(n*(n**2 -1 )))
    return r




