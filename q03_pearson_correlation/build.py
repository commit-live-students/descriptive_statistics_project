# Default Imports
import pandas as pd
import numpy as np
import math

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    df1 = dataframe_1['SalePrice']
    df2 = dataframe_2['SalePrice']
    df3 = df1 * df2
    df4 = df1*df1
    df5 = df2*df2
    sx = df1.sum()
    sy = df2.sum()
    sxy = df3.sum()
    sx2 = df4.sum()
    sy2 = df5.sum()
    sxsq = sx*sx
    sysq = sy*sy
    n = df1.shape[0]
    num = (n*sxy) - (sx*sy)
    den = math.sqrt((n*sx2 - sxsq)*(n*sy2 - sysq))
    ans = num / den
    return ans


#print correlation()
