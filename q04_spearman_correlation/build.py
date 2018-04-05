# Default Import
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    d1 = pd.DataFrame(dataframe_1['SalePrice'])
    d2 = pd.DataFrame(dataframe_2['SalePrice'])

    d1['Rank1'] = np.argsort(d1['SalePrice']).sort_values().index #d1.sort_values(by='SalePrice').index
    d1['Rank2'] = np.argsort(d2['SalePrice']).sort_values().index #d1.sort_values(by='SalePrice').index

    d1['d'] = d1['Rank1'] - d1['Rank2']
    d1['d_square'] = d1['d']**2
    sp_sum = d1['d_square'].sum()
    n = d1.shape[0]
    sp = 1 - 6*(sp_sum/(n * (n**2-1)))
    #print(sp)
    return sp


spearman_correlation()
