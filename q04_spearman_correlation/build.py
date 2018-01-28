'''---------------------------------------------My code---------------------------------------------------------#
# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np
import math
pd.options.display.float_format = '{:.2f}'.format


dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here

df1 = pd.DataFrame(dataframe_1.loc[:,'SalePrice']).sort_values('SalePrice')
df2 = pd.DataFrame(dataframe_2.loc[:,'SalePrice']).sort_values('SalePrice')
df2 = pd.DataFrame(df2.reset_index()['SalePrice'])
df1 = pd.DataFrame(df1.reset_index()['SalePrice'])

df3 = pd.merge(df1,df2,left_index=True,right_index=True)

def conv(row):
    a = float(row['SalePrice_y'])
    return a

df3['SalePrice_y'] = df3.apply(conv,axis=1)
#df3['SalePrice_z'] = np.int64(df3['SalePrice_y'])

def func(row):
    return row['SalePrice_x'] - row['SalePrice_y']
df3['Difference'] = df3.apply(func, axis=1)

def sqfunc(row):
    return row['Difference'] * row['Difference']

df3['square'] = df3.apply(sqfunc, axis = 1)
print df3.head()
total = 0

def tot(row):
    global total
    total = total + row['square']
    return total

fintot=df3.apply(tot,axis = 1)

print fintot.tail()

print df3

#---------------------------------------------My code---------------------------------------------------------'''

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

spearman_correlation()


